from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re
class InputData(BaseModel):
    data: List[str]

app = FastAPI()

class InputData(BaseModel):
    data: List[str]


@app.post("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}
@app.post("/bfhl")
async def process_array(input_data: InputData):
    try:
        # Initialize response fields
        user_id = "pugazh_mukilan_26082004"
        email = "pugazhmukilanoffical2004@gmail.com"
        roll_number = "22BCE9292"
        
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        all_chars = []
        total_sum = 0
        
       
        for item in input_data.data:
            #check for a number
            if re.match(r'^-?\d+$', item): 
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))



            
            elif re.match(r'^[a-zA-Z]+$', item):
                alphabets.append(item.upper())
           

            elif re.match(r'^[^a-zA-Z0-9]$', item):
                special_characters.append(item)
           
            else:
                if any(c.isalpha() for c in item):
                    alphabets.append(item.upper())
                else:
                    special_characters.append(item)
        
        
        for item in input_data.data:
            all_chars.extend([c for c in item if c.isalpha()])
        
       
        concat_string = ""
        for i, char in enumerate(reversed(all_chars)):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
        
        return {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail={
            "is_success": False,
            "error": str(e)
        })