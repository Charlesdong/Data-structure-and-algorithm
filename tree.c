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
    BTree *root;
    root = create_tree(root);
    inorder_traversal(root); 
    return 0;
}
