
/**
 * AISys UI - Main Application Logic
 * Implements Read-Only MCP Client behavior.
 */

// Configuration
const API_BASE = './mock/api.json';

// State
let appState = {
    currentView: 'dashboard',
    data: null,
    selectedIntentId: null
};

// Utils
const $ = (selector) => document.querySelector(selector);
const formatTime = (isoString) => new Date(isoString).toLocaleString();

// Navigation
function navigateTo(view, param = null) {
    console.log(`Navigating to ${view} with param ${param}`);
    appState.currentView = view;
    appState.selectedIntentId = param;

    // Update active link
    document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));
    const activeLink = document.querySelector(`[data-view="${view}"]`);
    if (activeLink) activeLink.classList.add('active');

    render();
}

// Data Fetching
async function fetchData() {
    try {
        const response = await fetch(API_BASE);
        appState.data = await response.json();
        console.log("Data fetched:", appState.data);
    } catch (error) {
        console.error("Failed to fetch data:", error);
        $('#view-container').innerHTML = `<div class="card"><h3 class="text-danger">Connection Error</h3><p>Could not load data from ${API_BASE}</p></div>`;
    }
}

// Rendering Engine
async function render() {
    if (!appState.data) await fetchData();
    const container = $('#view-container');

    switch (appState.currentView) {
        case 'dashboard':
            container.innerHTML = renderDashboard();
            break;
        case 'intents':
            container.innerHTML = renderIntentExplorer();
            break;
        case 'intent_detail':
            container.innerHTML = renderIntentDetail(appState.selectedIntentId);
            break;
        case 'capabilities':
            container.innerHTML = renderCapabilities();
            break;
        default:
            container.innerHTML = '<h1>404 Not Found</h1>';
    }
}

// Views
function renderDashboard() {
    const { stats, health, intents } = appState.data;
    // Get last 5 activities
    const recent = intents.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp)).slice(0, 5);

    return `
        <div class="header">
            <h1 class="page-title">Dashboard</h1>
            <div class="badge state-EXECUTED">System Online</div>
        </div>

        <div class="grid-3">
            <div class="card">
                <h3>Active Intents</h3>
                <div class="metric-value">${stats.active_intents}</div>
            </div>
            <div class="card">
                <h3>Core Health</h3>
                <div class="metric-value text-success">${health.core.toUpperCase()}</div>
            </div>
            <div class="card">
                <h3>Agent Status</h3>
                <div class="metric-value ${health.agent === 'online' ? 'text-success' : 'text-danger'}">${health.agent.toUpperCase()}</div>
            </div>
        </div>
        
        <div class="card">
            <h3>Recent Activity Feed</h3>
            <table>
                <thead>
                    <tr>
                         <th>ID</th>
                         <th>Source</th>
                         <th>Action</th>
                         <th>State</th>
                         <th>Time</th>
                    </tr>
                </thead>
                <tbody>
                    ${recent.map(intent => `
                        <tr onclick="navigateTo('intent_detail', '${intent.id}')">
                            <td>#${intent.id.split('-')[1]}</td>
                            <td>${intent.source}</td>
                            <td>${intent.content}</td>
                            <td><span class="badge state-${intent.current_state}">${intent.current_state}</span></td>
                            <td>${formatTime(intent.timestamp)}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        </div>
    `;
}

function renderIntentExplorer() {
    const { intents } = appState.data;
    // filter logic could go here

    return `
        <div class="header">
            <h1 class="page-title">Intent Explorer</h1>
        </div>
        <div class="card">
            <table>
                <thead>
                    <tr>
                         <th>Intent ID</th>
                         <th>Source</th>
                         <th>Content</th>
                         <th>Current State</th>
                         <th>Created At</th>
                    </tr>
                </thead>
                <tbody>
                    ${intents.map(intent => `
                        <tr onclick="navigateTo('intent_detail', '${intent.id}')">
                            <td>${intent.id}</td>
                            <td>${intent.source}</td>
                            <td>${intent.content}</td>
                            <td><span class="badge state-${intent.current_state}">${intent.current_state}</span></td>
                            <td>${formatTime(intent.timestamp)}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        </div>
    `;
}

function renderIntentDetail(id) {
    const intent = appState.data.intents.find(i => i.id === id);
    if (!intent) return '<h1>Intent not found</h1>';

    return `
        <div class="header">
            <div>
                <button onclick="navigateTo('intents')" style="background:none; border:none; color:var(--text-muted); cursor:pointer; margin-bottom:10px;">← Back to Explorer</button>
                <h1 class="page-title">Intent ${intent.id}</h1>
            </div>
            <span class="badge state-${intent.current_state}" style="font-size: 1rem; padding: 10px 20px;">${intent.current_state}</span>
        </div>

        <div class="grid-3">
             <div class="card">
                <h3>Source</h3>
                <div>${intent.source}</div>
             </div>
             <div class="card">
                <h3>Content (Intent)</h3>
                <div>${intent.content}</div>
             </div>
             <div class="card">
                <h3>Decision Metadata</h3>
                <div>${intent.decision_metadata ? JSON.stringify(intent.decision_metadata) : 'N/A'}</div>
             </div>
        </div>

        <div class="card">
            <h3>State Lifecycle Timeline</h3>
            <div class="timeline">
                ${intent.history.map(step => `
                    <div class="timeline-item">
                        <div class="timeline-dot"></div>
                        <div class="timeline-time">${formatTime(step.timestamp)}</div>
                        <div class="timeline-content">
                            <strong>${step.from} &rarr; ${step.to}</strong>
                            ${step.trigger ? `<br><small class="text-muted">Trigger: ${step.trigger}</small>` : ''}
                            ${step.component ? `<br><small class="text-muted">Component: ${step.component}</small>` : ''}
                        </div>
                    </div>
                `).join('')}
                <!-- Current state as final node -->
                 <div class="timeline-item">
                        <div class="timeline-dot" style="background:var(--primary-color)"></div>
                        <div class="timeline-time">Now</div>
                        <div class="timeline-content">
                             <strong>Current: ${intent.current_state}</strong>
                        </div>
                 </div>
            </div>
        </div>

        ${intent.execution_result ? `
            <div class="card">
                <h3>Execution Result</h3>
                <pre style="background:rgba(0,0,0,0.2); padding:10px; border-radius:4px;">${JSON.stringify(intent.execution_result, null, 2)}</pre>
            </div>
        ` : ''}
    `;
}

function renderCapabilities() {
    const { capabilities } = appState.data;
    return `
        <div class="header">
            <h1 class="page-title">System Capabilities</h1>
        </div>
        <div class="card">
            <table>
                 <thead>
                    <tr>
                         <th>Name</th>
                         <th>Type</th>
                         <th>Description</th>
                         <th>Bindings</th>
                    </tr>
                </thead>
                <tbody>
                     ${capabilities.map(cap => `
                        <tr>
                            <td><strong>${cap.name}</strong></td>
                            <td><span class="badge" style="background:rgba(255,255,255,0.1)">${cap.type}</span></td>
                            <td>${cap.description}</td>
                             <td>${cap.bindings.map(b => `<span style="display:inline-block; background:rgba(63, 135, 245, 0.2); padding:2px 6px; border-radius:4px; margin-right:5px; font-size:0.8em;">${b}</span>`).join('')}</td>
                        </tr>
                     `).join('')}
                </tbody>
            </table>
        </div>
    `;
}

// Init
document.addEventListener('DOMContentLoaded', () => {
    // Attach nav listeners
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const view = e.target.closest('a').dataset.view;
            if (view) navigateTo(view);
        });
    });

    // Initial Render
    render();
});
