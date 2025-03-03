Assignment ML(22IT052)
Step 1: Fork the file
Step 2: Update your code in personal-api.py file
![Screenshot 2025-03-03 202559](https://github.com/user-attachments/assets/f50d3597-17a0-4dcc-a8b8-f13eea0b2705)

Step 3: Run the command python personal-api.py and check the details
![Screenshot 2025-03-03 202715](https://github.com/user-attachments/assets/1f40f1d1-09af-4099-9a88-1e3491fc1a06)
![Screenshot 2025-03-03 202733](https://github.com/user-attachments/assets/9099c5e2-a2bb-4c30-8782-2ccf5abccb39)
![Screenshot 2025-03-03 202757](https://github.com/user-attachments/assets/f53ebe7f-2b5c-43d0-bdef-f4fadedd3aab)

Step 4: Run --> docker build -t personal-api .
![Screenshot 2025-03-03 192851](https://github.com/user-attachments/assets/153291f8-ff80-4e96-bd4b-a1def3e393f4)

Step 5:  Run --> docker run -d -p 5000:5000 personal-api
![image](https://github.com/user-attachments/assets/789dff75-3352-481a-8ec6-28a1fa80b837)

Step 6: Run --> docker ps and docker images
![image](https://github.com/user-attachments/assets/9f828eda-ce2c-43dd-b594-b9e7023a710c)
![Screenshot 2025-03-03 194614](https://github.com/user-attachments/assets/931d6b53-0200-4c05-a0e7-42b9ea96ea52)

Step 7: Update compose.yml file
![image](https://github.com/user-attachments/assets/1f04fc23-8472-45c6-867f-71bb13cfbbce)

Step 8: Run --> docker compose up and docker compose up -d
![Screenshot 2025-03-03 214113](https://github.com/user-attachments/assets/a3ad0460-1690-442a-9b3f-a08c5e744208)
![Screenshot 2025-03-03 214537](https://github.com/user-attachments/assets/a8e24ab9-10b8-4f72-8679-f81177cc480a)
![image](https://github.com/user-attachments/assets/7cd33c21-1e98-4ab7-8f6e-29f3cd7342d1)

Step 9: Test the output for me and friend
Varuna:
![Screenshot 2025-03-03 214211](https://github.com/user-attachments/assets/fc588d26-3a6d-4aa4-90d5-977bcccfdcfd)
![Screenshot 2025-03-03 214334](https://github.com/user-attachments/assets/e442dcbf-ed46-4877-82b8-39d98e9d02d2)
![Screenshot 2025-03-03 214633](https://github.com/user-attachments/assets/0423d5f7-4728-48d8-b22d-04b168feaa90)

Friend:
![Screenshot 2025-03-03 214227](https://github.com/user-attachments/assets/50c82e5f-71df-4bfa-8aa7-abbeb7ec358a)
![Screenshot 2025-03-03 214359](https://github.com/user-attachments/assets/32489b19-572f-4438-8a97-f2184a3c37ce)
![Screenshot 2025-03-03 214612](https://github.com/user-attachments/assets/b0f715e0-b9fd-47f8-9d68-29c0f060167b)
![Screenshot 2025-03-03 214537](https://github.com/user-attachments/assets/47aa0abd-bb32-4a77-8967-8de06bc4a43f)

Step 10: Run the ml model
Run --> docker build -t varunapriyas/22it052-ml-model:latest .
![Screenshot 2025-03-03 221211](https://github.com/user-attachments/assets/6042064c-3a10-434e-bece-616b1e03bee8)

Run --> docker push varunapriyas/22it052-ml-model:latest
![Screenshot 2025-03-03 224043](https://github.com/user-attachments/assets/73c750e8-1cdb-413c-a3fd-dc1f94bdef18)

Run -->MAIN command:
docker run varunapriyas/22it052-ml-model:latest
![Screenshot 2025-03-03 224059](https://github.com/user-attachments/assets/cf4c0d5b-98eb-4343-bf21-b03ed4024316)
![image](https://github.com/user-attachments/assets/81b1da31-1501-4dd9-b1b7-c0ee15ebd7cc)
Images:
![image](https://github.com/user-attachments/assets/eae03cf8-de30-4739-b383-73844975cebb)

Login to DOCKER HUB
USERname:varunapriyas
![Screenshot 2025-03-03 224125](https://github.com/user-attachments/assets/3d27fb3b-6292-4d43-b909-148c40fb83c7)

