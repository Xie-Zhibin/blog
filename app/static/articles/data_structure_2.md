# 数据结构(二)

## 表、栈、队列

### 表(list)
有由 A1,A2,...,AN 组成的表，表的大小为 N ，称 Ai−1 是 Ai 的前驱， Ai+1 是 Ai 的后继。大小为0的表为空表。

表ADT上的操作常见的包括：插入、删除、索引、查找、清空、打印。这是些基本的操作，根据需要可以再添加。

##### 数组实现
对表的所有这些操作都可以通过数组实现。但是用数组实现表时，需要对表的最大长度进行估计，如果表的长度变化较大，会浪费大量的空间。数组实现的表，索引为 O(1) ，插入和删除的最坏情况为 O(N) ，查找、清空和打印为 O(N) 。数组实现的表的插入和删除较慢，而且对表的大小还要有一定的了解，所以通常不用数组来实现表。
```
public class MyArrayList<AnyType> implements Iterable<AnyType>
{
    /**
     * Construct an empty ArrayList.
     */
    public MyArrayList( )
    {
        doClear( );
    }

    /**
     * Returns the number of items in this collection.
     * @return the number of items in this collection.
     */
    public int size( )
    {
        return theSize;
    }

    /**
     * Returns true if this collection is empty.
     * @return true if this collection is empty.
     */
    public boolean isEmpty( )
    {
        return size( ) == 0;
    }

    /**
     * Returns the item at position idx.
     * @param idx the index to search in.
     * @throws ArrayIndexOutOfBoundsException if index is out of range.
     */
    public AnyType get( int idx )
    {
        if( idx < 0 || idx >= size( ) )
            throw new ArrayIndexOutOfBoundsException( "Index " + idx + "; size " + size( ) );
        return theItems[ idx ];
    }

    /**
     * Changes the item at position idx.
     * @param idx the index to change.
     * @param newVal the new value.
     * @return the old value.
     * @throws ArrayIndexOutOfBoundsException if index is out of range.
     */
    public AnyType set( int idx, AnyType newVal )
    {
        if( idx < 0 || idx >= size( ) )
            throw new ArrayIndexOutOfBoundsException( "Index " + idx + "; size " + size( ) );
        AnyType old = theItems[ idx ];
        theItems[ idx ] = newVal;

        return old;
    }

    @SuppressWarnings("unchecked")
    public void ensureCapacity( int newCapacity )
    {
        if( newCapacity < theSize )
            return;

        AnyType [ ] old = theItems;
        theItems = (AnyType []) new Object[ newCapacity ];
        for( int i = 0; i < size( ); i++ )
            theItems[ i ] = old[ i ];
    }

    /**
     * Adds an item to this collection, at the end.
     * @param x any object.
     * @return true.
     */
    public boolean add( AnyType x )
    {
    add( size( ), x );
        return true;
    }

    /**
     * Adds an item to this collection, at the specified index.
     * @param x any object.
     * @return true.
     */
    public void add( int idx, AnyType x )
    {
        if( theItems.length == size( ) )
            ensureCapacity( size( ) * 2 + 1 );

        for( int i = theSize; i > idx; i-- )
            theItems[ i ] = theItems[ i - 1 ];

        theItems[ idx ] = x;
        theSize++;
    }

    /**
     * Removes an item from this collection.
     * @param idx the index of the object.
     * @return the item was removed from the collection.
     */
    public AnyType remove( int idx )
    {
        AnyType removedItem = theItems[ idx ];

        for( int i = idx; i < size( ) - 1; i++ )
            theItems[ i ] = theItems[ i + 1 ];
        theSize--;

        return removedItem;
    }

    /**
     * Change the size of this collection to zero.
     */
    public void clear( )
    {
        doClear( );
    }

    private void doClear( )
    {
        theSize = 0;
        ensureCapacity( DEFAULT_CAPACITY );
    }

    /**
     * Obtains an Iterator object used to traverse the collection.
     * @return an iterator positioned prior to the first element.
     */
    public java.util.Iterator<AnyType> iterator( )
    {
        return new ArrayListIterator( );
    }

    /**
     * Returns a String representation of this collection.
     */
    public String toString( )
    {
            StringBuilder sb = new StringBuilder( "[ " );

            for( AnyType x : this )
                sb.append( x + " " );
            sb.append( "]" );

            return new String( sb );
    }

    /**
     * This is the implementation of the ArrayListIterator.
     * It maintains a notion of a current position and of
     * course the implicit reference to the MyArrayList.
     */
    private class ArrayListIterator implements java.util.Iterator<AnyType>
    {
        private int current = 0;
        private boolean okToRemove = false;

        public boolean hasNext( )
        {
            return current < size( );
        }


        public AnyType next( )
        {
            if( !hasNext( ) )
                throw new java.util.NoSuchElementException( );

            okToRemove = true;
            return theItems[ current++ ];
        }

        public void remove( )
        {
            if( !okToRemove )
                throw new IllegalStateException( );

            MyArrayList.this.remove( --current );
            okToRemove = false;
        }
    }

    private static final int DEFAULT_CAPACITY = 10;

    private AnyType [ ] theItems;
    private int theSize;
}

class TestArrayList
{
    public static void main( String [ ] args )
    {
        MyArrayList<Integer> lst = new MyArrayList<>( );

        for( int i = 0; i < 10; i++ )
                lst.add( i );
        for( int i = 20; i < 30; i++ )
                lst.add( 0, i );

        lst.remove( 0 );
        lst.remove( lst.size( ) - 1 );

        System.out.println( lst );
    }
}

```

