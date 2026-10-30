




ghad = float(input("ghad khod ra be metr vared konid : "))
vazn = float(input("vazn khod ra be kilogeram vared konid : "))

BMI = vazn/(ghad**2)

if BMI < 18.5:
    print("shoma kambod vazn darid.")

elif 18.5<= BMI <25:
    print("BMI shoma monaseb ast.")

elif 25 <= BMI <= 30:
    print("shoma ezafe vazn darid.")

elif 30 < BMI:
    print("shoma chagh hastid.")