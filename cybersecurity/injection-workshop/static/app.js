// ---------------------------------------------------------
// Application State (initial state)
// ---------------------------------------------------------

const state = {
  activity: 'sql-read',
  secure: false,
  cheatmode: document.body.dataset.cheatmode === 'true'
};

const workspace = document.getElementById('workspace');
const titleEl = document.getElementById('activityTitle');
const subtitleEl = document.getElementById('activitySubtitle');
const vulnerableMode = document.getElementById('vulnerableMode');
const secureMode = document.getElementById('secureMode');

// ---------------------------------------------------------
// Activity Registry
// ---------------------------------------------------------

const activities = {

  'sql-read': {
    title: 'SQL Injection — Read / Reveal',
    subtitle: 'Can a normal customer search reveal records the user was never meant to see?',
    render: renderSqlRead
  },

  'sql-delete': {
    title: 'SQL Injection — Delete / Disrupt',
    subtitle: 'Can an order-cancellation feature be manipulated so that it affects other customers?',
    render: renderSqlDelete
  },

  'sql-modify': {
    title: 'SQL Injection — Modify / Account Takeover',
    subtitle: 'Can a logged-in customer alter another customer’s trusted account information?',
    render: renderSqlModify
  },

  'cmd-discover': {
    title: 'Command Injection — Discover',
    subtitle: 'The vendor search looks ordinary. Can you discover what the server is really doing?',
    render: renderCmdDiscover
  },

  'cmd-read': {
    title: 'Command Injection — Read',
    subtitle: 'Can a vendor-search feature make the server reveal a completely different file?',
    render: renderCmdRead
  },

  'cmd-disrupt': {
    title: 'Command Injection — Disrupt',
    subtitle: 'Can a search function interfere with a shipping process employees rely on?',
    render: renderCmdDisrupt
  },

  'cmd-modify': {
    title: 'Command Injection — Modify',
    subtitle: 'Can a vulnerable label viewer be used to alter a trusted shipping artifact?',
    render: renderCmdModify
  }

};

// ---------------------------------------------------------
// Event Wiring
// ---------------------------------------------------------

document.querySelectorAll('.activity').forEach(btn => btn.addEventListener('click', () => {

  document.querySelectorAll('.activity').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  state.activity = btn.dataset.activity;

  // ---------------------------------------------------------
  // Initial Render
  // ---------------------------------------------------------

  renderCurrent();

}));

// ---------------------------------------------------------
// Button Handlers
// ---------------------------------------------------------

vulnerableMode.addEventListener('click', () => setMode(false));
secureMode.addEventListener('click', () => setMode(true));
document.getElementById('resetButton').addEventListener('click', resetLab);

// ---------------------------------------------------------
// Shared UI / API Helpers
// ---------------------------------------------------------

function setMode(secure) {
  state.secure = secure;
  vulnerableMode.classList.toggle('active', !secure);
  secureMode.classList.toggle('active', secure);
  const badge = document.getElementById('modeBadge');
  badge.textContent = secure ? 'Fixed' : 'Vulnerable';
  badge.classList.toggle('safe', secure);
  renderCurrent();
}

function renderCurrent() {
  const a = activities[state.activity];
  titleEl.textContent = a.title;
  subtitleEl.textContent = a.subtitle;
  clearDebug();
  a.render();
}

async function api(url, body) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  });
  const data = await response.json();
  if (data.debug) updateDebug(data.debug);
  return data;
}

async function getState() {
  const response = await fetch('/api/state');
  return response.json();
}

async function resetLab() {
  const button = document.getElementById('resetButton');
  button.disabled = true;
  button.textContent = 'Restoring…';
  await api('/api/reset', {});
  button.textContent = 'Restored';
  setTimeout(() => { button.textContent = 'Restore Lab'; button.disabled = false; }, 800);
  renderCurrent();
}

function updateDebug(d) {
  document.getElementById('debugInput').textContent = d.input ?? '—';
  let statement = d.statement ?? '—';
  if (d.parameters) statement += `\n\nParameters:\n${JSON.stringify(d.parameters, null, 2)}`;
  document.getElementById('debugStatement').textContent = statement;
  document.getElementById('debugExplanation').textContent = d.explanation ?? '';
}

