#include <iostream>
#include <stdio.h>

class Node{
    public:
        Node* next = nullptr;
        int value = 0;

        Node(int value){
            this->value = value;
        }
};

class linkedList{
    public:
        Node* head = nullptr;
        Node* tail = nullptr;
        int n = 0;

        int size(){
            return this->n;
        }

        ~linkedList(){
            Node* current = this->head;
            while(current){
                Node* next = current->next;
                delete current;
                current = next;
            }
        }

        void insert_head(int value){
            Node* newNode = new Node(value);

            if(!head){
                head = newNode;
                tail = newNode;
                return;
            }
            
            newNode->next = head;
            head = newNode;
            this->n++;
        }

        void insert_tail(int value){
            Node* newNode = new Node(value);

            if(!head){
                head = newNode;
                tail = newNode;
                return;
            }

            tail->next = newNode;
            tail = newNode;
            this->n++;
        }

        void remove_tail(){
            if(!this->tail){
                return;
            }

            Node* cur = this->head;
            while(cur->next && cur->next->next){
                cur = cur->next;
            }

            delete tail;
            tail = cur;
            this->n--;
        }

        void inplace_reverse(){
            Node* cur = head;
            Node* nex = head->next;
            cur->next = nullptr;
            while(nex){
                Node* temp = nex->next;
                nex->next = cur;
                cur = nex;
                nex = temp;
            }
            nex = head;
            head = tail;
            tail = nex;
        }



        void print(){
            Node* current = this->head;
            while(current){
                std::cout << current->value << "->";
                current = current->next;
            }
            std::cout << std::endl;
        }

        int max(){
            if(!head) return 0;
            int m = head->value;
            Node* cur = head->next;
            while(cur){
                m = std::max(m, cur->value);
                cur = cur->next;
            }
            return m;
        }
};

int main(){
    linkedList ll = linkedList();
    ll.insert_head(1);
    ll.insert_head(3);
    ll.insert_head(2);
    ll.insert_tail(69);
    ll.print();
    ll.inplace_reverse();
    ll.print();
    std::cout << ll.max() << std::endl;
}