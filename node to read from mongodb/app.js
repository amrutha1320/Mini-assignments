const {MongoClient}= require('mongodb');
const url='mongodb://127.0.0.1:27017'
const client=new MongoClient(url);
const dbName='Ammulu';
async function main(){
    await client.connect();
    console.log("server connected");
    const db=client.db(dbName);
    const collection=db.collection('cll');
    const result=await collection.find({}).toArray();                                         
    console.log(result);
    return 'done';
}
main()
  .then(console.log)
  .catch(console.error)
  .finally(()=>client.close())