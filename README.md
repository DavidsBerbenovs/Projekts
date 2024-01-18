# Projekts
***WARNING kods nedarbosies github, lai tas darbojas, jums būs nepieciešams VisualStuidoCode***

**Projekts ir uzrakstīts Python programmēšanas valodā un paredzēts teksta tulkošanas procesa automatizācijai starp krievu, latviešu un angļu valodu, izmantojot Google Translate. Programma nodrošina lietotājam ērtu saskarni, ļaujot viņam izvēlēties tulkošanas virzienu un ievadīt tekstu turpmākai automātiskai tulkošanai.Programma arī piedāvā opciju saglabāt tulkojumus Excel failā un nosaukt Excel failā.**

**Python bibliotēkas:**
  **Selenium:**
  **Izmanto, lai automatizētu Chrome tīmekļa pārlūkprogrammu.
    Bibliotēka ļauj programmatiski mijiedarboties ar tīmekļa lapu, ievadīt tekstu un izgūt rezultātus.
    Google tulkotāja tīmekļa lapa ir dinamiska, un Selenium nodrošina līdzekļus, lai ar to manipulētu.**
    
  **Time:**
  **Izmanto, lai starp programmas soļiem ievietotu pauzes.
    Tiek pievienotas nelielas aizkaves, lai nodrošinātu skripta izpildes stabilitāti, ņemot vērā laiku, kas nepieciešams tīmekļa lapas ielādei vai citām darbībām.**

  **Pandas:**
  **Programma izmanto Pandas, lai efektīvi pārvaldītu un saglabātu tulkojumu datus. Pandas DataFrame tiek izmantots, lai organizētu un saglabātu tulkojumus Excel failā.**
  **Programmatūras izmantošanas metodes:**
  
  **Tulkošanas virziena izvēle:
    Lietotājam tiek nodrošināta izvēlne ar tulkošanas valodas virziena izvēles iespējām (krievu-angļu, latviešu-angļu, angļu-krievu, angļu-latviešu,nosaukt Excel un saglabat Excel faila vardus tulkojumu), .
    Ievadot atbilstošo numuru, lietotājs izvēlas vēlamo virzienu.**
    
  **Teksta ievadīšana tulkošanai:
    Pēc virziena izvēles programma liks ievadīt tekstu tulkošanai.
    Lietotājs var ievadīt frāzes, vārdus un pat tekstus.**
    
  **Tulkošanas rezultāta iegūšana:
    Programma izmanto Selēnu, lai mijiedarbotos ar Google tulkotāja tīmekļa lapas elementiem.
    Teksts tiek nosūtīts uz lapu, un tulkojuma rezultāts tiek izgūts un parādīts lietotājam.**
    
  **Tulkojumu saglabāšana Excel failā:**
  **Ja lietotājs vēlas saglabāt savu tulkojumu, viņš var nospiest 5, lai dot nosaukumu Excel Failam. Kad lietotājs nosaucis Excel Failu, viņš varēs saglabāt visu tulkojumu**
   
  **Iziet no programmas:
    Lietotājs var beigt programmu, tulkošanas virziena izvēles izvēlnē ievadot '0' vai ievadot 'x', lai pēc teksta ievadīšanas izietu.**
    
  **Apstrādājot kļūdu:
    Programma nodrošina ievades kļūdu apstrādi, sniedzot kļūdas ziņojumu, ja lietotājs ievada nepareizi.**
    
