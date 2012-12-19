/*
 * 二叉查找树（ADT）： 对于树中每一个节点X，
 * 它的左子树中所有关键字的值都小于X，它的右子树中所有关键字的值都大于X
 * */
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
}BTree;

/* creat a tree */
BTree * create_tree(BTree *T)
{
    int data;
    scanf("%d", &data);
    if(data == 0){
        T = NULL;
    }else{
        T = (BTree *)malloc(sizeof(struct TreeNode));
        T->data = data;
        T->left = create_tree(T->left);
        T->right = create_tree(T->right);
    }
    return T;
}

/* to find Maxdata*/
BTree * find_max_tree(BTree *T)
{
    if(T == NULL)
        return NULL;
    if(T->right == NULL)
        return T;
    else
        return find_max_tree(T->right);
}

/* to find Mixdata */
BTree * find_min_tree(BTree *T)
{
    if(T == NULL)
        return NULL;
    while(T->left != NULL)
        T = T->left;
    
    return T;
}

/* insert */
BTree * insert_to_tree(int n, BTree *T)
{
    if(T == NULL){
        T = (BTree *)malloc(sizeof(BTree));
        T->data = n;
        T->left = NULL;
        T->right = NULL;
    }else if(n < T->data){
        T->left = insert_to_tree(n, T->left);
    }else if(n > T->data){
        T->right = insert_to_tree(n, T->right);
    }

    return T;
}

/* delete */
/* 删除策略，在ADT树中：
 * 1. 如果要删除的节点是叶子节点， 则可以立即删除。
 * 2. 如果该节点有1个儿子，则可以通过父节点的绕过该节点删除。
 * 3. 如果有两个儿子，用其右子树中最小的代替该节点的数据并递归的删除那个节点。
 * */
BTree * delete_from_tree(int n, BTree *T)
{
    BTree *Temp;

    if(T == NULL)
        return T;
    else if(n > T->data)
        T->right = delete_from_tree(n, T->right);
    else if(n < T->data)
        T->left = delete_from_tree(n, T->left);
    else{
        printf("%d\n", T->data);
        if(T->left && T->right){
            Temp = find_min_tree(T->right);        
            T->data = Temp->data;
            T->right = delete_from_tree(T->data, T->right);
        }else{
            Temp = T;
            if(T->left == NULL)
                T = T->right;
            if(T->right == NULL)
                T = T->left;
            free(Temp);
        }
    }
    return T;
}

void inorder_traversal(BTree *T)
{   
    if(T != NULL){
        inorder_traversal(T->left);
        printf("%4d", T->data);
        inorder_traversal(T->right);
    }
}
int main(int argc, const char *argv[])
{
    BTree *root, *max, *min, *T;
    
    root = create_tree(root);
    //inorder_traversal(root); 
    //max = find_max_tree(root);
    //min = find_min_tree(root);
    //printf("max data is : %d, min data is : %d\n", max->data, min->data);

    //inorder_traversal(insert_to_tree(5, root));
 
    T = delete_from_tree(5, root);
    return 0;
}
