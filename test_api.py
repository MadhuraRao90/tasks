from flask import Flask,request,jsonify
import mysql.connector as conn
import pymongo
app=Flask(__name__)


@app.route('/test1')
def test():
    get_name=request.args.get("get_name")
    mobile_num=request.args.get("mob_num")
    email_id=request.args.get("email")
    return "this is my first function to get name= {}, mobile number {}, and email id {}".format(get_name,mobile_num,email_id)

@app.route('/dbtask',methods=['GET'])
def dbtsk():
    try:
        db=request.args.get("db")
        table=request.args.get("table")
        mydb=conn.connect(host='localhost',user='root',password='Pradhyun@14042022',database=db)
        cursor=mydb.cursor()
        s=f'select * from {table} where name="new_madhu"'
        cursor.execute(s)
        data=cursor.fetchall()
        print("ghhggh",type(data))
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

@app.route('/mongo')
def mongo():
    client=pymongo.MongoClient("mongodb+srv://madhura:Maddy2809@cluster0.jx1ws.mongodb.net/?retryWrites=true&w=majority")
    db=request.args.get("db")
    collect=request.args.get("collection")
    #name=request.args.get("item")
    try:
        database=client[db]
        collection=database[collect]
        data=collection.find({"item":"umbrella"})
    except Exception as e:
        return jsonify(e)
    return jsonify(data)
if __name__=='__main__':
    app.run(port=5002)