grammar g;

root : stat*;

stat : VAR '=:' expr                        #assignacio    
     | expr                                 #expressio      
     ;

expr : numlist                                              #llista       
     | '_' expr                                             #negacio       
     | <assoc=right> expr (OPBINARI|'#') expr  #binari  
     | VAR expr+                                            #callFunc 
     | (OPUNARI|'#') expr                                   #unari        
     | '(' expr ')'                                         #parentesis   
     | VAR                                                  #id            
     | OPUNARI                                              #unariExpr   
     | OPBINARI                                             #binariExpr   
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
VAR : [a-zA-Z][a-zA-Z0-9_]*;               
WS : [ \t\r\n]+ -> skip;                 
COMMENT : 'NB.' ~[\r\n]* -> skip;         