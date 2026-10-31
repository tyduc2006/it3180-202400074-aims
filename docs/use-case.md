# AIMS – Use Case Description

## 1. Actors

- **Customer**: Người dùng mua và tìm kiếm DVD
- **Administrator**: Người quản lý hệ thống và thông tin DVD

## 2. Use Cases

### Customer
- View DVD Information
- Search DVD by Title
- Add DVD to Cart
- Remove DVD from Cart
- View Cart
- Calculate Cart Total

### Administrator
- Manage DVD Information

## 3. Use Case Diagram

```mermaid
flowchart LR
    C[Customer]
    A[Administrator]

    UC1((View DVD Information))
    UC2((Search DVD by Title))
    UC3((Add DVD to Cart))
    UC4((Remove DVD from Cart))
    UC5((View Cart))
    UC6((Calculate Cart Total))
    UC7((Manage DVD Information))

    C --- UC1
    C --- UC2
    C --- UC3
    C --- UC4
    C --- UC5
    C --- UC6
    A --- UC7
```