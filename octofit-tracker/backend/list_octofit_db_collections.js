# List collections and show sample documents from each in octofit_db
use('octofit_db');
print('Collections:');
printjson(db.getCollectionNames());

const collections = db.getCollectionNames();
collections.forEach(function(coll) {
    print('Sample from ' + coll + ':');
    printjson(db.getCollection(coll).findOne());
});