##### 链表实现
为了避免插入和删除的线性开销，需要保证表可以不连续存储。
链表由一系列在内存中可以不相连的结构组成，每个结构含有表元素和指向后继结构的指针，最后一个结构的指针为 NULL 。为了避免删除操作的一些麻烦，一般在链表开始增加一个标志节点，称为表头，它不含有表元素。
在经典的链表中，每个节点均存储到其下一节点的链，而拥有指向最后节点的链并不提供最后节点的前驱节点的任何信息。
双向链表则是让每个节点持有一个指向它在表中的前驱节点的链。
```
/**
 * LinkedList class implements a doubly-linked list.
 */
public class MyLinkedList<AnyType> implements Iterable<AnyType>
{
    /**
     * Construct an empty LinkedList.
     */
    public MyLinkedList( )
    {
        doClear( );
    }

    private void clear( )
    {
        doClear( );
    }

    /**
     * Change the size of this collection to zero.
     */
    public void doClear( )
    {
        beginMarker = new Node<>( null, null, null );
        endMarker = new Node<>( null, beginMarker, null );
        beginMarker.next = endMarker;

        theSize = 0;
        modCount++;
    }

    /**
     * Returns the number of items in this collection.
     * @return the number of items in this collection.
     */
    public int size( )
    {
        return theSize;
    }

    public boolean isEmpty( )
    {
        return size( ) == 0;
    }

    /**
     * Adds an item to this collection, at the end.
     * @param x any object.
     * @return true.
     */
    public boolean add( AnyType x )
    {
        add( size( ), x );
        return true;
    }

    /**
     * Adds an item to this collection, at specified position.
     * Items at or after that position are slid one position higher.
     * @param x any object.
     * @param idx position to add at.
     * @throws IndexOutOfBoundsException if idx is not between 0 and size(), inclusive.
     */
    public void add( int idx, AnyType x )
    {
        addBefore( getNode( idx, 0, size( ) ), x );
    }

    /**
     * Adds an item to this collection, at specified position p.
     * Items at or after that position are slid one position higher.
     * @param p Node to add before.
     * @param x any object.
     * @throws IndexOutOfBoundsException if idx is not between 0 and size(), inclusive.
     */
    private void addBefore( Node<AnyType> p, AnyType x )
    {
        Node<AnyType> newNode = new Node<>( x, p.prev, p );
        newNode.prev.next = newNode;
        p.prev = newNode;
        theSize++;
        modCount++;
    }


    /**
     * Returns the item at position idx.
     * @param idx the index to search in.
     * @throws IndexOutOfBoundsException if index is out of range.
     */
    public AnyType get( int idx )
    {
        return getNode( idx ).data;
    }

    /**
     * Changes the item at position idx.
     * @param idx the index to change.
     * @param newVal the new value.
     * @return the old value.
     * @throws IndexOutOfBoundsException if index is out of range.
     */
    public AnyType set( int idx, AnyType newVal )
    {
        Node<AnyType> p = getNode( idx );
        AnyType oldVal = p.data;

        p.data = newVal;
        return oldVal;
    }

    /**
     * Gets the Node at position idx, which must range from 0 to size( ) - 1.
     * @param idx index to search at.
     * @return internal node corresponding to idx.
     * @throws IndexOutOfBoundsException if idx is not between 0 and size( ) - 1, inclusive.
     */
    private Node<AnyType> getNode( int idx )
    {
        return getNode( idx, 0, size( ) - 1 );
    }

    /**
     * Gets the Node at position idx, which must range from lower to upper.
     * @param idx index to search at.
     * @param lower lowest valid index.
     * @param upper highest valid index.
     * @return internal node corresponding to idx.
     * @throws IndexOutOfBoundsException if idx is not between lower and upper, inclusive.
     */
    private Node<AnyType> getNode( int idx, int lower, int upper )
    {
        Node<AnyType> p;

        if( idx < lower || idx > upper )
            throw new IndexOutOfBoundsException( "getNode index: " + idx + "; size: " + size( ) );

        if( idx < size( ) / 2 )
        {
            p = beginMarker.next;
            for( int i = 0; i < idx; i++ )
                p = p.next;
        }
        else
        {
            p = endMarker;
            for( int i = size( ); i > idx; i-- )
                p = p.prev;
        }

        return p;
    }

    /**
     * Removes an item from this collection.
     * @param idx the index of the object.
     * @return the item was removed from the collection.
     */
    public AnyType remove( int idx )
    {
        return remove( getNode( idx ) );
    }

    /**
     * Removes the object contained in Node p.
     * @param p the Node containing the object.
     * @return the item was removed from the collection.
     */
    private AnyType remove( Node<AnyType> p )
    {
        p.next.prev = p.prev;
        p.prev.next = p.next;
        theSize--;
        modCount++;

        return p.data;
    }

    /**
     * Returns a String representation of this collection.
     */
    public String toString( )
    {
        StringBuilder sb = new StringBuilder( "[ " );

        for( AnyType x : this )
            sb.append( x + " " );
        sb.append( "]" );

        return new String( sb );
    }

    /**
     * Obtains an Iterator object used to traverse the collection.
     * @return an iterator positioned prior to the first element.
     */
    public java.util.Iterator<AnyType> iterator( )
    {
        return new LinkedListIterator( );
    }

    /**
     * This is the implementation of the LinkedListIterator.
     * It maintains a notion of a current position and of
     * course the implicit reference to the MyLinkedList.
     */
    private class LinkedListIterator implements java.util.Iterator<AnyType>
    {
        private Node<AnyType> current = beginMarker.next;
        private int expectedModCount = modCount;
        private boolean okToRemove = false;

        public boolean hasNext( )
        {
            return current != endMarker;
        }

        public AnyType next( )
        {
            if( modCount != expectedModCount )
                throw new java.util.ConcurrentModificationException( );
            if( !hasNext( ) )
                throw new java.util.NoSuchElementException( );

            AnyType nextItem = current.data;
            current = current.next;
            okToRemove = true;
            return nextItem;
        }

        public void remove( )
        {
            if( modCount != expectedModCount )
                throw new java.util.ConcurrentModificationException( );
            if( !okToRemove )
                throw new IllegalStateException( );

            MyLinkedList.this.remove( current.prev );
            expectedModCount++;
            okToRemove = false;
        }
    }

    /**
     * This is the doubly-linked list node.
     */
    private static class Node<AnyType>
    {
        public Node( AnyType d, Node<AnyType> p, Node<AnyType> n )
        {
            data = d; prev = p; next = n;
        }

        public AnyType data;
        public Node<AnyType>   prev;
        public Node<AnyType>   next;
    }

    private int theSize;
    private int modCount = 0;
    private Node<AnyType> beginMarker;
    private Node<AnyType> endMarker;
}

class TestLinkedList
{
    public static void main( String [ ] args )
    {
        MyLinkedList<Integer> lst = new MyLinkedList<>( );

        for( int i = 0; i < 10; i++ )
                lst.add( i );
        for( int i = 20; i < 30; i++ )
                lst.add( 0, i );

        lst.remove( 0 );
        lst.remove( lst.size( ) - 1 );

        System.out.println( lst );

        java.util.Iterator<Integer> itr = lst.iterator( );
        while( itr.hasNext( ) )
        {
                itr.next( );
                itr.remove( );
                System.out.println( lst );
        }
    }
}

```

