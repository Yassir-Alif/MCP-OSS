import sys
import logging
from core.intent_manager import IntentLifecycleManager
from agent.agent_facade import AgentFacade
from models import Intent, IntentState

# Configure logging to stdout
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def main():
    print("--- AISys L-MCP Reference Implementation ---")
    print("Normative Architecture: MCP-OSS_Architektur-Modell_v1.0")
    
    # Bootstrap
    agent = AgentFacade()
    lifecycle_manager = IntentLifecycleManager(agent)
    
    while True:
        print("\nOptions:")
        print("1. Create Intent: List Files (fs.list)")
        print("2. Create Intent: Read File (fs.read)")
        print("3. Create Intent: Forbidden Tool (system.delete)")
        print("4. Exit")
        
        choice = input("Select: ")
        
        intent = None
        tool = ""
        params = {}
        
        if choice == "1":
            path = input("Path to list (default: .): ") or "."
            intent = Intent(source="CLI_User", content=f"List files in {path}")
            tool = "fs.list"
            params = {"path": path}
            
        elif choice == "2":
            path = input("Path to read: ")
            intent = Intent(source="CLI_User", content=f"Read file {path}")
            tool = "fs.read"
            params = {"path": path}
            
        elif choice == "3":
            # Demostrate DENIED
            intent = Intent(source="CLI_User", content="Delete system")
            tool = "system.delete"
            params = {"force": True}
            
        elif choice == "4":
            sys.exit(0)
        else:
            continue
            
        if intent:
            print(f"\n[Flow] Intent CREATED: {intent.id}")
            print(f"[Flow] Submitting to Core...")
            
            final_intent = lifecycle_manager.process_intent(intent, tool, params)
            
            print("\n--- Final Status ---")
            print(f"State: {final_intent.current_state}")
            print("History:")
            for step in final_intent.history:
                print(f" -> {step.from_state} to {step.to_state} | Trigger: {step.trigger}")

if __name__ == "__main__":
    main()
