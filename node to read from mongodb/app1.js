const { MongoClient } = require('mongodb');

// MongoDB connection URL
const url = 'mongodb://localhost:27017';

// Database and collection names
const dbName = 'Ammulu';
const collectionName = 'cll';

// Connect to MongoDB
MongoClient.connect(url, (err, client) => {
  if (err) {
    console.error('Error connecting to MongoDB:', err);
    return;
  }

  console.log('Connected to MongoDB');

  const db = client.db("Ammulu");
  const collection = db.collection("cll");

  // Find all documents in the collection
  collection.find({}).toArray((err, documents) => {
    if (err) {
      console.error('Error retrieving documents:', err);
    } else {
      console.log('Retrieved documents:');
      console.log(documents);
    }

    // Close the MongoDB connection
    client.close();
  });
});