function clearDebug() {
  updateDebug({input:'—', statement:'—', explanation:'Run an activity to see what happened on the server.'});
}

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function notice(text, type='info') {
  return `<div class="notice ${type}">${escapeHtml(text)}</div>`;
}

function challenge(text, hint='') {
  return `<div class="challenge"><div class="eyebrow">CHALLENGE</div><p>${text}</p>${hint ? `<details><summary>Need a hacking hint?</summary><p>${hint}</p></details>` : ''}</div>`;
}

function renderCustomerTable(rows) {
  if (!rows.length) return `<div class="empty-mini">No matching customer records.</div>`;
  return `<div class="table-wrap"><table><thead><tr><th>ID</th><th>Company</th><th>POC</th><th>Street</th><th>City</th><th>State</th><th>Email</th></tr></thead><tbody>${rows.map(r => `<tr><td>${r.id}</td><td><strong>${escapeHtml(r.company)}</strong></td><td>${escapeHtml(r.contact)}</td><td>${escapeHtml(r.street)}</td><td>${escapeHtml(r.city)}</td><td>${escapeHtml(r.state)}</td><td>${escapeHtml(r.email)}</td></tr>`).join('')}</tbody></table></div>`;
}

// ---------------------------------------------------------
// SQL Injection Activities
// ---------------------------------------------------------

