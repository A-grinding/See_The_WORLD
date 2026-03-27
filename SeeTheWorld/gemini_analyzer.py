from google import genai
from google.genai import types
import json



def inferDoc(gclient, input, output):
    print(f"Loading tweets")
    
    df = pd.read_csv(input)
    
    tweetsList = df['full text'].head(50).tolist()
    
    prompt = f"""
    Analyze the following list of scraped tweets. 
    1. Identify the 10 most important overall keywords/topics across this specific dataset.
    2. For each of these 10 keywords, identify the sentiment (Positive, Negative, or Neutral).
    
    Return the result EXACTLY as a JSON array of objects with this structure:
    [
      {{"tweet": "exact tweet text", "primary_keyword": "keyword", "sentiment": "Positive/Negative/Neutral"}}
    ]
    
    Here are the tweets:
    {tweetsList}
    """
    
    
    response = gclient.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt,
        config = types.GenerateContentConfig(
            response_mime_type= "application/json",
            temperature=0.2,
        )
    )
    try:    
        data = json.loads(response.text)
        results_df = pd.DataFrame(data)
        
        results_df.to_csv(output, index=False)
        print(f"Success! Analyzed data saved to {output}")
    
    except Exception as e:
        print("Error parsing response as JSON:", e)
        print("Raw response text:", response.text)
        
