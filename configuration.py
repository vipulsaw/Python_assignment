import configparser
import json
from flask import Flask, jsonify
from pymongo import MongoClient

CONFIG_FILE = "config.txt"
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "configdb"
COLLECTION_NAME = "configurations"

app = Flask(__name__)

def parse_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        data = {section: dict(config.items(section)) for section in config.sections()}
        return data
    except Exception as e:
        print(f"❌ Error reading configuration file: {e}")
        return {}

def save_to_mongodb(data):
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        collection.insert_one({"config_data": data})
        client.close()
        print("✅ Configuration data saved to MongoDB successfully!")
    except Exception as e:
        print(f"❌ Error saving data to MongoDB: {e}")

@app.route('/getconfig', methods=['GET'])
def get_config():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        result = collection.find_one(sort=[("_id", -1)])
        client.close()
        if result:
            return jsonify(result["config_data"])
        else:
            return jsonify({"message": "No configuration data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    config_data = parse_config(CONFIG_FILE)
    if config_data:
        print("📄 Configuration File Parser Results:")
        for section, values in config_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
        save_to_mongodb(config_data)
    
    print("🚀 Starting API server on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