async function renderSqlRead() {
  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">CUSTOMER ACCOUNT DETAILS</div><h2>Display the details for your customer account</h2></div><span class="story-pill">Public-facing lookup</span></div>
    ${challenge('To view your customer account, enter the ID number from your customer invoice.', `The webapp searches for id=1 OR a sneaky hacker might search for other id numbers.`)}
    <div class="form-grid one"><label>Company ID<input id="sqlReadTerm" value="1" autocomplete="off"></label><button id="sqlReadGo" class="primary">Search</button></div>
    <div id="sqlReadMsg"></div><div id="sqlReadResults" class="results-panel"></div>`;

  document.getElementById('sqlReadGo').onclick = async () => {
    const term = document.getElementById('sqlReadTerm').value;
    const data = await api('/api/sql/read', {term, secure: state.secure});
    document.getElementById('sqlReadMsg').innerHTML = data.error ? notice(data.error, 'danger') : '';
    document.getElementById('sqlReadResults').innerHTML = renderCustomerTable(data.rows || []);
  };
}

async function renderSqlDelete() {
  const s = await getState();
  const open = s.orders.filter(o => o.status === 'Open');

  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">ORDER PORTAL</div><h2>Cancel an order</h2><p>Logged in as <strong>Acme Office Supply</strong> (customer 1).</p></div><span class="story-pill">Customer account</span></div>
    ${challenge('To cancel an order, enter the order number and click the cancel button (logged in as <b>Acme Office Supply</b>)', `The latter half of the WHERE clause limits DELETE to the logged in user. What if this latter half was just a programmer's note?`)}
    <div class="metric-row"><div><span>Open orders</span><strong>${s.open_order_count}</strong></div><div><span>Pending revenue</span><strong>$${s.pending_revenue.toLocaleString(undefined,{minimumFractionDigits:2,maximumFractionDigits:2})}</strong></div></div>
    <div class="form-grid one"><label>Order number<input id="sqlDeleteId" value="1042" autocomplete="off"></label><button id="sqlDeleteGo" class="danger-button">Cancel order</button></div>
    <div id="sqlDeleteMsg"></div>
    <div class="table-wrap"><table><thead><tr><th>Order</th><th>Customer</th><th>Item</th><th>Amount</th><th>Stage</th></tr></thead><tbody>${open.map(o => `<tr><td>${o.id}</td><td>${escapeHtml(o.company)}</td><td>${escapeHtml(o.item)}</td><td>$${Number(o.amount).toFixed(2)}</td><td>${escapeHtml(o.fulfillment_stage)}</td></tr>`).join('')}</tbody></table></div>`;

  document.getElementById('sqlDeleteGo').onclick = async () => {
    const order_id = document.getElementById('sqlDeleteId').value;
    const data = await api('/api/sql/delete', {order_id, secure: state.secure});
    document.getElementById('sqlDeleteMsg').innerHTML = data.error ? notice(data.error,'danger') : notice(`${data.affected} order record(s) affected.`, data.affected > 1 ? 'danger' : 'info');
    const after = await getState();
    const openAfter = after.orders.filter(o => o.status === 'Open');
    document.querySelector('.metric-row').innerHTML = `<div><span>Open orders</span><strong>${after.open_order_count}</strong></div><div><span>Pending revenue</span><strong>$${after.pending_revenue.toLocaleString(undefined,{minimumFractionDigits:2,maximumFractionDigits:2})}</strong></div>`;
    document.querySelector('tbody').innerHTML = openAfter.map(o => `<tr><td>${o.id}</td><td>${escapeHtml(o.company)}</td><td>${escapeHtml(o.item)}</td><td>$${Number(o.amount).toFixed(2)}</td><td>${escapeHtml(o.fulfillment_stage)}</td></tr>`).join('');
  };
}

async function renderSqlModify() {
  const s = await getState();
  const acme = s.customers.find(c => c.id === 1);
  const target = s.customers.find(c => c.id === 33923);
  
  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">ACCOUNT PROFILE</div><h2>Update your account</h2><p>Logged in as <strong>Acme Office Supply</strong>.</p></div><span class="story-pill">Authenticated customer</span></div>
    ${challenge('Use the form below to update the contact information for your company (e.g., name, address, or email).', `Your text will be placed inside quotation marks in an UPDATE statement. Can you end the value early and supply a different WHERE clause?`)}
    <div class="profile-grid">
      <div class="profile-card"><div class="eyebrow">YOUR ACCOUNT — #1</div><h3>${escapeHtml(acme.company)}</h3><p><strong>POC:</strong> ${escapeHtml(acme.contact)}</p><p><strong>Email:</strong> ${escapeHtml(acme.email)}</p><p><strong>Address:</strong> ${escapeHtml(acme.address)}</p></div>
      <div class="profile-card target"><div class="eyebrow">TARGET ACCOUNT — #33923</div><h3>${escapeHtml(target.company)}</h3><p><strong>POC:</strong> ${escapeHtml(target.contact)}</p><p><strong>Email:</strong> ${escapeHtml(target.email)}</p><p><strong>Address:</strong> ${escapeHtml(target.address)}</p></div>
    </div>

    <div class="form-grid two">
      <label>Field<select id="sqlModifyField"><option value="contact">Point of contact</option><option value="street">Street address</option><option value="email" selected>Email</option></select></label>
      <label>New value<input id="sqlModifyValue" value="newaddress\@acme.example" autocomplete="off"></label>
      <button id="sqlModifyGo" class="primary">Save changes</button>
    </div>

    <div id="sqlModifyMsg"></div>
    <div class="reset-sim"><div><div class="eyebrow">ACCOUNT RECOVERY SIMULATION</div><h3>Forgot password?</h3><p>Check where a reset for Mountain View Dental would be sent.</p></div><button id="resetSimGo" class="secondary">Send simulated reset</button></div>
    <div id="resetSimResult"></div>`;

  document.getElementById('sqlModifyGo').onclick = async () => {
    const field = document.getElementById('sqlModifyField').value;
    const value = document.getElementById('sqlModifyValue').value;
    const data = await api('/api/sql/modify', {field, value, secure: state.secure});
    document.getElementById('sqlModifyMsg').innerHTML = data.error ? notice(data.error,'danger') : notice(`${data.affected} customer record(s) affected.`, data.affected ? 'info' : 'danger');
    setTimeout(renderSqlModify, 350);
  };

  document.getElementById('resetSimGo').onclick = async () => {
    const data = await api('/api/password-reset', {customer_id: 33923});
    document.getElementById('resetSimResult').innerHTML = `<div class="notice warning"><strong>${escapeHtml(data.company)}</strong><br>Password reset message sent to: <strong>${escapeHtml(data.destination)}</strong></div>`;
  };
}

// ---------------------------------------------------------
// Command Injection Activities
// ---------------------------------------------------------