****

### 栈(stack)
栈是限制插入和删除只能在一个位置上进行的表，该位置是表的末端，叫做栈的顶，栈有时又叫做LIFO(后进先出表)。对栈的基本操作有push(进栈)和出栈(pop)，前者相当于插入，后者则是删除最后的插入的元素。一般的抽象栈模型是，存在某个元素位于栈顶，而该元素是唯一的可见元素。
由于栈是一个表，因此任何实现表的方法都能实现栈。
对栈的这种限制可以使栈的操作以一个非常快的常数时间内完成。
##### 栈的链表实现
```
import java.util.LinkedList;;

public class MyStack<AnyType> {
    private LinkedList<AnyType> linkedList = new LinkedList<>();

    public void push(AnyType item) {
        linkedList.add(item);
    }

    public AnyType pop() {
        if (getSize() > 0) {
            return linkedList.removeLast();

        } else {
            return null;
        }
    }

    public boolean isEmpty() {
        return getSize() == 0;
    }

    public int getSize() {
        return linkedList.size();
    }

    public static void main(String[] args) {
        MyStack<Integer> stack = new MyStack<>();
        for (int i=0;i<50;i++) {
            stack.push(i);
        }

        while (!stack.isEmpty()) {
            System.out.println("Size: " + stack.getSize());
            System.out.println("Value: " + stack.pop());
            System.out.println("--------------");
        }

    }
}

```
##### 栈的数组实现
```
import java.util.ArrayList;

public class MyStack<AnyType> {
    private ArrayList<AnyType> arrayList = new ArrayList<>();

    public void push(AnyType item) {
        arrayList.add(item);
    }

    public AnyType pop() {
        return arrayList.remove(getSize() - 1);
    }

    public boolean isEmpty() {
        return arrayList.isEmpty();
    }

    public int getSize() {
        return arrayList.size();
    }

    public static void main(String[] args) {
        MyStack<Integer> stack = new MyStack<>();
        for (int i=0;i<5;i++) {
            stack.push(i);
        }

        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }

    }
}
```
栈常用的地方有，平衡符号(编译器检查配对的符号)、后缀表达式、方法调用、浏览器进入/返回(入栈/出栈)页面等

