const fs = require('fs');
const tasks = require('./trello_tasks_utf8.json');

const relevantCards = tasks.filter(t => !t.isSummary && (
  ['fase1', 'fase2', 'fase3'].includes(t.phase) ||
  ['4.1', '4.2', '4.3'].includes(t.code)
));

console.log(`Extracted ${relevantCards.length} cards matching schedule up to 13-oct-2026.`);

fs.writeFileSync('Entregables_Latex/cards_manifest.json', JSON.stringify(relevantCards, null, 2), 'utf8');
