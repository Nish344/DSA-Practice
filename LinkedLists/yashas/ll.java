#HW1
class Node{
    int data;
    Node next;

    Node(int d,Node n){
        data=d;
        next=n;
    }
    Node(int d2){
        data=d2;
        next=null;
    }
}
public class ll{
    public static Node reverse(Node n){
    Node prev=null;
    Node temp=n;
    while(temp!=null){
        Node front=temp.next;
        temp.next=prev;
        prev=temp;
        temp=front;
    }
    return prev;
}
public static int max(Node n){
    Node temp=n;
    int maximum=Integer.MIN_VALUE;
    if(n==null) return Integer.MIN_VALUE;
    while(temp!=null){
        maximum=Math.max(maximum,temp.data);
        temp=temp.next;
    }
    return maximum;
}
    public static void main(String [] args){
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);
        System.out.println("MAX= "+max(head));
        Node res=reverse(head);
        Node temp = res;
        while (temp!=null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
}
