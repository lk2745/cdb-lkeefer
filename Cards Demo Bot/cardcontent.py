cardcontent = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.2",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                "type": "Column",
                "width": 2,
                "items": [
                    {
                        "type": "TextBlock",
                        "text": "Sign up for our Newsletter!",
                        "weight": "Bolder",
                        "size": "Medium"
                    },
                    {
                        "type": "TextBlock",
                        "text": "Our Newsletter is Super freaking awesome, and there is no other like it in the universe",
                        "isSubtle": True,
                        "wrap": True
                    },
                    {
                        "type": "TextBlock",
                        "text": "Don't worry. We'll never sell or share your information (unless we can profit from it, hehe).",
                        "isSubtle": True,
                        "wrap": True,
                        "size": "Small"
                    },
                    {
                        "type": "TextBlock",
                        "text": "Your Name",
                        "wrap": True
                    },
                    {
                        "type": "Input.Text",
                        "id": "myName",
                        "placeholder": "First and Last Name"
                    },
                    {
                        "type": "TextBlock",
                        "text": "Your Email",
                        "wrap": True
                    },
                    {
                        "type": "Input.Text",
                        "id": "myEmail",
                        "placeholder": "youremail@example.com",
                        "style": "Email"
                    },
                    {
                        "type": "TextBlock",
                        "text": "Phone Number"
                    },
                    {
                        "type": "Input.Text",
                        "id": "myTel",
                        "placeholder": "000-000-0000",
                        "style": "Tel"
                    }
                ]   
            },
            {
                "type": "Column",
                "width": 1,
                "items": [
                    {
                        "type": "Image",
                        "url": "https://storage.googleapis.com/wx-blg-prd-gcs/wp-content/uploads/1/2019/10/AW25276-e1570465726605.jpg",
                        "size": "auto"
                    }       
                ]
            }
        ]
    }
],
"actions": [
    {
        "type": "Action.Submit",
        "title": "Submit"
    }
    ]
}
