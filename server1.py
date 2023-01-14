import asyncio
import os
import websockets
import whisper

PORT=7003
print("Server is connecting"+str(PORT))

async def test(websocket,path):
    print("client connection")
    try:
        file_name = "test.mp3"
        file_size = os.stat(file_name).st_size
    except Exception as e:
       print("Exception ",e)

    with open(file_name,"wb") as file:
       c = 0
       while c <= int(file_size):
         data = file.read(1024)
         if not data:
            break
         file.write(data)
         c += len(data)

    #file_name = await websocket.recv()
    #print("filename is",file_name)
    model = whisper.load_model("small")
    result = model.transcribe(file_name,fp16= False,verbose = False,language="Japanese")
    print(result['text'])
    await websocket.send(result['text'])
    
    #await websocket.send("Return msg from server")
   


#start_server=websockets.serve(test,"localhost",PORT)

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()        

async def main():
    async with websockets.serve(test, "localhost", PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())
#async def main():
    #async with websockets.serve(test, "localhost", PORT):
     #   await asyncio.Future()  # run forever

#asyncio.run(main())



