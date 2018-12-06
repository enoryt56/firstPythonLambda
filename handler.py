import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.2! Your function executed successfully!"
    }
    head = {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials" : True
    }
    response = {
        "statusCode": 200,
        "headers" : head,
        "body": json.dumps(body)
    }
    return response
def goodbye(event, context):
    input = event["body"]
    output = "Testing"
    if input == "l33t":
        output = "https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/thumb/f/f2/SeasonalRankTop0.png/180px-SeasonalRankTop0.png?version=3ea336672491d767083386822e25e997" 
    else:
        output = "https://c-7npsfqifvt0x24e2v6q4m5x78qbz4lx2edmpvegspoux2eofu.g00.gamepedia.com/g00/3_c-7epub3.hbnfqfejb.dpn_/c-7NPSFQIFVT0x24iuuqtx3ax2fx2fe2v6q4m5x78qbz4l.dmpvegspou.ofux2fepub3_hbnfqfejbx2f9x2f96x2fTfbtpobmSbol2-2.qohx3fwfstjpox3d1245259bb2b4dfbc4cb695eb32g338cc_$/$/$/$/$?i10c.ua=1&i10c.dv=19"

    body = {
        "message": "Go Serverless v1.2! Your function executed successfully returned something given an input!","input": input,"output":output  
    }
    head = {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials" : True
    }
    response = {
        "statusCode": 200,
        "headers" : head,
        "body": json.dumps(body)
    }
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
