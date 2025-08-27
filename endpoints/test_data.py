payload = {
        "text": "Funny cats",
        "url": "https://kinpet.ru/upload/webp/iblock/5a9/zqfsks555los2ovnmv2vxwyuchdrm7i9/polosatye_koty_fon_jpg.webp",
        "tags": ["cats", "boys", "girls"],
        "info": {"colour": "different", "age": "1-10"}
    }

update_payload = {
        "id": "",
        "text": "Great people",
        "url": "https://www.biografguru.ru/img/4420_cnt_bgr.jpg",
        "tags": ["people", "young", "old"],
        "info": {"nationality": "different", "age": "30-80"}
    }

incorrect_tags = {
        "id": "",
        "text": "Great people",
        "url": "https://www.biografguru.ru/img/4420_cnt_bgr.jpg",
        "tags": "incorrect format",
        "info": {"nationality": "different", "age": "30-80"}
    }

incorrect_text = {
        "id": "",
        "text": 1,
        "url": "https://www.biografguru.ru/img/4420_cnt_bgr.jpg",
        "tags": ["people", "young", "old"],
        "info": {"nationality": "different", "age": "30-80"}
    }

incorrect_url = {
        "id": "",
        "text": "Great people",
        "url": 1,
        "tags": ["people", "young", "old"],
        "info": {"nationality": "different", "age": "30-80"}
    }

incorrect_info = {
        "id": "",
        "text": "Great people",
        "url": "https://www.biografguru.ru/img/4420_cnt_bgr.jpg",
        "tags": ["people", "young", "old"],
        "info": "test"
    }
