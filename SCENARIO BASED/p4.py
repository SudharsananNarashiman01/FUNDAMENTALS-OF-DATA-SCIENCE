import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load CSV
df = pd.read_csv(r"C:\Users\tthul\Downloads\car_resale(1).csv")

print("Dataset:")
print(df)

# Encode Brand
le = LabelEncoder()
df['Brand'] = le.fit_transform(df['Brand'])

X = df[['Brand', 'Age', 'Kms_Driven', 'Engine_CC']]
y = df['Resale_Price']

model = LinearRegression()
model.fit(X, y)

brand = input("Enter Brand (Maruti/Hyundai/Honda/Toyota/Tata): ")

if brand not in le.classes_:
    print("Brand not found!")
else:
    age = int(input("Enter Age: "))
    kms = int(input("Enter Kilometers Driven: "))
    engine = int(input("Enter Engine CC: "))

    brand = le.transform([brand])[0]

    prediction = model.predict([[brand, age, kms, engine]])

    print("Estimated Resale Price = ₹", prediction[0])