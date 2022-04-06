# Twitter

J'ai crée un bot qui répond automatiquement aux personnes qui écrivent mal le nom de Shawn Froste,
le fameux personnage d'Inazuma Eleven en l'écrivant Shawn Frost.

J'ai également ajouté le fait que le bot réponde quand il s'agit du frère de Shawn Froste, Aiden Froste

Le bot peut
- répondre automatiqueùent toutes les 5 minutes pour ne pas dépasser la limite de l'API
- répondre quand on l'identifie sous la forme: @shawnfrostebot + nom d'un des deux frères

exemple: @shawnfrostebot aiden --> Je connais aucun Aiden Frost mais par contre Aiden Froste quel masterclass !!

La seule limite du bot sont le fait qu'on fait une recherche uniquement sur les tweets français or Twitter
considère 'Shawn Frost' seul dans un tweet comme un tweet anglais même s'il a été rédigé par un français.

Le fait d'analyser uniquement les tweets français est du à des embrouilles avec la communauté espagnole
