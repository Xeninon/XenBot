import random as rand

def handle_bingus(content, user):
    command = content[8:]
    if command.startswith('ask'):
        responses = ("yes", "no", "maybe so", "erm...")
        return f'Bingus says "{rand.choice(responses)}"'
    
    pics = [
        "https://i.imgur.com/sdb25ls.jpeg",
        "https://i.imgur.com/QBcgqZZ.jpeg",
        "https://i.imgur.com/hEDwtut.jpeg",
        "https://i.imgur.com/trr6izC.jpeg",
        "https://i.imgur.com/dA7KueC.jpeg",
        "https://i.imgur.com/EyWQGDN.jpeg",
        "https://i.imgur.com/YgE9pvW.jpeg",
        "https://i.imgur.com/XGpi4UB.jpeg",
        "https://i.imgur.com/BoOD8qW.jpeg",
        "https://i.imgur.com/GHI3a0j.jpeg",
        "https://i.imgur.com/LLjkYYT.jpeg",
        "https://i.imgur.com/31HoAwq.jpeg",
        "https://i.imgur.com/tRz1V57.jpeg",
        "https://i.imgur.com/IqyKL7D.jpeg",
        "https://i.imgur.com/8ElLq7v.jpeg",
        "https://i.imgur.com/QXIcqfZ.jpeg",
        "https://i.imgur.com/HkDlRcV.jpeg",
        "https://i.imgur.com/9hPk1za.jpeg",
        "https://i.imgur.com/G6c6iaR.jpeg",
        "https://i.imgur.com/SnvCKF0.jpeg",
        "https://i.imgur.com/KDvKELC.jpeg",
        "https://i.imgur.com/qFrqDWZ.jpeg",
        "https://i.imgur.com/EAY5yuA.jpeg",
        "https://i.imgur.com/YoHoivG.jpeg",
        "https://i.imgur.com/b4Zt2uW.jpeg",
        "https://i.imgur.com/4JMYXSj.jpeg",
        "https://i.imgur.com/DEQGqFC.jpeg",
        "https://i.imgur.com/I6DlkEj.jpeg",
        "https://i.imgur.com/3O8nNaU.jpeg",
        "https://i.imgur.com/8peLtRI.jpeg",
        "https://i.imgur.com/vQC0yKt.jpeg",
        "https://i.imgur.com/B4kS7PF.jpeg",
        "https://i.imgur.com/pYgUE60.jpeg",
        "https://i.imgur.com/V32Hh96.jpeg",
        "https://i.imgur.com/aLofZxA.jpeg",
        "https://i.imgur.com/oA08bY2.jpeg",
        "https://i.imgur.com/gI2KrbA.jpeg"
        ]
    return f"[bingus]({rand.choice(pics)})"
