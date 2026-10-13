const items = require('./full_deliverables_manifest.json');

console.log("Total deliverables:", items.length);
items.forEach(it => {
  console.log(`[${it.code}] ${it.folder} -> ${it.filename}`);
  console.log(`     Titulo Trello: ${it.title}`);
  console.log(`     Entregable: ${it.deliverable}`);
});
