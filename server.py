import asyncio
import websockets
from pydub import AudioSegment
from queue import Queue

PORT=8001
print("Server is connecting "+str(PORT))
rec_queue = Queue()
async def listen1():
       
       print("Connecting in server")
       try: 
            print("/////",)
          
           
        
       except Exception as e:
           print("Connection ended")
           print(e)

async def main():
       async with websockets.serve(listen1, "", 8001):
        await asyncio.Future()  # run forever

asyncio.run(main())