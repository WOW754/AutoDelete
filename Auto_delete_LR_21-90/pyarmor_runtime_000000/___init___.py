import base64
xx = b'''
aW1wb3J0IGRpc2NvcmQNCmltcG9ydCBhc3luY2lvDQpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZSwgdGltZWRlbHRhLCB0aW1lem9uZQ0KZnJvbSBkaXNjb3JkLmV4dCBpbXBvcnQgY29tbWFuZHMsIHRhc2tzDQoNCiMgQm90IGNvbmZpZ3VyYXRpb24NClRPS0VOID0gIk1UTTBNelV4TlRFMU5UazFORFF3TlRRMk9BLkdlaDBrdi5WY0Ztd3ZPVk1XUVZXNWNmRWR1SUZGb0U1QjZ5MjlTdGtMZUhQUSINCg0KR1VJTERfSUQgPSAxMzM5OTkzMTUzNTM2NTI4NDA3DQpDSEFOTkVMX0lEUyA9IFsxMzQwMDA0OTI0MjgwNDEwMjYyLCAxMzQwMDA0OTYzNzUzMDAwOTcwLCAxMzQwMDA1MDI5MDI0NjI4OTQ3LCAxMzQwMDA1MjI5MDcyMjIwMjEyLCAxMzQwMDA1MjcyODU2NDMyNzEwXQ0KTE9HX0NIQU5ORUxfSUQgPSAxMzQxMDc4NjY2NDU2NzI3NTkyIA0KDQpDSEVDS19JTlRFUlZBTCA9IDEyMCAgIyBDaGVjayBldmVyeSAxMjAgc2Vjb25kcw0KTUFYX1JVTlRJTUUgPSAxMCAqIDYwICAjIFN0b3AgYWZ0ZXIgNiBob3Vycw0KREVMRVRFX1RIUkVTSE9MRCA9IHRpbWVkZWx0YShob3Vycz03MikgICMgRGVsZXRlIG1lc3NhZ2VzIG9sZGVyIHRoYW4gNzIgaG91cnMNCg0KDQojIFNldCB1cCBib3Qgd2l0aCBpbnRlbnRzDQppbnRlbnRzID0gZGlzY29yZC5JbnRlbnRzLmRlZmF1bHQoKQ0KaW50ZW50cy5tZXNzYWdlcyA9IFRydWUNCmludGVudHMuZ3VpbGRzID0gVHJ1ZQ0KYm90ID0gY29tbWFuZHMuQm90KGNvbW1hbmRfcHJlZml4PSIhIiwgaW50ZW50cz1pbnRlbnRzKQ0KDQpAYm90LmV2ZW50DQphc3luYyBkZWYgb25fcmVhZHkoKToNCiAgICBwcmludChmIkxvZ2dlZCBpbiBhcyB7Ym90LnVzZXJ9IikNCiAgICBkZWxldGVfb2xkX21lc3NhZ2VzLnN0YXJ0KCkNCiAgICANCiAgICAjIFN0b3AgYm90IGFmdGVyIDEyIGhvdXJzDQogICAgYXdhaXQgYXN5bmNpby5zbGVlcChNQVhfUlVOVElNRSkNCiAgICBkZWxldGVfb2xkX21lc3NhZ2VzLmNhbmNlbCgpDQogICAgYXdhaXQgYm90LmNsb3NlKCkNCg0KQHRhc2tzLmxvb3Aoc2Vjb25kcz1DSEVDS19JTlRFUlZBTCkNCmFzeW5jIGRlZiBkZWxldGVfb2xkX21lc3NhZ2VzKCk6DQogICAgbm93ID0gZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykgICMgVXNlIHRpbWV6b25lLWF3YXJlIGRhdGV0aW1lDQogICAgbG9nX2NoYW5uZWwgPSBib3QuZ2V0X2NoYW5uZWwoTE9HX0NIQU5ORUxfSUQpDQogICAgDQogICAgaWYgbm90IGxvZ19jaGFubmVsOg0KICAgICAgICBwcmludChmIkxvZyBjaGFubmVsIHtMT0dfQ0hBTk5FTF9JRH0gbm90IGZvdW5kISIpDQogICAgICAgIHJldHVybg0KICAgIA0KICAgIGZvciBjaGFubmVsX2lkIGluIENIQU5ORUxfSURTOg0KICAgICAgICBjaGFubmVsID0gYm90LmdldF9jaGFubmVsKGNoYW5uZWxfaWQpDQogICAgICAgIGlmIG5vdCBjaGFubmVsOg0KICAgICAgICAgICAgcHJpbnQoZiJDaGFubmVsIHtjaGFubmVsX2lkfSBub3QgZm91bmQhIikNCiAgICAgICAgICAgIGNvbnRpbnVlDQoNCiAgICAgICAgZGVsZXRlZF9jb3VudCA9IDANCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgYXN5bmMgZm9yIG1lc3NhZ2UgaW4gY2hhbm5lbC5oaXN0b3J5KGxpbWl0PTEwMCk6DQogICAgICAgICAgICAgICAgaWYgKG5vdyAtIG1lc3NhZ2UuY3JlYXRlZF9hdCkgPiBERUxFVEVfVEhSRVNIT0xEOg0KICAgICAgICAgICAgICAgICAgICBhd2FpdCBtZXNzYWdlLmRlbGV0ZSgpDQogICAgICAgICAgICAgICAgICAgIGRlbGV0ZWRfY291bnQgKz0gMQ0KICAgICAgICAgICAgICAgICAgICBwcmludChmIkRlbGV0ZWQgbWVzc2FnZSBmcm9tIHttZXNzYWdlLmF1dGhvcn0gaW4ge2NoYW5uZWwubmFtZX0iKQ0KICAgICAgICAgICAgDQogICAgICAgICAgICBpZiBkZWxldGVkX2NvdW50ID4gMDoNCiAgICAgICAgICAgICAgICBhd2FpdCBsb2dfY2hhbm5lbC5zZW5kKGYi4pyFIERlbGV0ZWQgKip7ZGVsZXRlZF9jb3VudH0qKiBtZXNzYWdlcyBpbiA8I3tjaGFubmVsX2lkfT4uIikNCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgcHJpbnQoZiJFcnJvciBpbiB7Y2hhbm5lbF9pZH06IHtlfSIpDQoNCmJvdC5ydW4oVE9LRU4p
'''
exec(base64.b64decode(xx))
