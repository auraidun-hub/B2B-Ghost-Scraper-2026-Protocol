function generateGhostLeads() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // High-value 2026 Tech Leads (The "Seed" Data)
  var leads = [
    ["Quantum Leap AI", "Sarah Jenkins", "s.jenkins@qleap.ai", "linkedin.com/in/sjenkins2026", "2026-04-24"],
    ["CyberFlow Systems", "Marcus Vane", "m.vane@cyberflow.io", "linkedin.com/in/marcusvane", "2026-04-24"],
    ["SynthData Corp", "Amara Okafor", "a.okafor@synthdata.net", "linkedin.com/in/aokafor", "2026-04-24"],
    ["Titan Robotics", "Leo Sterling", "l.sterling@titanrobot.com", "linkedin.com/in/lsterling", "2026-04-24"],
    ["BioLink Solutions", "Chloe Dupont", "c.dupont@biolink.tech", "linkedin.com/in/cdupont", "2026-04-24"]
  ];
  
  // Find the last row and add the new data
  var lastRow = sheet.getLastRow();
  sheet.getRange(lastRow + 1, 1, leads.length, 5).setValues(leads);
  
  SpreadsheetApp.getUi().alert("✅ SYSTEM NOTIFICATION: 5 New High-Value Leads Injected into Stream.");
}

function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('⚡ GHOST-PROTOCOL')
      .addItem('Inject New Leads', 'generateGhostLeads')
      .addToUi();
}
