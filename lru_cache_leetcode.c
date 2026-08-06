#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

int VERBOSE = false;

struct Node
{
    int key;
    int val;
    struct Node *next;
    struct Node *prev;
};

typedef struct {
    int capacity;
    int elems;
    struct Node *head;
    struct Node *tail;
} LRUCache;

LRUCache* lRUCacheCreate(int capacity) {
    LRUCache *cache = malloc(sizeof(LRUCache));
    cache->capacity = capacity;
    cache->elems = 0;
    cache->head = NULL;
    cache->tail = NULL;
    return cache;
}

bool isCacheEmpty(LRUCache *cache)
{
    return !!(cache->elems == 0);
}

bool isCacheFull(LRUCache *cache)
{
    return !!(cache->elems == cache->capacity);
}

void disconectElement(LRUCache *cache, struct Node *node)
{
    struct Node *prev = node->prev;
    struct Node *next = node->next;
    
    node->prev = NULL;
    node->next = NULL;

    if (prev && next)
    {
        /* Middle element */
        prev->next = next;
        next->prev = prev;
    }
    else if (prev)
    {
        /* Special case: tail */
        prev->next = NULL;
        cache->tail = prev;
    }
    else if (next)
    {
        /* Special case: head */
        next->prev = NULL;
        cache->head = next;
    }
    return;
}

void moveElementToHead(LRUCache *cache, struct Node *node)
{
    if (cache->elems == 1 && node == cache->head)
    {
        /* We are the head, there is nothing to do here */
        return;
    }
    if (node->next != NULL || node->prev != NULL)
        disconectElement(cache, node);

    node->next = cache->head;
    cache->head->prev = node;
    cache->head = node;
    return;
}

int lRUCacheGet(LRUCache* obj, int key) {
    struct Node *ptr = obj->head;
    struct Node *prev;
    struct Node *next;

    if (VERBOSE)
        printf("Looking for key %d\n", key);
    
    /* No elements inthe cache yet */
    if (isCacheEmpty(obj))
    {
        if (VERBOSE)
            printf("Cache is empty, returning\n");
        return -1;
    }

    /* Look for the key in the node LL */
    while(ptr)
    {
        if (VERBOSE)
            printf("Iterating. key=%d expected=%d\n", ptr->key, key);
        if (ptr->key == key)
            break;
        ptr = ptr->next;
    }

    if (ptr == NULL)
    {
        if (VERBOSE)
            printf("Key not found in cache!\n");
        return -1;
    }
    moveElementToHead(obj, ptr);

    return ptr->val;
}

struct Node* isKeyInCache(LRUCache* obj, int key)
{
    struct Node *ptr = obj->head;
    while (ptr && ptr->key != key)
        if (VERBOSE)
            printf("isKeyInCache: iteration. key=%d\n", ptr->key);
        ptr = ptr->next;
    return ptr;

}

void lRUCachePut(LRUCache* obj, int key, int value) {
    struct Node *newNode = malloc(sizeof(struct Node));
    struct Node *updateNode;
    newNode->val = value;
    newNode->key = key;
    newNode->next = NULL;
    newNode->prev = NULL;

    if (VERBOSE)
        printf("Inserting %d:%d to cache\n", key, value);

    if (isCacheEmpty(obj))
    {
        if (VERBOSE)
            printf("Cache is empty\n");
        obj->head = newNode;
        obj->tail = newNode;
        obj->head->next = NULL;
        obj->head->prev = NULL;
        obj->elems ++;
        return;
    }
    else if((updateNode = isKeyInCache(obj, key)))
    {
        struct Node *prev;
        struct Node *next;

        if (VERBOSE)
            printf("Key is found in cache\n");

        updateNode->val = value;
        /* 
         * If there is only one element in the cache or this is the 1st element
         * there we have nothing left to do 
         */
        if (obj->elems == 1 || updateNode == obj->head)
        {

            if (VERBOSE)
                printf("Element is head or we only have 1 element\n");
            free(newNode);
            return; /* Nothing else to do */
        }

        moveElementToHead(obj, updateNode);
        free(newNode);
        return;
    }
    else if (isCacheFull(obj))
    {

        struct Node *lruElem = obj->tail;
        if (VERBOSE)
            printf("Cache is full\n");

        obj->tail = obj->tail->prev;

        /* Remove the last recently used element */
        disconectElement(obj, lruElem);
        free(lruElem);

        /* Insert the new element at the head */
        moveElementToHead(obj, newNode);

        return;
    }
    else
    {
        if (VERBOSE)
            printf("Generic insertion\n");
        /* Insert the new element at the head */
        moveElementToHead(obj, newNode);
        obj->elems ++;
    }
    
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
    LRUCache *cache = lRUCacheCreate(1);
    VERBOSE = true;
    printf("Inserting 2:1\n");
    lRUCachePut(cache, 2, 1);
    printf("%d\n", lRUCacheGet(cache, 2));
    printf("Inserting 2:2\n");
    lRUCachePut(cache, 2, 2);   
    printf("Inserting 3:3\n");
    lRUCachePut(cache, 3, 3);   
    printf("Inserting 6:8\n");
    lRUCachePut(cache, 6, 8);   
    printCache(cache);


    lRUCacheFree(cache);
}

/**
 * Your LRUCache struct will be instantiated and called as such:
 * LRUCache* obj = lRUCacheCreate(capacity);
 * int param_1 = lRUCacheGet(obj, key);
 
 * lRUCachePut(obj, key, value);
 
 * lRUCacheFree(obj);
*/