grammar g;

root : stat*
    ;

numlist : NUM+
    ;

expr : VAR expr+                                                        #funcioAplicada
    | (OPUNARI|'#') expr                                                #unari
    | expr (OPBINARI|OPBINARI '~'|'#') expr                             #binari
    | numlist                                                           #llista
    | '(' expr ')'                                                      #parentesis
    | VAR                                                               #id
    | OPUNARI                                                           #opunariExpr
    | OPBINARI                                                          #opbinariExpr
    ;

stat : VAR '=:' expr                                                    #assignacio
    | expr                                                              #expressio
    ;

OPUNARI : '_'|']'|'i.'|[+\-*/%|^]':'|[+\-*/%|^]'/';
OPBINARI : '+'|'-'|'*'|'%'|'|'|'^'|'>'|'<'|'>='|'<='|'='|'<>'|','|'@:'|'{';
NUM : [0-9]+;
VAR : [a-zA-Z][a-zA-Z0-9_]*;
WS : [ \t\r\n]+ -> skip ;
COMMENT : 'NB.' ~[\r\n]* -> skip ;