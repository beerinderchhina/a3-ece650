

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main()
{
  /* use adjacent matrix to store the undirected graph */


  int src, des; /* the vertices to calculate shortest path */
  char command[2];

  /* read the first character as the command.
   * until EOF */
  while (scanf("%s", command) == 1) {
    char c = command[0];
    switch (c) {

      case 'S':
      case 's':
	  break;
      default:
        break;
    }
  }
  
return 0;
}





