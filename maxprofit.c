#include <stdio.h>

int maxprofit(int prices[], int pricesSize){
    int max_price = 0;
    for (int i = 0; i < pricesSize; i++)
    {
        for (int j=i+1; j < pricesSize; j++)
        {
            int profit = prices[j] - prices[i];
            if (profit > max_price)
            {
                    max_price = profit;
            }
        }
    }
    return max_price;
}
