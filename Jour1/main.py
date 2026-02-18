from compte_bancaire import compte_bancaire

def main():
    print("=== CREATION D`UN COMPTE BANCAIRE ===")
    
    id_compte = int(input("Entrez l`id du compte : "))
    
    nom = input("Entrez le nom de votre compte : ")
    
    solde_init = float(input("Entrez le solde initial  : "))
    
    compte = compte_bancaire(id_compte, nom , solde_init)
    
    while True:
        print("\n=== MENU ===")
        print("1 - Deposer l`argent")
        print("2 - Retirer  l`argent")
        print("3 - Verifier mon solde")
        print("4 - Quitter")
        
        choix = input("votre choix : ")
        
        if choix == "1":
            montant = float(input("le mpontant deposer est : "))
            compte.deposer(montant)
             
        elif choix == "2":
              montant = float(input("le montant retirer est : "))
              compte.retirer(montant) 
                
        elif choix == "3":
             compte.Verifier_solde()
        
        elif choix == "4":
             print("merci!")     
             
        else:
            print("choix invalide.")   
            
if __name__ =="__main__":
    main()                     
                