****

### 队列(queue)
和栈一样，队列也是表,但是使用队列时插入在一端进行而删除则在另一端进行。队列的基本操作是enqueue(入队)，它是在表的末端(队尾rear)插入一个元素;和dequeue(出队)，它是删除(并返回)在表的开头(对头front)的元素。
元素入队的位置是队尾的位置，即队尾始终指向元素下次插入的位置。
队列可以很好地异步处理数据传送和存储，当频繁地向数据库中插入数据、频繁地向搜索引擎提交数据，就可采取队列来异步插入。另外，还可以将较慢的处理逻辑、有并发数量限制的处理逻辑，通过消息队列放在后台处理，例如FLV视频转换、发送手机短信、发送电子邮件等。
##### 循环队列的数组实现
```
// @author island
// Nov 17, 2016 8:58:18 PM
import java.util.Random;

public class MyQueue<AnyType> {
    private final int CAPACITY;
    private AnyType[] queue;
    private int front, rear, size;

    MyQueue() {
        this(10);
    }

    MyQueue(int capacity) {
        CAPACITY = capacity;
        queue = (AnyType[]) new Object[CAPACITY];
    }

    public boolean enqueue(AnyType item) {
        if (isFull()) {
            return false;
        }
        size++;
        queue[rear] = item;
        rear = (rear + 1) % CAPACITY;
        return true;
    }

    public AnyType dequeue() {
        if (isEmpty()) {
            return null;
        }
        size--;
        AnyType temp = queue[front];
        queue[front] = null;
        front = (front + 1) % CAPACITY;
        return temp;
    }

    public int getSize() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == CAPACITY;
    }

    public void traverse() {
        for (int i=front; i < size + front; i++) {
            System.out.println(queue[i % CAPACITY]);
        }
    }

    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<>(10);
        Random rand = new Random(12);
        for (int i=0; !queue.isFull();i++) {
            queue.enqueue(rand.nextInt());
        }
        queue.traverse();
        System.out.println();

        queue.dequeue();
        queue.enqueue(12);
        queue.enqueue(34);

        queue.traverse();
    }
}

```