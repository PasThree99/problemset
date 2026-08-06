#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

typedef struct Node
{
    int key;
    int val;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct {
    int capacity;
    int elems;
    Node *head;
    Node *tail;
} LRUCache;

void inserElementToHead(LRUCache *cache, Node *node)
{

    printf("%s: Entering\n", __FUNCTION__);
    if (cache->head == NULL)
    {
        cache->head = node;
        cache->tail = node;
        cache->elems ++;
        return;
    }

    node->next = cache->head;
    cache->head->prev = node;
    cache->head = node;
    cache->elems ++;
    return;
}

Node* isKeyInCache(LRUCache* cache, int key)
{
    Node *node = cache->head;
    for(int i = 0; i < cache->elems; i++)
    {
        if (node->key == key)
            return node;

        node = node->next;

        if (! node)
            break;
    }
    return NULL;
}

/* Allocate the LRU cache main structrure */
LRUCache* lRUCacheCreate(int capacity) {
    LRUCache *cache = malloc(sizeof(LRUCache));
    cache->capacity = capacity;
    cache->elems = 0;
    cache->head = NULL;
    cache->tail = NULL;
    return cache;
}

void disconectElement(LRUCache *cache, Node *node)
{
    /* Assume the node elem is part of the cache */
    Node *prev = node->prev;
    Node *next = node->next;

    assert(node);

    bool isHead = !!(node == cache->head);
    bool isTail = !!(node == cache->tail);

    /* 
     * Keep head and tail updated. It does not matter if node is the only element
     * in the cache. If that is the case, the cache will be updated to NULL
     */
    if(isHead)
        cache->head = cache->head->next;
    if(isTail)
        cache->tail = cache->tail->prev;

    node->next = NULL;
    node->prev = NULL;
    
    if(prev)
        prev->next = next;
    if(next)
        next->prev = prev;

    cache->elems --;
}

void lRUCachePut(LRUCache* cache, int key, int value) 
{
    Node *newNode = malloc(sizeof(Node));
    Node *node;
    newNode->val = value;
    newNode->key = key;
    newNode->next = NULL;
    newNode->prev = NULL;

    printf("%s: Entering\n", __FUNCTION__);

    /* Case 1: Cache empty */
    if (cache->elems == 0)
    {
        printf("%s: Cache empty\n", __FUNCTION__);
        inserElementToHead(cache, newNode);
    }
    /* Case 2: Update */
    else if ((node = isKeyInCache(cache, key)))
    {
        printf("%s: Updating\n", __FUNCTION__);
        Node *prev;
        Node *next;

        if (cache->elems == 1)
        {
            /* Avoid the whole thing */
            cache->head->val = newNode->val;
            free(newNode);
            return;
        }

        disconectElement(cache, node);
        /* Connect node to head */
        inserElementToHead(cache, newNode);
        
        free(node);
    }
    /* Case 3: Cache full */
    else if (cache->elems == cache->capacity)
    {
        printf("%s: Cache is full\n", __FUNCTION__);
        Node *lru = cache->tail;
        
        /* Delete tail */
        disconectElement(cache, lru);
        lru->prev = NULL;

        free(lru);

        /* Add new elem to head */
        inserElementToHead(cache, newNode);
    }
    /* Case 1: Generic entry */
    else
    {   
        printf("%s: Generic insert\n", __FUNCTION__);
        inserElementToHead(cache, newNode);
    }
}


int lRUCacheGet(LRUCache* cache, int key) 
{
    Node *node;

    if(cache->elems == 0)
        return -1;

    node = cache->head;
    for(int i = 0 ; i < cache->elems; i ++)
    {
        if (node->key == key)
        {
            Node *prev;
            Node *next;

            /* Unlink node */
            disconectElement(cache, node);

            /* Connect node to head */
            inserElementToHead(cache, node);
            
            return node->val;
        }

        node = node->next;
    }

    return -1;
}

void lRUCacheFree(LRUCache* obj) {
    struct Node *ptr;
    struct Node *next;
    ptr = obj->head;
    while(ptr)
    {
        next = ptr->next;
        free(ptr);
        ptr = next;
    }
    free(obj);
}

void printCache(LRUCache *cache)
{
    struct Node *node = cache->head;
    printf("printing cache\n");
    while(node)
    {
        printf("%d:%d, ", node->key, node->val);
        node = node->next;
    }
    printf("\n");
}

int main()
{
    LRUCache *cache = lRUCacheCreate(2);
    lRUCachePut(cache, 2, 1);
    printf("Inserting 2:2\n");
    lRUCachePut(cache, 2, 2);   
    printCache(cache);
    printf("%d\n", lRUCacheGet(cache, 2));
    lRUCacheFree(cache);
}

