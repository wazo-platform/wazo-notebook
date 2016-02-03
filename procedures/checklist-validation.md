Dès que le validateur considère une étape insuffisante, on retourne la balle aux développeurs en charge des branches

1.  Effectuer le code review
2.  Fusionner (merge) les branches dans master (localement)
3.  Valider la séparation claire et digeste des commits.
4.  Valider la présence du numéro de ticket dans le nom de branche
5.  Valider les tests
    1.  Valider la couverture des tests (unitaires,fonctionnels)
    2.  Passer tests unitaires
    3.  Passer tests automatiques
    4.  Passer tests manuels pertinents

6.  Documentation
    1.  Relire la documentation associée
    2.  Si modification du protocole CTI, vérifier que le changement est documenté

7.  Confirmer que la feature/le bugfix fonctionne
8.  Push sur origin (+ supprimer branche + "git fetch -p")
9.  Rebuild
10. Feedback au(x) développeur(s) de l'incrément fonctionnel
11. Marquer le ticket redmine correspondant comme resolved, valider qu'il est bien sur la roadmap. Si le ticket n'existe pas, le créer.
