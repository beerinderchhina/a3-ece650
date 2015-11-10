#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<string.h>

void Timer(int delayInSeconds)
{
    int defaultDelay = 5;
    if(delayInSeconds == 0)
        delayInSeconds = defaultDelay;
    int retTime = time(0) + delayInSeconds;
    while (time(0) < retTime); 
    printf("Delay of %i seconds.\n", delayInSeconds);
}

int GenerateRandom(int number)
{
    return (rand()%(number));
}

int Cordinates(int range)
{ 
    int defaultRange = 20;
    if(range == 0)
        range = defaultRange;
    int r = rand()%(range)-(range);
    return r;
}

int main(void)
{
    
    
    int streetCount;
    int vectorCount;
    int delayTime;
    int cordinatesRange;
    char *nextValue;
    
    char * strtok (char *src, const char *delimiters);
    char str1[] ="-s 5 -l 4";
    char *pch;
    printf ("Splitting string \"%s\" into tokens:\n",str1);
    pch = strtok (str1," ,.-");
    while (pch != NULL)
    {
        
            pch = strtok (NULL, " ,.-");
        
    }
    

    printf("%d 's'=", streetCount);
    
    
    printf("\nstop\n");
    
    return 0;
    
    char *streetNameArray[25];
    streetNameArray[0] = "King Street ";
    streetNameArray[1] = "Queen Street ";
    streetNameArray[2] = "Dundas Ave. ";
    streetNameArray[3] = "Goldie Ave. ";
    streetNameArray[4] = "Eastview Gate ";
    streetNameArray[5] = "Steeles Ave ";
    streetNameArray[6] = "Sandhu Drive ";
    streetNameArray[7] = "Khalsa Drive ";
    streetNameArray[8] = "Abbort Ave. ";
    streetNameArray[9] = "Main Street ";
    streetNameArray[10] = "Kipling Ave. ";
    streetNameArray[11] = "Martin Grove ";
    streetNameArray[12] = "Islington Ave ";
    streetNameArray[13] = "William Parkway ";
    streetNameArray[14] = "Winston Ave. ";
    streetNameArray[15] = "Highway 7 ";
    streetNameArray[16] = "Vankirk Ave ";
    streetNameArray[17] = "Bovaid Dr ";
    streetNameArray[18] = "Airport Road ";
    streetNameArray[19] = "Hulk Ave ";
    streetNameArray[20] = "Wayne Street ";
    streetNameArray[21] = "Kent Ave. ";
    streetNameArray[22] = "Clark Ave. ";
    streetNameArray[23] = "Allen Dr. ";
    streetNameArray[24] = "Captain Dr. ";
    
    
    char *vector[30];
    vector[0] = "(2,2) ";
    vector[1] = "(2,8) ";
    vector[2] = "(4,4) ";
    vector[3] = "(5,5) ";
    vector[4] = "(1,4) ";
    vector[5] = "(1,7) ";
    vector[6] = "(5,6) ";
    vector[7] = "(5,8) ";
    vector[8] = "(3,8) ";
    vector[9] = "(4,8) ";
    vector[10] = "(2,7) ";
    vector[11] = "(4,2) ";
    vector[12] = "(7,7) ";
    vector[13] = "(5,5) ";
    vector[14] = "(1,4) ";
    vector[15] = "(4,7) ";
    vector[16] = "(4,6) ";
    vector[17] = "(7,1) ";
    vector[18] = "(8,1) ";
    vector[19] = "(1,8) ";
    vector[20] = "(7,8) ";
    vector[21] = "(8,7) ";
    vector[22] = "(4,0) ";
    vector[23] = "(3,3) ";
    vector[24] = "(1,1) ";
    vector[25] = "(4,2) ";
    vector[26] = "(5,4) ";
    vector[27] = "(7,8) ";
    vector[28] = "(5,1) ";
    vector[29] = "(6,8) ";
    
    char *strcat(char *dest, const char *src);
    
    int defaultStreetCount = 10;
    if( streetCount == 0)
        streetCount = defaultStreetCount;
    int i = 0;
    for(i =0; i < streetCount; i++)
    {
        char str[80];
        str[0] = 0;
        strcat(str, streetNameArray[GenerateRandom(25)]);
        
        int defaultVectorCount = 5;
        if( vectorCount == 0)
            vectorCount = defaultVectorCount;
        int j =0;
        for(j =0; j < vectorCount; j++)
        {
            strcat(str, vector[GenerateRandom(30)]);
        }
        char finalValue = strlen(str);
        printf("%s.\n", finalValue);
    }
    
    int defaultDelayTime = 5;
    if( delayTime == 0)
        delayTime = defaultDelayTime;
    Timer(delayTime);
    
    int defaultCordinatesRange = 20;
    if( cordinatesRange == 0)
        cordinatesRange = defaultCordinatesRange;
    
    int xCordinate = Cordinates(cordinatesRange);
    int yCordinate = Cordinates(cordinatesRange);
    
    return 0;
}
