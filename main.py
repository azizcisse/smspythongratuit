from tkinter import * 
from tkinter import messagebox 
import vonage



class Api_sms:
    def __init__(self, root):
        self.root = root
        self.root.title("API-SMS")
        self.root.geometry("700x500")
        self.root.config(bg="cyan")
        
         
        self.var_numero = StringVar()
        lbl_numero = Label(self.root, text="Numéro Téléphone :", font=("times new roman", 20, "bold"), bg="cyan").place(x=0, y=10)
        txt_numero = Entry(self.root,textvariable=self.var_numero, font=("times new roman", 16, "bold"), bd=7).place(x=250, y=10)

        lbl_sms = Label(self.root, text="Message :", font=("times new roman", 20, "bold"), bg="cyan").place(x=60, y=70)
        self.message = Text( self.root, bd=7)
        self.message.place(x=250, y=70, width=350, height=200)
        
        btn_envoyer =  Button(self.root, cursor="hand2", command=self.envoyer, text="Enoyer", width=16, bd=7, bg="green", fg="white", font=("times new roman", 14, "bold")).place(x=400, y=300)
        
        
    def envoyer(self):
        #Initialiser la bibliothèque
        client = vonage.Client(key="b07492bb", secret="y7AoVXKJqqIWMv3E")
        sms = vonage.Sms(client)
        
        #Écrivez le code
        responseData = sms.send_message(
            {
                "from": "AZIZ-CISSE",
                "to": self.var_numero.get(),
                "text": self.message.get("1.0", END),
            }
        )

        if responseData["messages"][0]["status"] == "0":
            messagebox.showinfo("Envoyer", "Message envoyé avec succès.")
        else:
            messagebox.showerror("Erreur",f"Le message a échoué avec l'erreur : {responseData['messages'][0]['error-text']}")







if __name__=="__main__":
    root=Tk()
    obj = Api_sms(root)
    root.mainloop()
        