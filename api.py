from fastapi import FastAPI, File, UploadFile
import gridfs
import Database
import shutil

app = FastAPI()
database = Database.get_database()['Photos']
fs = gridfs.GridFS(database)

@app.get('/')
def root():
    return {'Hello': 'world'}
@app.post("/post_photo/")
async def post_photo(file: UploadFile = File(...)):

    contents = await file.read()
    fs.put(contents, filename=file.filename)
    return {'Result': 'File uploaded successfully'}

@app.get("/get_photo/{photo_name}")
async def get_photo(photo_name: str):
    query = fs.find({'filename': f'{photo_name}'}).limit(1)
    content = next(query, None)
    if content:
        id = content._id
        file = fs.get(id)
        with open(photo_name, 'wb') as savedPhoto:
            shutil.copyfileobj(file, savedPhoto)
        return {'Result': 'File downloaded successfully'}
    else:
        return {'Result': 'File not found'}

