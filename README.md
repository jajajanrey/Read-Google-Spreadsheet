# CREATE A FILE IN GOOGLE DRIVE

A [Supercode](http://gosupercode.com) function that reads google spreadsheet

## Sample Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

```
import json
import pprint
import supercode

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    sheet_id="SHEET_ID_HERE",
    range_notation_list="",
    service_account_json={SERVICE_ACCOUNT_JSON}
)

    
pprint(response)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.