function vendorShellWorkspace(kind) {
  const configs = {
    discover: {heading:'Vendor Lookup', challenge:'Search our website for a list of approved vendors.', hint:"In many shell commands, a semicolon separates two commands. Two harmless, helpful commands are 'whoami' and 'pwd'.", value:'Acme'},
    read: {heading:'Vendor Lookup', challenge:'The same search page as last time. This time, use injection to display a file the page was never designed to show.', hint:"An important file is in the 'data' directory; use the shell commands 'ls' to find it and 'cat' to display it.", value:'Acme'},
  };

  const c = configs[kind];
  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">LEGACY VENDOR TOOL</div><h2>${c.heading}</h2></div><span class="story-pill">Command-line backend</span></div>
    ${challenge(c.challenge,c.hint)}
    <div class="form-grid one"><label>Vendor name<input id="cmdVendorTerm" value="${c.value}" autocomplete="off"></label><button id="cmdVendorGo" class="primary">Search</button></div>
    <div id="cmdVendorMsg"></div><pre id="cmdVendorOutput" class="output-pre">Search results will appear here.</pre>`;

  document.getElementById('cmdVendorGo').onclick = async () => {
    const term = document.getElementById('cmdVendorTerm').value;
    const data = await api('/api/cmd/vendor', {term, secure: state.secure});
    document.getElementById('cmdVendorMsg').innerHTML = data.error ? notice(data.error,'danger') : '';
    document.getElementById('cmdVendorOutput').textContent = (data.output || []).join('\n') || '(no output)';
  };
}

function renderCmdDiscover(){ vendorShellWorkspace('discover'); }

function renderCmdRead(){ vendorShellWorkspace('read'); }

async function renderCmdDisrupt() {
  const s = await getState();

  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">FULFILLMENT</div><h2>Search today’s shipping queue</h2></div><span class="story-pill">Employee operations</span></div>
    ${challenge('Imagine this is a web interface that lets customers view their saved orders.', `This command can be exploited to view all orders using a wildcard.<br>There's also a powerful script to disrupt shipping in the 'workshop' directory.`)}
    <div class="metric-row"><div><span>Queue status</span><strong id="queueCount">${s.shipping_queue.split('\n').filter(x => x.startsWith('Order ')).length} shipments</strong></div></div>
    <div class="form-grid one"><label>Customer / order search<input id="cmdQueueTerm" value="Acme" autocomplete="off"></label><button id="cmdQueueGo" class="primary">Search queue</button></div>
    <div id="cmdQueueMsg"></div>
    <div class="split-panel"><div><h3>Search output</h3><pre id="cmdQueueOutput" class="output-pre">—</pre></div><div><h3>Current shipping queue</h3><pre id="queueState" class="output-pre">${escapeHtml(s.shipping_queue)}</pre></div></div>`;

  document.getElementById('cmdQueueGo').onclick = async () => {
    const term = document.getElementById('cmdQueueTerm').value;
    const data = await api('/api/cmd/queue-search', {term, secure: state.secure});
    document.getElementById('cmdQueueMsg').innerHTML = data.error ? notice(data.error,'danger') : '';
    document.getElementById('cmdQueueOutput').textContent = (data.output || []).join('\n') || '(no output)';
    const after = await getState();
    document.getElementById('queueState').textContent = after.shipping_queue;
    document.getElementById('queueCount').textContent = `${after.shipping_queue.split('\n').filter(x => x.startsWith('Order ')).length} shipments`;
  };
}

async function renderCmdModify() {
  workspace.innerHTML = `
    <div class="workspace-head"><div><div class="eyebrow">SHIPPING LABELS</div><h2>Preview a generated label</h2></div><span class="story-pill">Warehouse output</span></div>
    ${challenge('Verify the shipping details for your order.', `There is a backend helper script in the 'workshop' directory that generates shipping labels; it expects an order number.<br># Hackers might need to string together several tricks to make this one work.`)}
    <div class="form-grid one"><label>Label filename<input id="cmdLabelName" value="1057" autocomplete="off"></label><button id="cmdLabelGo" class="primary">Preview label</button></div>
    <div id="cmdLabelMsg"></div>
    <div class="label-preview"><pre id="cmdLabelOutput">Choose Preview label.</pre></div>`;

  document.getElementById('cmdLabelGo').onclick = async () => {
    const label_name = document.getElementById('cmdLabelName').value;
    const data = await api('/api/cmd/label', {label_name, secure: state.secure});
    document.getElementById('cmdLabelMsg').innerHTML = data.error ? notice(data.error,'danger') : '';
    document.getElementById('cmdLabelOutput').textContent = data.label || '(no label)';
  };
}

renderCurrent();
