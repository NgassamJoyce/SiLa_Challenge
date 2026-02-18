class compte_bancaire:
    def __init__(self, id_compte, nom ,  solde,):
        
        self.id_compte = id_compte
        
        self.nom = nom
        
        self.solde = solde


    def deposer(self, montant):
        
        if montant >= 0:
            
            self.solde += montant
            
            print(f"Dépôt de {montant} effectué. Nouveau solde: {self.solde}")
        
        else:
            print("le montant doit etre positif.")
            
    
    def retirer(self, montant):
        if montant <= 0:
            
            print("le montant de retrait doit etre positif.")
            
        elif montant > self.solde:
            print("votre solde est insuffisant.")   
            
        else:
            self.solde -=montant
            print(f"retrait de {montant} effectuer. Nouveau solde : {self.solde}")     
            
            
    def Verifier_solde(self):
        print(f"cher {self.nom} votre solde est : {self.solde}")        
            
            
