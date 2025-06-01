grammar g;

root : stat*;

stat : expr                                                 #expressio    
     | ID '=:' expr                                         #assignacio 
     | ID '=:' funcDefinition                               #funcDef 
     ;

expr : '(' expr ')'                                         #parentesis   
     | '_' expr                                             #negacio     
     | <assoc=right> expr (OPBINARI|'#') expr               #binari  
     | (OPUNARI|'#') expr                                   #unari       
     | ID expr+                                             #function    
     | ID                                                   #id
     | numlist                                              #llista      
     ;


funcDefinition : (NUM | ID | OPBINARI | OPUNARI)+     
     ;

numlist : NUM+;

OPUNARI : '_'                               
        | ']'                               
        | 'i.'                             
        | [+\-*/%|^]':'                    
        | [+\-*/%|^]'/'                     
        ;

OPBINARI : '+'                              
         | '-'                              
         | '*'                              
         | '%'                              
         | '|'                             
         | '^'                              
         | '>'|'<'|'>='|'<='|'='|'<>'        
         | ','                              
         | '@:'                            
         | '{'                             
         | '+~' | '-~' | '*~' | '%~'       
         | '|~' | '^~' | '>~' | '<~'       
         | '>=~' | '<=~' | '=~' | '<>~'    
         | ',~' | '@:~' | '{~'                
         ;

NUM : [0-9]+ | '_' [0-9]+;                
ID : [a-zA-Z][a-zA-Z0-9_]*;    
WS : [ \t\r\n]+ -> skip;                 
COMMENT : 'NB.' ~[\r\n]* -> skip;         