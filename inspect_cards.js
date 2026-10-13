const tasks = require('./trello_tasks_utf8.json');
const cards = tasks.filter(t => !t.isSummary);
console.log('Total non-summary cards in Trello:', cards.length);

const byPhase = {};
cards.forEach(c => {
  if (!byPhase[c.phase]) byPhase[c.phase] = [];
  byPhase[c.phase].push(c);
});

for (const phase in byPhase) {
  console.log(`\n=== ${phase.toUpperCase()} (${byPhase[phase].length} cards) ===`);
  byPhase[phase].forEach(c => {
    console.log(`  ${c.code} | ${c.dates} (${c.durationHours}h) | [${c.assignee}] ${c.title}`);
    console.log(`       Deliverable: ${c.deliverable}`);
    console.log(`       IsMilestone: ${c.isMilestone} | %Done: ${c.percentDone}%`);
  });
}
