# Resolved Indirect IAT Call Sites in MSDISPLAYSDKWRRAPER.dll

Total indirect IAT call sites resolved: `356`

## `KERNEL32.dll!CloseHandle` (13 Call Sites)

### Line 25249 (Address `0x180074088`)
```assembly
   1800171f3:	3c 19                	cmp    $0x19,%al
   1800171f5:	76 0d                	jbe    0x180017204
   1800171f7:	80 f9 3b             	cmp    $0x3b,%cl
   1800171fa:	75 94                	jne    0x180017190
   1800171fc:	41 be 01 00 00 00    	mov    $0x1,%r14d
   180017202:	eb 8c                	jmp    0x180017190
   180017204:	48 63 c3             	movslq %ebx,%rax
   180017207:	88 8c 04 20 01 00 00 	mov    %cl,0x120(%rsp,%rax,1)
   18001720e:	ff c3                	inc    %ebx
   180017210:	e9 6a ff ff ff       	jmp    0x18001717f
   180017215:	33 ff                	xor    %edi,%edi
   180017217:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   18001721c:	48 8b 4e 08          	mov    0x8(%rsi),%rcx
   180017220:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   180017224:	74 0e                	je     0x180017234
   180017226:	ff 15 5c ce 05 00    	call   *0x5ce5c(%rip)        # 0x180074088
   18001722c:	48 c7 46 08 ff ff ff 	movq   $0xffffffffffffffff,0x8(%rsi)
   180017233:	ff 
   180017234:	48 8b 06             	mov    (%rsi),%rax
   180017237:	ba 01 00 00 00       	mov    $0x1,%edx
```

### Line 26624 (Address `0x180074088`)
```assembly
   18001849b:	ff d0                	call   *%rax
   18001849d:	90                   	nop
   18001849e:	c6 43 3c 00          	movb   $0x0,0x3c(%rbx)
   1800184a2:	ba 44 01 00 00       	mov    $0x144,%edx
   1800184a7:	48 8b cb             	mov    %rbx,%rcx
   1800184aa:	e8 41 cb 03 00       	call   0x180054ff0
   1800184af:	90                   	nop
   1800184b0:	48 83 c7 18          	add    $0x18,%rdi
   1800184b4:	49 83 ee 01          	sub    $0x1,%r14
   1800184b8:	75 96                	jne    0x180018450
   1800184ba:	44 38 b6 f9 03 00 00 	cmp    %r14b,0x3f9(%rsi)
   1800184c1:	74 4e                	je     0x180018511
   1800184c3:	48 8b 0d c6 e8 08 00 	mov    0x8e8c6(%rip),%rcx        # 0x1800a6d90
   1800184ca:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   1800184ce:	74 12                	je     0x1800184e2
   1800184d0:	ff 15 b2 bb 05 00    	call   *0x5bbb2(%rip)        # 0x180074088
   1800184d6:	90                   	nop
   1800184d7:	48 c7 05 ae e8 08 00 	movq   $0xffffffffffffffff,0x8e8ae(%rip)        # 0x1800a6d90
   1800184de:	ff ff ff ff 
   1800184e2:	48 8b 0d 47 01 09 00 	mov    0x90147(%rip),%rcx        # 0x1800a8630
```

### Line 26669 (Address `0x180074088`)
```assembly
   180018555:	49 8d 4f 08          	lea    0x8(%r15),%rcx
   180018559:	ff 15 71 bb 05 00    	call   *0x5bb71(%rip)        # 0x1800740d0
   18001855f:	90                   	nop
   180018560:	49 89 1f             	mov    %rbx,(%r15)
   180018563:	48 8d 05 26 2b 08 00 	lea    0x82b26(%rip),%rax        # 0x18009b090
   18001856a:	48 89 06             	mov    %rax,(%rsi)
   18001856d:	48 8b 4e 08          	mov    0x8(%rsi),%rcx
   180018571:	48 8b 5c 24 50       	mov    0x50(%rsp),%rbx
   180018576:	48 8b 6c 24 58       	mov    0x58(%rsp),%rbp
   18001857b:	48 8b 74 24 60       	mov    0x60(%rsp),%rsi
   180018580:	48 8b 7c 24 68       	mov    0x68(%rsp),%rdi
   180018585:	48 83 c4 30          	add    $0x30,%rsp
   180018589:	41 5f                	pop    %r15
   18001858b:	41 5e                	pop    %r14
   18001858d:	41 5c                	pop    %r12
   18001858f:	48 ff 25 f2 ba 05 00 	rex.W jmp *0x5baf2(%rip)        # 0x180074088
   180018596:	cc                   	int3
   180018597:	cc                   	int3
   180018598:	cc                   	int3
   180018599:	cc                   	int3
```

### Line 26793 (Address `0x180074088`)
```assembly
   180018761:	84 c0                	test   %al,%al
   180018763:	75 13                	jne    0x180018778
   180018765:	48 8b cd             	mov    %rbp,%rcx
   180018768:	e8 c3 0d 00 00       	call   0x180019530
   18001876d:	0f b6 85 f9 03 00 00 	movzbl 0x3f9(%rbp),%eax
   180018774:	84 c0                	test   %al,%al
   180018776:	74 57                	je     0x1800187cf
   180018778:	48 8b cd             	mov    %rbp,%rcx
   18001877b:	e8 c0 08 00 00       	call   0x180019040
   180018780:	eb 4d                	jmp    0x1800187cf
   180018782:	80 bd f9 03 00 00 00 	cmpb   $0x0,0x3f9(%rbp)
   180018789:	74 44                	je     0x1800187cf
   18001878b:	48 8b 0d fe e5 08 00 	mov    0x8e5fe(%rip),%rcx        # 0x1800a6d90
   180018792:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   180018796:	74 11                	je     0x1800187a9
   180018798:	ff 15 ea b8 05 00    	call   *0x5b8ea(%rip)        # 0x180074088
   18001879e:	48 c7 05 e7 e5 08 00 	movq   $0xffffffffffffffff,0x8e5e7(%rip)        # 0x1800a6d90
   1800187a5:	ff ff ff ff 
   1800187a9:	48 8b 0d 80 fe 08 00 	mov    0x8fe80(%rip),%rcx        # 0x1800a8630
   1800187b0:	48 85 c9             	test   %rcx,%rcx
```

### Line 27772 (Address `0x180074088`)
```assembly
   18001968b:	ff 15 77 aa 05 00    	call   *0x5aa77(%rip)        # 0x180074108
   180019691:	44 8b c0             	mov    %eax,%r8d
   180019694:	48 8d 15 35 2f 08 00 	lea    0x82f35(%rip),%rdx        # 0x18009c5d0
   18001969b:	eb 18                	jmp    0x1800196b5
   18001969d:	0f b7 84 24 60 01 00 	movzwl 0x160(%rsp),%eax
   1800196a4:	00 
   1800196a5:	66 3b c5             	cmp    %bp,%ax
   1800196a8:	74 51                	je     0x1800196fb
   1800196aa:	44 0f b7 c0          	movzwl %ax,%r8d
   1800196ae:	48 8d 15 7b 2f 08 00 	lea    0x82f7b(%rip),%rdx        # 0x18009c630
   1800196b5:	48 8b 0d 4c ef 08 00 	mov    0x8ef4c(%rip),%rcx        # 0x1800a8608
   1800196bc:	e8 cf cb ff ff       	call   0x180016290
   1800196c1:	48 8b 0d c8 d6 08 00 	mov    0x8d6c8(%rip),%rcx        # 0x1800a6d90
   1800196c8:	48 3b cb             	cmp    %rbx,%rcx
   1800196cb:	74 0d                	je     0x1800196da
   1800196cd:	ff 15 b5 a9 05 00    	call   *0x5a9b5(%rip)        # 0x180074088
   1800196d3:	48 89 1d b6 d6 08 00 	mov    %rbx,0x8d6b6(%rip)        # 0x1800a6d90
   1800196da:	48 8b 0d 4f ef 08 00 	mov    0x8ef4f(%rip),%rcx        # 0x1800a8630
   1800196e1:	48 85 c9             	test   %rcx,%rcx
   1800196e4:	74 64                	je     0x18001974a
```

### Line 28232 (Address `0x180074088`)
```assembly
   180019d69:	cc                   	int3
   180019d6a:	cc                   	int3
   180019d6b:	cc                   	int3
   180019d6c:	cc                   	int3
   180019d6d:	cc                   	int3
   180019d6e:	cc                   	int3
   180019d6f:	cc                   	int3
   180019d70:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   180019d75:	57                   	push   %rdi
   180019d76:	48 83 ec 20          	sub    $0x20,%rsp
   180019d7a:	48 8d 05 0f 13 08 00 	lea    0x8130f(%rip),%rax        # 0x18009b090
   180019d81:	48 8b f9             	mov    %rcx,%rdi
   180019d84:	48 89 01             	mov    %rax,(%rcx)
   180019d87:	8b da                	mov    %edx,%ebx
   180019d89:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   180019d8d:	ff 15 f5 a2 05 00    	call   *0x5a2f5(%rip)        # 0x180074088
   180019d93:	f6 c3 01             	test   $0x1,%bl
   180019d96:	74 0d                	je     0x180019da5
   180019d98:	ba 18 00 00 00       	mov    $0x18,%edx
   180019d9d:	48 8b cf             	mov    %rdi,%rcx
```

### Line 28259 (Address `0x180074088`)
```assembly
   180019db4:	cc                   	int3
   180019db5:	cc                   	int3
   180019db6:	cc                   	int3
   180019db7:	cc                   	int3
   180019db8:	cc                   	int3
   180019db9:	cc                   	int3
   180019dba:	cc                   	int3
   180019dbb:	cc                   	int3
   180019dbc:	cc                   	int3
   180019dbd:	cc                   	int3
   180019dbe:	cc                   	int3
   180019dbf:	cc                   	int3
   180019dc0:	48 8d 05 c9 12 08 00 	lea    0x812c9(%rip),%rax        # 0x18009b090
   180019dc7:	48 89 01             	mov    %rax,(%rcx)
   180019dca:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   180019dce:	48 ff 25 b3 a2 05 00 	rex.W jmp *0x5a2b3(%rip)        # 0x180074088
   180019dd5:	cc                   	int3
   180019dd6:	cc                   	int3
   180019dd7:	cc                   	int3
   180019dd8:	cc                   	int3
```

### Line 29078 (Address `0x180074088`)
```assembly
   18001a6f8:	48 ff 60 18          	rex.W jmp *0x18(%rax)
   18001a6fc:	cc                   	int3
   18001a6fd:	cc                   	int3
   18001a6fe:	cc                   	int3
   18001a6ff:	cc                   	int3
   18001a700:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   18001a705:	57                   	push   %rdi
   18001a706:	48 83 ec 20          	sub    $0x20,%rsp
   18001a70a:	48 8d 05 9f 1c 08 00 	lea    0x81c9f(%rip),%rax        # 0x18009c3b0
   18001a711:	48 8b d9             	mov    %rcx,%rbx
   18001a714:	48 89 01             	mov    %rax,(%rcx)
   18001a717:	8b fa                	mov    %edx,%edi
   18001a719:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   18001a71d:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   18001a721:	74 0e                	je     0x18001a731
   18001a723:	ff 15 5f 99 05 00    	call   *0x5995f(%rip)        # 0x180074088
   18001a729:	48 c7 43 08 ff ff ff 	movq   $0xffffffffffffffff,0x8(%rbx)
   18001a730:	ff 
   18001a731:	48 8d 05 e8 09 08 00 	lea    0x809e8(%rip),%rax        # 0x18009b120
   18001a738:	48 89 43 10          	mov    %rax,0x10(%rbx)
```

### Line 29923 (Address `0x180074088`)
```assembly
   18001b359:	49 89 7e 50          	mov    %rdi,0x50(%r14)
   18001b35d:	49 8d 4e 58          	lea    0x58(%r14),%rcx
   18001b361:	ff 15 69 8d 05 00    	call   *0x58d69(%rip)        # 0x1800740d0
   18001b367:	90                   	nop
   18001b368:	49 89 5e 50          	mov    %rbx,0x50(%r14)
   18001b36c:	48 8d 05 1d fd 07 00 	lea    0x7fd1d(%rip),%rax        # 0x18009b090
   18001b373:	49 89 06             	mov    %rax,(%r14)
   18001b376:	49 8b 4e 08          	mov    0x8(%r14),%rcx
   18001b37a:	48 8b 5c 24 50       	mov    0x50(%rsp),%rbx
   18001b37f:	48 8b 6c 24 58       	mov    0x58(%rsp),%rbp
   18001b384:	48 8b 74 24 60       	mov    0x60(%rsp),%rsi
   18001b389:	48 83 c4 30          	add    $0x30,%rsp
   18001b38d:	41 5f                	pop    %r15
   18001b38f:	41 5e                	pop    %r14
   18001b391:	5f                   	pop    %rdi
   18001b392:	48 ff 25 ef 8c 05 00 	rex.W jmp *0x58cef(%rip)        # 0x180074088
   18001b399:	cc                   	int3
   18001b39a:	cc                   	int3
   18001b39b:	cc                   	int3
   18001b39c:	cc                   	int3
```

### Line 96994 (Address `0x180074088`)
```assembly
   180055173:	b9 07 00 00 00       	mov    $0x7,%ecx
   180055178:	e8 13 0a 00 00       	call   0x180055b90
   18005517d:	90                   	nop
   18005517e:	b9 07 00 00 00       	mov    $0x7,%ecx
   180055183:	e8 08 0a 00 00       	call   0x180055b90
   180055188:	90                   	nop
   180055189:	cc                   	int3
   18005518a:	cc                   	int3
   18005518b:	cc                   	int3
   18005518c:	48 83 ec 28          	sub    $0x28,%rsp
   180055190:	48 8d 0d c1 21 05 00 	lea    0x521c1(%rip),%rcx        # 0x1800a7358
   180055197:	ff 15 33 ef 01 00    	call   *0x1ef33(%rip)        # 0x1800740d0
   18005519d:	48 8b 0d e4 21 05 00 	mov    0x521e4(%rip),%rcx        # 0x1800a7388
   1800551a4:	48 85 c9             	test   %rcx,%rcx
   1800551a7:	74 06                	je     0x1800551af
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
   1800551af:	48 83 c4 28          	add    $0x28,%rsp
   1800551b3:	c3                   	ret
   1800551b4:	40 53                	rex push %rbx
   1800551b6:	48 83 ec 20          	sub    $0x20,%rsp
```

### Line 121904 (Address `0x180074088`)
```assembly
   180069dc3:	40 84 b8 c8 00 00 00 	test   %dil,0xc8(%rax)
   180069dca:	75 0d                	jne    0x180069dd9
   180069dcc:	3b f9                	cmp    %ecx,%edi
   180069dce:	75 20                	jne    0x180069df0
   180069dd0:	f6 80 80 00 00 00 01 	testb  $0x1,0x80(%rax)
   180069dd7:	74 17                	je     0x180069df0
   180069dd9:	e8 06 5c 00 00       	call   0x18006f9e4
   180069dde:	b9 01 00 00 00       	mov    $0x1,%ecx
   180069de3:	48 8b d8             	mov    %rax,%rbx
   180069de6:	e8 f9 5b 00 00       	call   0x18006f9e4
   180069deb:	48 3b c3             	cmp    %rbx,%rax
   180069dee:	74 be                	je     0x180069dae
   180069df0:	8b cf                	mov    %edi,%ecx
   180069df2:	e8 ed 5b 00 00       	call   0x18006f9e4
   180069df7:	48 8b c8             	mov    %rax,%rcx
   180069dfa:	ff 15 88 a2 00 00    	call   *0xa288(%rip)        # 0x180074088
   180069e00:	85 c0                	test   %eax,%eax
   180069e02:	75 aa                	jne    0x180069dae
   180069e04:	ff 15 fe a2 00 00    	call   *0xa2fe(%rip)        # 0x180074108
   180069e0a:	8b d8                	mov    %eax,%ebx
```

### Line 130889 (Address `0x180074088`)
```assembly
   1800719dd:	ba 00 00 00 40       	mov    $0x40000000,%edx
   1800719e2:	ff 15 18 27 00 00    	call   *0x2718(%rip)        # 0x180074100
   1800719e8:	48 89 05 71 53 03 00 	mov    %rax,0x35371(%rip)        # 0x1800a6d60
   1800719ef:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   1800719f3:	0f 95 c3             	setne  %bl
   1800719f6:	8b c3                	mov    %ebx,%eax
   1800719f8:	48 83 c4 40          	add    $0x40,%rsp
   1800719fc:	5b                   	pop    %rbx
   1800719fd:	c3                   	ret
   1800719fe:	cc                   	int3
   1800719ff:	cc                   	int3
   180071a00:	48 83 ec 28          	sub    $0x28,%rsp
   180071a04:	48 8b 0d 55 53 03 00 	mov    0x35355(%rip),%rcx        # 0x1800a6d60
   180071a0b:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
   180071a0f:	77 06                	ja     0x180071a17
   180071a11:	ff 15 71 26 00 00    	call   *0x2671(%rip)        # 0x180074088
   180071a17:	48 83 c4 28          	add    $0x28,%rsp
   180071a1b:	c3                   	ret
   180071a1c:	48 8b c4             	mov    %rsp,%rax
   180071a1f:	48 89 58 08          	mov    %rbx,0x8(%rax)
```

### Line 130916 (Address `0x180074088`)
```assembly
   180071a3b:	8b f2                	mov    %edx,%esi
   180071a3d:	44 8b c2             	mov    %edx,%r8d
   180071a40:	48 8b e9             	mov    %rcx,%rbp
   180071a43:	48 8b d1             	mov    %rcx,%rdx
   180071a46:	48 8b 0d 13 53 03 00 	mov    0x35313(%rip),%rcx        # 0x1800a6d60
   180071a4d:	ff 15 4d 28 00 00    	call   *0x284d(%rip)        # 0x1800742a0
   180071a53:	8b d8                	mov    %eax,%ebx
   180071a55:	85 c0                	test   %eax,%eax
   180071a57:	75 6a                	jne    0x180071ac3
   180071a59:	ff 15 a9 26 00 00    	call   *0x26a9(%rip)        # 0x180074108
   180071a5f:	83 f8 06             	cmp    $0x6,%eax
   180071a62:	75 5f                	jne    0x180071ac3
   180071a64:	48 8b 0d f5 52 03 00 	mov    0x352f5(%rip),%rcx        # 0x1800a6d60
   180071a6b:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
   180071a6f:	77 06                	ja     0x180071a77
   180071a71:	ff 15 11 26 00 00    	call   *0x2611(%rip)        # 0x180074088
   180071a77:	48 83 64 24 30 00    	andq   $0x0,0x30(%rsp)
   180071a7d:	48 8d 0d 9c 75 02 00 	lea    0x2759c(%rip),%rcx        # 0x180099020
   180071a84:	83 64 24 28 00       	andl   $0x0,0x28(%rsp)
   180071a89:	41 b8 03 00 00 00    	mov    $0x3,%r8d
```

## `KERNEL32.dll!CompareStringW` (1 Call Sites)

### Line 122395 (Address `0x1800742c0`)
```assembly
   18006a45a:	48 8b cd             	mov    %rbp,%rcx
   18006a45d:	ff 15 0d 9f 00 00    	call   *0x9f0d(%rip)        # 0x180074370
   18006a463:	eb 32                	jmp    0x18006a497
   18006a465:	33 d2                	xor    %edx,%edx
   18006a467:	48 8b cd             	mov    %rbp,%rcx
   18006a46a:	e8 a9 02 00 00       	call   0x18006a718
   18006a46f:	8b c8                	mov    %eax,%ecx
   18006a471:	44 8b cb             	mov    %ebx,%r9d
   18006a474:	8b 84 24 88 00 00 00 	mov    0x88(%rsp),%eax
   18006a47b:	4c 8b c7             	mov    %rdi,%r8
   18006a47e:	89 44 24 28          	mov    %eax,0x28(%rsp)
   18006a482:	8b d6                	mov    %esi,%edx
   18006a484:	48 8b 84 24 80 00 00 	mov    0x80(%rsp),%rax
   18006a48b:	00 
   18006a48c:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18006a491:	ff 15 29 9e 00 00    	call   *0x9e29(%rip)        # 0x1800742c0
   18006a497:	48 8b 5c 24 60       	mov    0x60(%rsp),%rbx
   18006a49c:	48 8b 6c 24 68       	mov    0x68(%rsp),%rbp
   18006a4a1:	48 8b 74 24 70       	mov    0x70(%rsp),%rsi
   18006a4a6:	48 83 c4 50          	add    $0x50,%rsp
```

## `KERNEL32.dll!CreateDirectoryW` (1 Call Sites)

### Line 37813 (Address `0x180074178`)
```assembly
   1800226e9:	48 8b 5e 50          	mov    0x50(%rsi),%rbx
   1800226ed:	48 8d 8c 24 18 02 00 	lea    0x218(%rsp),%rcx
   1800226f4:	00 
   1800226f5:	e8 56 77 ff ff       	call   0x180019e50
   1800226fa:	90                   	nop
   1800226fb:	48 8b d3             	mov    %rbx,%rdx
   1800226fe:	48 8d 8c 24 18 02 00 	lea    0x218(%rsp),%rcx
   180022705:	00 
   180022706:	48 8b 84 24 18 02 00 	mov    0x218(%rsp),%rax
   18002270d:	00 
   18002270e:	ff 50 08             	call   *0x8(%rax)
   180022711:	90                   	nop
   180022712:	33 d2                	xor    %edx,%edx
   180022714:	48 8b 8c 24 20 02 00 	mov    0x220(%rsp),%rcx
   18002271b:	00 
   18002271c:	ff 15 56 1a 05 00    	call   *0x51a56(%rip)        # 0x180074178
   180022722:	4c 89 a4 24 18 02 00 	mov    %r12,0x218(%rsp)
   180022729:	00 
   18002272a:	48 8b 8c 24 20 02 00 	mov    0x220(%rsp),%rcx
   180022731:	00 
```

## `KERNEL32.dll!CreateEventW` (1 Call Sites)

### Line 96970 (Address `0x1800741c0`)
```assembly
   180055124:	84 c0                	test   %al,%al
   180055126:	74 40                	je     0x180055168
   180055128:	48 8d 0d 5d 00 00 00 	lea    0x5d(%rip),%rcx        # 0x18005518c
   18005512f:	e8 e8 06 00 00       	call   0x18005581c
   180055134:	90                   	nop
   180055135:	33 c0                	xor    %eax,%eax
   180055137:	48 8b 5c 24 40       	mov    0x40(%rsp),%rbx
   18005513c:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180055141:	48 83 c4 30          	add    $0x30,%rsp
   180055145:	5f                   	pop    %rdi
   180055146:	c3                   	ret
   180055147:	45 33 c9             	xor    %r9d,%r9d
   18005514a:	45 33 c0             	xor    %r8d,%r8d
   18005514d:	41 8d 51 01          	lea    0x1(%r9),%edx
   180055151:	33 c9                	xor    %ecx,%ecx
   180055153:	ff 15 67 f0 01 00    	call   *0x1f067(%rip)        # 0x1800741c0
   180055159:	90                   	nop
   18005515a:	48 89 05 27 22 05 00 	mov    %rax,0x52227(%rip)        # 0x1800a7388
   180055161:	48 85 c0             	test   %rax,%rax
   180055164:	74 0d                	je     0x180055173
```

## `KERNEL32.dll!CreateFileW` (7 Call Sites)

### Line 25184 (Address `0x180074100`)
```assembly
   180017105:	e8 46 2d 00 00       	call   0x180019e50
   18001710a:	90                   	nop
   18001710b:	48 8b 46 10          	mov    0x10(%rsi),%rax
   18001710f:	49 8b d6             	mov    %r14,%rdx
   180017112:	48 8d 4e 10          	lea    0x10(%rsi),%rcx
   180017116:	ff 50 08             	call   *0x8(%rax)
   180017119:	48 89 7c 24 30       	mov    %rdi,0x30(%rsp)
   18001711e:	c7 44 24 28 80 00 00 	movl   $0x80,0x28(%rsp)
   180017125:	00 
   180017126:	c7 44 24 20 03 00 00 	movl   $0x3,0x20(%rsp)
   18001712d:	00 
   18001712e:	45 33 c9             	xor    %r9d,%r9d
   180017131:	ba 00 00 00 80       	mov    $0x80000000,%edx
   180017136:	45 8d 41 01          	lea    0x1(%r9),%r8d
   18001713a:	48 8b 4e 18          	mov    0x18(%rsi),%rcx
   18001713e:	ff 15 bc cf 05 00    	call   *0x5cfbc(%rip)        # 0x180074100
   180017144:	48 89 46 08          	mov    %rax,0x8(%rsi)
   180017148:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18001714c:	0f 84 61 02 00 00    	je     0x1800173b3
   180017152:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
```

### Line 27722 (Address `0x180074100`)
```assembly
   1800195a9:	48 8d 15 a0 2f 08 00 	lea    0x82fa0(%rip),%rdx        # 0x18009c550
   1800195b0:	e8 db cc ff ff       	call   0x180016290
   1800195b5:	bb fe ff ff ff       	mov    $0xfffffffe,%ebx
   1800195ba:	eb 5e                	jmp    0x18001961a
   1800195bc:	33 f6                	xor    %esi,%esi
   1800195be:	48 8d 8c 24 70 02 00 	lea    0x270(%rsp),%rcx
   1800195c5:	00 
   1800195c6:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
   1800195cb:	45 33 c9             	xor    %r9d,%r9d
   1800195ce:	c7 44 24 28 20 00 00 	movl   $0x20,0x28(%rsp)
   1800195d5:	00 
   1800195d6:	ba 00 00 00 10       	mov    $0x10000000,%edx
   1800195db:	c7 44 24 20 01 00 00 	movl   $0x1,0x20(%rsp)
   1800195e2:	00 
   1800195e3:	44 8d 46 03          	lea    0x3(%rsi),%r8d
   1800195e7:	ff 15 13 ab 05 00    	call   *0x5ab13(%rip)        # 0x180074100
   1800195ed:	48 89 05 9c d7 08 00 	mov    %rax,0x8d79c(%rip)        # 0x1800a6d90
   1800195f4:	48 3b c3             	cmp    %rbx,%rax
   1800195f7:	75 3c                	jne    0x180019635
   1800195f9:	ff 15 09 ab 05 00    	call   *0x5ab09(%rip)        # 0x180074108
```

### Line 37869 (Address `0x180074100`)
```assembly
   1800227c3:	e8 88 76 ff ff       	call   0x180019e50
   1800227c8:	90                   	nop
   1800227c9:	49 8b 47 10          	mov    0x10(%r15),%rax
   1800227cd:	48 8b d7             	mov    %rdi,%rdx
   1800227d0:	49 8d 4f 10          	lea    0x10(%r15),%rcx
   1800227d4:	ff 50 08             	call   *0x8(%rax)
   1800227d7:	4c 89 74 24 30       	mov    %r14,0x30(%rsp)
   1800227dc:	c7 44 24 28 80 00 00 	movl   $0x80,0x28(%rsp)
   1800227e3:	00 
   1800227e4:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   1800227eb:	00 
   1800227ec:	45 33 c9             	xor    %r9d,%r9d
   1800227ef:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   1800227f4:	45 8d 41 01          	lea    0x1(%r9),%r8d
   1800227f8:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   1800227fc:	ff 15 fe 18 05 00    	call   *0x518fe(%rip)        # 0x180074100
   180022802:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022806:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18002280a:	0f 84 78 03 00 00    	je     0x180022b88
   180022810:	41 b9 02 00 00 00    	mov    $0x2,%r9d
```

### Line 37930 (Address `0x180074100`)
```assembly
   1800228bc:	e8 8f 75 ff ff       	call   0x180019e50
   1800228c1:	90                   	nop
   1800228c2:	49 8b 47 10          	mov    0x10(%r15),%rax
   1800228c6:	48 8b d7             	mov    %rdi,%rdx
   1800228c9:	49 8d 4f 10          	lea    0x10(%r15),%rcx
   1800228cd:	ff 50 08             	call   *0x8(%rax)
   1800228d0:	4c 89 74 24 30       	mov    %r14,0x30(%rsp)
   1800228d5:	c7 44 24 28 80 00 00 	movl   $0x80,0x28(%rsp)
   1800228dc:	00 
   1800228dd:	c7 44 24 20 02 00 00 	movl   $0x2,0x20(%rsp)
   1800228e4:	00 
   1800228e5:	45 33 c9             	xor    %r9d,%r9d
   1800228e8:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   1800228ed:	45 8d 41 01          	lea    0x1(%r9),%r8d
   1800228f1:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   1800228f5:	ff 15 05 18 05 00    	call   *0x51805(%rip)        # 0x180074100
   1800228fb:	49 89 47 08          	mov    %rax,0x8(%r15)
   1800228ff:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   180022903:	0f 84 bf 02 00 00    	je     0x180022bc8
   180022909:	4c 89 be 90 00 00 00 	mov    %r15,0x90(%rsi)
```

### Line 38053 (Address `0x180074100`)
```assembly
   180022a88:	e8 c3 73 ff ff       	call   0x180019e50
   180022a8d:	90                   	nop
   180022a8e:	49 8b 47 10          	mov    0x10(%r15),%rax
   180022a92:	48 8b d7             	mov    %rdi,%rdx
   180022a95:	49 8d 4f 10          	lea    0x10(%r15),%rcx
   180022a99:	ff 50 08             	call   *0x8(%rax)
   180022a9c:	4c 89 74 24 30       	mov    %r14,0x30(%rsp)
   180022aa1:	c7 44 24 28 80 00 00 	movl   $0x80,0x28(%rsp)
   180022aa8:	00 
   180022aa9:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   180022ab0:	00 
   180022ab1:	45 33 c9             	xor    %r9d,%r9d
   180022ab4:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   180022ab9:	45 8d 41 01          	lea    0x1(%r9),%r8d
   180022abd:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   180022ac1:	ff 15 39 16 05 00    	call   *0x51639(%rip)        # 0x180074100
   180022ac7:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022acb:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   180022acf:	0f 84 15 01 00 00    	je     0x180022bea
   180022ad5:	41 b9 02 00 00 00    	mov    $0x2,%r9d
```

### Line 130875 (Address `0x180074100`)
```assembly
   1800719aa:	c3                   	ret
   1800719ab:	cc                   	int3
   1800719ac:	40 53                	rex push %rbx
   1800719ae:	48 83 ec 40          	sub    $0x40,%rsp
   1800719b2:	48 8b 05 a7 53 03 00 	mov    0x353a7(%rip),%rax        # 0x1800a6d60
   1800719b9:	33 db                	xor    %ebx,%ebx
   1800719bb:	48 83 f8 fe          	cmp    $0xfffffffffffffffe,%rax
   1800719bf:	75 2e                	jne    0x1800719ef
   1800719c1:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   1800719c6:	44 8d 43 03          	lea    0x3(%rbx),%r8d
   1800719ca:	89 5c 24 28          	mov    %ebx,0x28(%rsp)
   1800719ce:	48 8d 0d 4b 76 02 00 	lea    0x2764b(%rip),%rcx        # 0x180099020
   1800719d5:	45 33 c9             	xor    %r9d,%r9d
   1800719d8:	44 89 44 24 20       	mov    %r8d,0x20(%rsp)
   1800719dd:	ba 00 00 00 40       	mov    $0x40000000,%edx
   1800719e2:	ff 15 18 27 00 00    	call   *0x2718(%rip)        # 0x180074100
   1800719e8:	48 89 05 71 53 03 00 	mov    %rax,0x35371(%rip)        # 0x1800a6d60
   1800719ef:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   1800719f3:	0f 95 c3             	setne  %bl
   1800719f6:	8b c3                	mov    %ebx,%eax
```

### Line 130924 (Address `0x180074100`)
```assembly
   180071a57:	75 6a                	jne    0x180071ac3
   180071a59:	ff 15 a9 26 00 00    	call   *0x26a9(%rip)        # 0x180074108
   180071a5f:	83 f8 06             	cmp    $0x6,%eax
   180071a62:	75 5f                	jne    0x180071ac3
   180071a64:	48 8b 0d f5 52 03 00 	mov    0x352f5(%rip),%rcx        # 0x1800a6d60
   180071a6b:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
   180071a6f:	77 06                	ja     0x180071a77
   180071a71:	ff 15 11 26 00 00    	call   *0x2611(%rip)        # 0x180074088
   180071a77:	48 83 64 24 30 00    	andq   $0x0,0x30(%rsp)
   180071a7d:	48 8d 0d 9c 75 02 00 	lea    0x2759c(%rip),%rcx        # 0x180099020
   180071a84:	83 64 24 28 00       	andl   $0x0,0x28(%rsp)
   180071a89:	41 b8 03 00 00 00    	mov    $0x3,%r8d
   180071a8f:	45 33 c9             	xor    %r9d,%r9d
   180071a92:	44 89 44 24 20       	mov    %r8d,0x20(%rsp)
   180071a97:	ba 00 00 00 40       	mov    $0x40000000,%edx
   180071a9c:	ff 15 5e 26 00 00    	call   *0x265e(%rip)        # 0x180074100
   180071aa2:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   180071aa8:	4c 8b cf             	mov    %rdi,%r9
   180071aab:	48 8b c8             	mov    %rax,%rcx
   180071aae:	48 89 05 ab 52 03 00 	mov    %rax,0x352ab(%rip)        # 0x1800a6d60
```

## `KERNEL32.dll!CreateThread` (2 Call Sites)

### Line 23443 (Address `0x180074090`)
```assembly
   18001591b:	41 b8 98 04 00 00    	mov    $0x498,%r8d
   180015921:	48 8b c8             	mov    %rax,%rcx
   180015924:	4c 8b f0             	mov    %rax,%r14
   180015927:	e8 04 15 04 00       	call   0x180056e30
   18001592c:	49 8d 4e 10          	lea    0x10(%r14),%rcx
   180015930:	4d 8b ce             	mov    %r14,%r9
   180015933:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   180015938:	48 8d 05 51 57 08 00 	lea    0x85751(%rip),%rax        # 0x18009b090
   18001593f:	49 89 06             	mov    %rax,(%r14)
   180015942:	4c 8d 05 97 44 00 00 	lea    0x4497(%rip),%r8        # 0x180019de0
   180015949:	33 c9                	xor    %ecx,%ecx
   18001594b:	41 c6 46 15 00       	movb   $0x0,0x15(%r14)
   180015950:	33 d2                	xor    %edx,%edx
   180015952:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   180015959:	00 
   18001595a:	ff 15 30 e7 05 00    	call   *0x5e730(%rip)        # 0x180074090
   180015960:	41 89 5e 1c          	mov    %ebx,0x1c(%r14)
   180015964:	49 8d 8e 18 02 00 00 	lea    0x218(%r14),%rcx
   18001596b:	49 89 46 08          	mov    %rax,0x8(%r14)
   18001596f:	48 8d 1d d2 57 08 00 	lea    0x857d2(%rip),%rbx        # 0x18009b148
```

### Line 29580 (Address `0x180074090`)
```assembly
   18001adf9:	4d 8b f0             	mov    %r8,%r14
   18001adfc:	8b da                	mov    %edx,%ebx
   18001adfe:	48 8b f1             	mov    %rcx,%rsi
   18001ae01:	48 8d 05 88 02 08 00 	lea    0x80288(%rip),%rax        # 0x18009b090
   18001ae08:	48 89 01             	mov    %rax,(%rcx)
   18001ae0b:	c6 41 14 00          	movb   $0x0,0x14(%rcx)
   18001ae0f:	c6 41 15 00          	movb   $0x0,0x15(%rcx)
   18001ae13:	48 8d 41 10          	lea    0x10(%rcx),%rax
   18001ae17:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001ae1c:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   18001ae23:	00 
   18001ae24:	4c 8b c9             	mov    %rcx,%r9
   18001ae27:	4c 8d 05 b2 ef ff ff 	lea    -0x104e(%rip),%r8        # 0x180019de0
   18001ae2e:	33 d2                	xor    %edx,%edx
   18001ae30:	33 c9                	xor    %ecx,%ecx
   18001ae32:	ff 15 58 92 05 00    	call   *0x59258(%rip)        # 0x180074090
   18001ae38:	48 89 46 08          	mov    %rax,0x8(%rsi)
   18001ae3c:	48 8d 05 ed 1a 08 00 	lea    0x81aed(%rip),%rax        # 0x18009c930
   18001ae43:	48 89 06             	mov    %rax,(%rsi)
   18001ae46:	45 33 ff             	xor    %r15d,%r15d
```

## `KERNEL32.dll!DeleteCriticalSection` (17 Call Sites)

### Line 23685 (Address `0x1800740d0`)
```assembly
   180015cea:	4c 8d 3d 77 54 08 00 	lea    0x85477(%rip),%r15        # 0x18009b168
   180015cf1:	48 8b f9             	mov    %rcx,%rdi
   180015cf4:	48 85 f6             	test   %rsi,%rsi
   180015cf7:	74 4a                	je     0x180015d43
   180015cf9:	4c 8b 4e 30          	mov    0x30(%rsi),%r9
   180015cfd:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180015d02:	48 8d 4e 30          	lea    0x30(%rsi),%rcx
   180015d06:	48 89 5c 24 58       	mov    %rbx,0x58(%rsp)
   180015d0b:	4d 8b 01             	mov    (%r9),%r8
   180015d0e:	e8 5d 09 00 00       	call   0x180016670
   180015d13:	48 8b 4e 30          	mov    0x30(%rsi),%rcx
   180015d17:	ba 40 00 00 00       	mov    $0x40,%edx
   180015d1c:	e8 cf f2 03 00       	call   0x180054ff0
   180015d21:	48 8d 4e 08          	lea    0x8(%rsi),%rcx
   180015d25:	4c 89 36             	mov    %r14,(%rsi)
   180015d28:	ff 15 a2 e3 05 00    	call   *0x5e3a2(%rip)        # 0x1800740d0
   180015d2e:	ba 70 00 00 00       	mov    $0x70,%edx
   180015d33:	4c 89 3e             	mov    %r15,(%rsi)
   180015d36:	48 8b ce             	mov    %rsi,%rcx
   180015d39:	e8 b2 f2 03 00       	call   0x180054ff0
```

### Line 23717 (Address `0x1800740d0`)
```assembly
   180015d70:	72 18                	jb     0x180015d8a
   180015d72:	4c 8b 41 f8          	mov    -0x8(%rcx),%r8
   180015d76:	48 83 c2 27          	add    $0x27,%rdx
   180015d7a:	49 2b c8             	sub    %r8,%rcx
   180015d7d:	48 8d 41 f8          	lea    -0x8(%rcx),%rax
   180015d81:	48 83 f8 1f          	cmp    $0x1f,%rax
   180015d85:	77 4d                	ja     0x180015dd4
   180015d87:	49 8b c8             	mov    %r8,%rcx
   180015d8a:	e8 61 f2 03 00       	call   0x180054ff0
   180015d8f:	33 c0                	xor    %eax,%eax
   180015d91:	48 89 47 48          	mov    %rax,0x48(%rdi)
   180015d95:	48 89 47 50          	mov    %rax,0x50(%rdi)
   180015d99:	48 89 47 58          	mov    %rax,0x58(%rdi)
   180015d9d:	48 8d 4f 18          	lea    0x18(%rdi),%rcx
   180015da1:	4c 89 77 10          	mov    %r14,0x10(%rdi)
   180015da5:	ff 15 25 e3 05 00    	call   *0x5e325(%rip)        # 0x1800740d0
   180015dab:	4c 89 7f 10          	mov    %r15,0x10(%rdi)
   180015daf:	40 f6 c5 01          	test   $0x1,%bpl
   180015db3:	74 0d                	je     0x180015dc2
   180015db5:	ba 70 00 00 00       	mov    $0x70,%edx
```

### Line 26649 (Address `0x1800740d0`)
```assembly
   1800184fb:	00 00 00 00 
   1800184ff:	48 c7 05 1e 01 09 00 	movq   $0x0,0x9011e(%rip)        # 0x1800a8628
   180018506:	00 00 00 00 
   18001850a:	c6 86 f9 03 00 00 00 	movb   $0x0,0x3f9(%rsi)
   180018511:	49 8b 04 24          	mov    (%r12),%rax
   180018515:	49 8b cc             	mov    %r12,%rcx
   180018518:	ff 50 10             	call   *0x10(%rax)
   18001851b:	90                   	nop
   18001851c:	48 8d 15 45 27 08 00 	lea    0x82745(%rip),%rdx        # 0x18009ac68
   180018523:	48 8b 0d de 00 09 00 	mov    0x900de(%rip),%rcx        # 0x1800a8608
   18001852a:	e8 61 dd ff ff       	call   0x180016290
   18001852f:	90                   	nop
   180018530:	48 8d 3d 11 2c 08 00 	lea    0x82c11(%rip),%rdi        # 0x18009b148
   180018537:	49 89 3c 24          	mov    %rdi,(%r12)
   18001853b:	49 8d 4c 24 08       	lea    0x8(%r12),%rcx
   180018540:	ff 15 8a bb 05 00    	call   *0x5bb8a(%rip)        # 0x1800740d0
   180018546:	90                   	nop
   180018547:	48 8d 1d 1a 2c 08 00 	lea    0x82c1a(%rip),%rbx        # 0x18009b168
   18001854e:	49 89 1c 24          	mov    %rbx,(%r12)
   180018552:	49 89 3f             	mov    %rdi,(%r15)
```

### Line 26655 (Address `0x1800740d0`)
```assembly
   180018518:	ff 50 10             	call   *0x10(%rax)
   18001851b:	90                   	nop
   18001851c:	48 8d 15 45 27 08 00 	lea    0x82745(%rip),%rdx        # 0x18009ac68
   180018523:	48 8b 0d de 00 09 00 	mov    0x900de(%rip),%rcx        # 0x1800a8608
   18001852a:	e8 61 dd ff ff       	call   0x180016290
   18001852f:	90                   	nop
   180018530:	48 8d 3d 11 2c 08 00 	lea    0x82c11(%rip),%rdi        # 0x18009b148
   180018537:	49 89 3c 24          	mov    %rdi,(%r12)
   18001853b:	49 8d 4c 24 08       	lea    0x8(%r12),%rcx
   180018540:	ff 15 8a bb 05 00    	call   *0x5bb8a(%rip)        # 0x1800740d0
   180018546:	90                   	nop
   180018547:	48 8d 1d 1a 2c 08 00 	lea    0x82c1a(%rip),%rbx        # 0x18009b168
   18001854e:	49 89 1c 24          	mov    %rbx,(%r12)
   180018552:	49 89 3f             	mov    %rdi,(%r15)
   180018555:	49 8d 4f 08          	lea    0x8(%r15),%rcx
   180018559:	ff 15 71 bb 05 00    	call   *0x5bb71(%rip)        # 0x1800740d0
   18001855f:	90                   	nop
   180018560:	49 89 1f             	mov    %rbx,(%r15)
   180018563:	48 8d 05 26 2b 08 00 	lea    0x82b26(%rip),%rax        # 0x18009b090
   18001856a:	48 89 06             	mov    %rax,(%rsi)
```

### Line 28912 (Address `0x1800740d0`)
```assembly
   18001a519:	5b                   	pop    %rbx
   18001a51a:	c3                   	ret
   18001a51b:	cc                   	int3
   18001a51c:	cc                   	int3
   18001a51d:	cc                   	int3
   18001a51e:	cc                   	int3
   18001a51f:	cc                   	int3
   18001a520:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18001a525:	57                   	push   %rdi
   18001a526:	48 83 ec 20          	sub    $0x20,%rsp
   18001a52a:	48 8d 05 17 0c 08 00 	lea    0x80c17(%rip),%rax        # 0x18009b148
   18001a531:	48 8b f9             	mov    %rcx,%rdi
   18001a534:	48 89 01             	mov    %rax,(%rcx)
   18001a537:	8b da                	mov    %edx,%ebx
   18001a539:	48 83 c1 08          	add    $0x8,%rcx
   18001a53d:	ff 15 8d 9b 05 00    	call   *0x59b8d(%rip)        # 0x1800740d0
   18001a543:	48 8d 05 1e 0c 08 00 	lea    0x80c1e(%rip),%rax        # 0x18009b168
   18001a54a:	48 89 07             	mov    %rax,(%rdi)
   18001a54d:	f6 c3 01             	test   $0x1,%bl
   18001a550:	74 0d                	je     0x18001a55f
```

### Line 28934 (Address `0x1800740d0`)
```assembly
   18001a55a:	e8 91 aa 03 00       	call   0x180054ff0
   18001a55f:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18001a564:	48 8b c7             	mov    %rdi,%rax
   18001a567:	48 83 c4 20          	add    $0x20,%rsp
   18001a56b:	5f                   	pop    %rdi
   18001a56c:	c3                   	ret
   18001a56d:	cc                   	int3
   18001a56e:	cc                   	int3
   18001a56f:	cc                   	int3
   18001a570:	40 53                	rex push %rbx
   18001a572:	48 83 ec 20          	sub    $0x20,%rsp
   18001a576:	48 8d 05 cb 0b 08 00 	lea    0x80bcb(%rip),%rax        # 0x18009b148
   18001a57d:	48 8b d9             	mov    %rcx,%rbx
   18001a580:	48 89 01             	mov    %rax,(%rcx)
   18001a583:	48 83 c1 08          	add    $0x8,%rcx
   18001a587:	ff 15 43 9b 05 00    	call   *0x59b43(%rip)        # 0x1800740d0
   18001a58d:	48 8d 05 d4 0b 08 00 	lea    0x80bd4(%rip),%rax        # 0x18009b168
   18001a594:	48 89 03             	mov    %rax,(%rbx)
   18001a597:	48 83 c4 20          	add    $0x20,%rsp
   18001a59b:	5b                   	pop    %rbx
```

### Line 29792 (Address `0x1800740d0`)
```assembly
   18001b177:	cc                   	int3
   18001b178:	cc                   	int3
   18001b179:	cc                   	int3
   18001b17a:	cc                   	int3
   18001b17b:	cc                   	int3
   18001b17c:	cc                   	int3
   18001b17d:	cc                   	int3
   18001b17e:	cc                   	int3
   18001b17f:	cc                   	int3
   18001b180:	40 53                	rex push %rbx
   18001b182:	48 83 ec 20          	sub    $0x20,%rsp
   18001b186:	48 8d 05 bb ff 07 00 	lea    0x7ffbb(%rip),%rax        # 0x18009b148
   18001b18d:	48 8b d9             	mov    %rcx,%rbx
   18001b190:	48 89 41 48          	mov    %rax,0x48(%rcx)
   18001b194:	48 83 c1 50          	add    $0x50,%rcx
   18001b198:	ff 15 32 8f 05 00    	call   *0x58f32(%rip)        # 0x1800740d0
   18001b19e:	48 8d 05 c3 ff 07 00 	lea    0x7ffc3(%rip),%rax        # 0x18009b168
   18001b1a5:	48 89 43 48          	mov    %rax,0x48(%rbx)
   18001b1a9:	48 83 c4 20          	add    $0x20,%rsp
   18001b1ad:	5b                   	pop    %rbx
```

### Line 29904 (Address `0x1800740d0`)
```assembly
   18001b30a:	75 b7                	jne    0x18001b2c3
   18001b30c:	8b c6                	mov    %esi,%eax
   18001b30e:	41 87 86 b0 01 00 00 	xchg   %eax,0x1b0(%r14)
   18001b315:	41 87 b6 b4 01 00 00 	xchg   %esi,0x1b4(%r14)
   18001b31c:	49 8b 07             	mov    (%r15),%rax
   18001b31f:	49 8b cf             	mov    %r15,%rcx
   18001b322:	ff 50 10             	call   *0x10(%rax)
   18001b325:	90                   	nop
   18001b326:	48 8d 15 8b 16 08 00 	lea    0x8168b(%rip),%rdx        # 0x18009c9b8
   18001b32d:	48 8b 0d d4 d2 08 00 	mov    0x8d2d4(%rip),%rcx        # 0x1800a8608
   18001b334:	e8 57 af ff ff       	call   0x180016290
   18001b339:	90                   	nop
   18001b33a:	48 8d 3d 07 fe 07 00 	lea    0x7fe07(%rip),%rdi        # 0x18009b148
   18001b341:	49 89 3f             	mov    %rdi,(%r15)
   18001b344:	49 8d 4f 08          	lea    0x8(%r15),%rcx
   18001b348:	ff 15 82 8d 05 00    	call   *0x58d82(%rip)        # 0x1800740d0
   18001b34e:	90                   	nop
   18001b34f:	48 8d 1d 12 fe 07 00 	lea    0x7fe12(%rip),%rbx        # 0x18009b168
   18001b356:	49 89 1f             	mov    %rbx,(%r15)
   18001b359:	49 89 7e 50          	mov    %rdi,0x50(%r14)
```

### Line 29910 (Address `0x1800740d0`)
```assembly
   18001b322:	ff 50 10             	call   *0x10(%rax)
   18001b325:	90                   	nop
   18001b326:	48 8d 15 8b 16 08 00 	lea    0x8168b(%rip),%rdx        # 0x18009c9b8
   18001b32d:	48 8b 0d d4 d2 08 00 	mov    0x8d2d4(%rip),%rcx        # 0x1800a8608
   18001b334:	e8 57 af ff ff       	call   0x180016290
   18001b339:	90                   	nop
   18001b33a:	48 8d 3d 07 fe 07 00 	lea    0x7fe07(%rip),%rdi        # 0x18009b148
   18001b341:	49 89 3f             	mov    %rdi,(%r15)
   18001b344:	49 8d 4f 08          	lea    0x8(%r15),%rcx
   18001b348:	ff 15 82 8d 05 00    	call   *0x58d82(%rip)        # 0x1800740d0
   18001b34e:	90                   	nop
   18001b34f:	48 8d 1d 12 fe 07 00 	lea    0x7fe12(%rip),%rbx        # 0x18009b168
   18001b356:	49 89 1f             	mov    %rbx,(%r15)
   18001b359:	49 89 7e 50          	mov    %rdi,0x50(%r14)
   18001b35d:	49 8d 4e 58          	lea    0x58(%r14),%rcx
   18001b361:	ff 15 69 8d 05 00    	call   *0x58d69(%rip)        # 0x1800740d0
   18001b367:	90                   	nop
   18001b368:	49 89 5e 50          	mov    %rbx,0x50(%r14)
   18001b36c:	48 8d 05 1d fd 07 00 	lea    0x7fd1d(%rip),%rax        # 0x18009b090
   18001b373:	49 89 06             	mov    %rax,(%r14)
```

### Line 36854 (Address `0x1800740d0`)
```assembly
   18002199b:	48 83 ec 20          	sub    $0x20,%rsp
   18002199f:	48 8d 05 62 c9 07 00 	lea    0x7c962(%rip),%rax        # 0x18009e308
   1800219a6:	48 8b d9             	mov    %rcx,%rbx
   1800219a9:	48 89 01             	mov    %rax,(%rcx)
   1800219ac:	33 ff                	xor    %edi,%edi
   1800219ae:	48 8b 89 90 00 00 00 	mov    0x90(%rcx),%rcx
   1800219b5:	48 85 c9             	test   %rcx,%rcx
   1800219b8:	74 0f                	je     0x1800219c9
   1800219ba:	48 8b 01             	mov    (%rcx),%rax
   1800219bd:	8d 57 01             	lea    0x1(%rdi),%edx
   1800219c0:	ff 10                	call   *(%rax)
   1800219c2:	48 89 bb 90 00 00 00 	mov    %rdi,0x90(%rbx)
   1800219c9:	48 8d 05 78 97 07 00 	lea    0x79778(%rip),%rax        # 0x18009b148
   1800219d0:	48 8d 8b a0 00 00 00 	lea    0xa0(%rbx),%rcx
   1800219d7:	48 89 83 98 00 00 00 	mov    %rax,0x98(%rbx)
   1800219de:	ff 15 ec 26 05 00    	call   *0x526ec(%rip)        # 0x1800740d0
   1800219e4:	48 8d 05 7d 97 07 00 	lea    0x7977d(%rip),%rax        # 0x18009b168
   1800219eb:	48 89 83 98 00 00 00 	mov    %rax,0x98(%rbx)
   1800219f2:	48 8d 35 27 97 07 00 	lea    0x79727(%rip),%rsi        # 0x18009b120
   1800219f9:	48 89 73 68          	mov    %rsi,0x68(%rbx)
```

### Line 96990 (Address `0x1800740d0`)
```assembly
   180055166:	eb b4                	jmp    0x18005511c
   180055168:	b9 07 00 00 00       	mov    $0x7,%ecx
   18005516d:	e8 1e 0a 00 00       	call   0x180055b90
   180055172:	90                   	nop
   180055173:	b9 07 00 00 00       	mov    $0x7,%ecx
   180055178:	e8 13 0a 00 00       	call   0x180055b90
   18005517d:	90                   	nop
   18005517e:	b9 07 00 00 00       	mov    $0x7,%ecx
   180055183:	e8 08 0a 00 00       	call   0x180055b90
   180055188:	90                   	nop
   180055189:	cc                   	int3
   18005518a:	cc                   	int3
   18005518b:	cc                   	int3
   18005518c:	48 83 ec 28          	sub    $0x28,%rsp
   180055190:	48 8d 0d c1 21 05 00 	lea    0x521c1(%rip),%rcx        # 0x1800a7358
   180055197:	ff 15 33 ef 01 00    	call   *0x1ef33(%rip)        # 0x1800740d0
   18005519d:	48 8b 0d e4 21 05 00 	mov    0x521e4(%rip),%rcx        # 0x1800a7388
   1800551a4:	48 85 c9             	test   %rcx,%rcx
   1800551a7:	74 06                	je     0x1800551af
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
```

### Line 98079 (Address `0x1800740d0`)
```assembly
   180056083:	48 8d 0d 26 c3 03 00 	lea    0x3c326(%rip),%rcx        # 0x1800923b0
   18005608a:	ff 15 d0 df 01 00    	call   *0x1dfd0(%rip)        # 0x180074060
   180056090:	c6 05 c9 26 05 00 01 	movb   $0x1,0x526c9(%rip)        # 0x1800a8760
   180056097:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18005609c:	48 8b c7             	mov    %rdi,%rax
   18005609f:	48 83 c4 20          	add    $0x20,%rsp
   1800560a3:	5f                   	pop    %rdi
   1800560a4:	c3                   	ret
   1800560a5:	cc                   	int3
   1800560a6:	cc                   	int3
   1800560a7:	cc                   	int3
   1800560a8:	40 53                	rex push %rbx
   1800560aa:	48 83 ec 20          	sub    $0x20,%rsp
   1800560ae:	48 8b d9             	mov    %rcx,%rbx
   1800560b1:	48 83 c1 28          	add    $0x28,%rcx
   1800560b5:	ff 15 15 e0 01 00    	call   *0x1e015(%rip)        # 0x1800740d0
   1800560bb:	48 8b 4b 50          	mov    0x50(%rbx),%rcx
   1800560bf:	48 85 c9             	test   %rcx,%rcx
   1800560c2:	74 0a                	je     0x1800560ce
   1800560c4:	e8 7b 8b 00 00       	call   0x18005ec44
```

### Line 101490 (Address `0x1800740d0`)
```assembly
   180058d1d:	e8 0a 00 00 00       	call   0x180058d2c
   180058d22:	32 c0                	xor    %al,%al
   180058d24:	48 83 c4 20          	add    $0x20,%rsp
   180058d28:	5b                   	pop    %rbx
   180058d29:	c3                   	ret
   180058d2a:	cc                   	int3
   180058d2b:	cc                   	int3
   180058d2c:	40 53                	rex push %rbx
   180058d2e:	48 83 ec 20          	sub    $0x20,%rsp
   180058d32:	8b 1d 78 ed 04 00    	mov    0x4ed78(%rip),%ebx        # 0x1800a7ab0
   180058d38:	eb 1d                	jmp    0x180058d57
   180058d3a:	48 8d 05 47 ed 04 00 	lea    0x4ed47(%rip),%rax        # 0x1800a7a88
   180058d41:	ff cb                	dec    %ebx
   180058d43:	48 8d 0c 9b          	lea    (%rbx,%rbx,4),%rcx
   180058d47:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   180058d4b:	ff 15 7f b3 01 00    	call   *0x1b37f(%rip)        # 0x1800740d0
   180058d51:	ff 0d 59 ed 04 00    	decl   0x4ed59(%rip)        # 0x1800a7ab0
   180058d57:	85 db                	test   %ebx,%ebx
   180058d59:	75 df                	jne    0x180058d3a
   180058d5b:	b0 01                	mov    $0x1,%al
```

### Line 109658 (Address `0x1800740d0`)
```assembly
   18005fabc:	c3                   	ret
   18005fabd:	cc                   	int3
   18005fabe:	cc                   	int3
   18005fabf:	cc                   	int3
   18005fac0:	40 53                	rex push %rbx
   18005fac2:	48 83 ec 20          	sub    $0x20,%rsp
   18005fac6:	e8 75 04 00 00       	call   0x18005ff40
   18005facb:	e8 34 af 00 00       	call   0x18006aa04
   18005fad0:	33 db                	xor    %ebx,%ebx
   18005fad2:	48 8b 0d af 80 04 00 	mov    0x480af(%rip),%rcx        # 0x1800a7b88
   18005fad9:	48 8b 0c 0b          	mov    (%rbx,%rcx,1),%rcx
   18005fadd:	e8 72 a3 00 00       	call   0x180069e54
   18005fae2:	48 8b 05 9f 80 04 00 	mov    0x4809f(%rip),%rax        # 0x1800a7b88
   18005fae9:	48 8b 0c 03          	mov    (%rbx,%rax,1),%rcx
   18005faed:	48 83 c1 30          	add    $0x30,%rcx
   18005faf1:	ff 15 d9 45 01 00    	call   *0x145d9(%rip)        # 0x1800740d0
   18005faf7:	48 83 c3 08          	add    $0x8,%rbx
   18005fafb:	48 83 fb 18          	cmp    $0x18,%rbx
   18005faff:	75 d1                	jne    0x18005fad2
   18005fb01:	48 8b 0d 80 80 04 00 	mov    0x48080(%rip),%rcx        # 0x1800a7b88
```

### Line 121472 (Address `0x1800740d0`)
```assembly
   1800697e3:	48 8d 0c 80          	lea    (%rax,%rax,4),%rcx
   1800697e7:	48 8d 05 72 e9 03 00 	lea    0x3e972(%rip),%rax        # 0x1800a8160
   1800697ee:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   1800697f2:	48 ff 25 bf a8 00 00 	rex.W jmp *0xa8bf(%rip)        # 0x1800740b8
   1800697f9:	cc                   	int3
   1800697fa:	cc                   	int3
   1800697fb:	cc                   	int3
   1800697fc:	40 53                	rex push %rbx
   1800697fe:	48 83 ec 20          	sub    $0x20,%rsp
   180069802:	8b 1d 88 eb 03 00    	mov    0x3eb88(%rip),%ebx        # 0x1800a8390
   180069808:	eb 1d                	jmp    0x180069827
   18006980a:	48 8d 05 4f e9 03 00 	lea    0x3e94f(%rip),%rax        # 0x1800a8160
   180069811:	ff cb                	dec    %ebx
   180069813:	48 8d 0c 9b          	lea    (%rbx,%rbx,4),%rcx
   180069817:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   18006981b:	ff 15 af a8 00 00    	call   *0xa8af(%rip)        # 0x1800740d0
   180069821:	ff 0d 69 eb 03 00    	decl   0x3eb69(%rip)        # 0x1800a8390
   180069827:	85 db                	test   %ebx,%ebx
   180069829:	75 df                	jne    0x18006980a
   18006982b:	b0 01                	mov    $0x1,%al
```

### Line 122798 (Address `0x1800740d0`)
```assembly
   18006aa40:	75 02                	jne    0x18006aa44
   18006aa42:	eb 54                	jmp    0x18006aa98
   18006aa44:	8b 41 14             	mov    0x14(%rcx),%eax
   18006aa47:	c1 e8 0d             	shr    $0xd,%eax
   18006aa4a:	a8 01                	test   $0x1,%al
   18006aa4c:	74 19                	je     0x18006aa67
   18006aa4e:	48 8b 0d 33 d1 03 00 	mov    0x3d133(%rip),%rcx        # 0x1800a7b88
   18006aa55:	48 8b 0c f9          	mov    (%rcx,%rdi,8),%rcx
   18006aa59:	e8 aa 4b ff ff       	call   0x18005f608
   18006aa5e:	83 f8 ff             	cmp    $0xffffffff,%eax
   18006aa61:	74 04                	je     0x18006aa67
   18006aa63:	ff 44 24 20          	incl   0x20(%rsp)
   18006aa67:	48 8b 05 1a d1 03 00 	mov    0x3d11a(%rip),%rax        # 0x1800a7b88
   18006aa6e:	48 8b 0c f8          	mov    (%rax,%rdi,8),%rcx
   18006aa72:	48 83 c1 30          	add    $0x30,%rcx
   18006aa76:	ff 15 54 96 00 00    	call   *0x9654(%rip)        # 0x1800740d0
   18006aa7c:	48 8b 0d 05 d1 03 00 	mov    0x3d105(%rip),%rcx        # 0x1800a7b88
   18006aa83:	48 8b 0c f9          	mov    (%rcx,%rdi,8),%rcx
   18006aa87:	e8 30 be ff ff       	call   0x1800668bc
   18006aa8c:	48 8b 05 f5 d0 03 00 	mov    0x3d0f5(%rip),%rax        # 0x1800a7b88
```

### Line 128367 (Address `0x1800740d0`)
```assembly
   18006f7dd:	cc                   	int3
   18006f7de:	cc                   	int3
   18006f7df:	cc                   	int3
   18006f7e0:	48 85 c9             	test   %rcx,%rcx
   18006f7e3:	74 4a                	je     0x18006f82f
   18006f7e5:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18006f7ea:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
   18006f7ef:	57                   	push   %rdi
   18006f7f0:	48 83 ec 20          	sub    $0x20,%rsp
   18006f7f4:	48 8d b1 00 12 00 00 	lea    0x1200(%rcx),%rsi
   18006f7fb:	48 8b d9             	mov    %rcx,%rbx
   18006f7fe:	48 8b f9             	mov    %rcx,%rdi
   18006f801:	48 3b ce             	cmp    %rsi,%rcx
   18006f804:	74 12                	je     0x18006f818
   18006f806:	48 8b cf             	mov    %rdi,%rcx
   18006f809:	ff 15 c1 48 00 00    	call   *0x48c1(%rip)        # 0x1800740d0
   18006f80f:	48 83 c7 48          	add    $0x48,%rdi
   18006f813:	48 3b fe             	cmp    %rsi,%rdi
   18006f816:	75 ee                	jne    0x18006f806
   18006f818:	48 8b cb             	mov    %rbx,%rcx
```

## `KERNEL32.dll!DeviceIoControl` (7 Call Sites)

### Line 26913 (Address `0x180074120`)
```assembly
   18001893a:	66 89 73 08          	mov    %si,0x8(%rbx)
   18001893e:	66 89 43 0a          	mov    %ax,0xa(%rbx)
   180018942:	e8 89 e0 03 00       	call   0x1800569d0
   180018947:	48 8b 0d 42 e4 08 00 	mov    0x8e442(%rip),%rcx        # 0x1800a6d90
   18001894e:	48 8d 44 24 54       	lea    0x54(%rsp),%rax
   180018953:	48 c7 44 24 38 00 00 	movq   $0x0,0x38(%rsp)
   18001895a:	00 00 
   18001895c:	44 8b cf             	mov    %edi,%r9d
   18001895f:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   180018964:	4c 8b c3             	mov    %rbx,%r8
   180018967:	48 8d 44 24 60       	lea    0x60(%rsp),%rax
   18001896c:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   180018973:	00 
   180018974:	ba 54 40 30 00       	mov    $0x304054,%edx
   180018979:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001897e:	ff 15 9c b7 05 00    	call   *0x5b79c(%rip)        # 0x180074120
   180018984:	85 c0                	test   %eax,%eax
   180018986:	75 2f                	jne    0x1800189b7
   180018988:	ff 15 7a b7 05 00    	call   *0x5b77a(%rip)        # 0x180074108
   18001898e:	48 8b 0d 73 fc 08 00 	mov    0x8fc73(%rip),%rcx        # 0x1800a8608
```

### Line 27424 (Address `0x180074120`)
```assembly
   180019085:	33 ff                	xor    %edi,%edi
   180019087:	89 7c 24 60          	mov    %edi,0x60(%rsp)
   18001908b:	bb 02 10 00 00       	mov    $0x1002,%ebx
   180019090:	89 9d e0 03 00 00    	mov    %ebx,0x3e0(%rbp)
   180019096:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   18001909b:	48 8d 44 24 60       	lea    0x60(%rsp),%rax
   1800190a0:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800190a5:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800190ac:	00 
   1800190ad:	48 8d 85 f0 04 00 00 	lea    0x4f0(%rbp),%rax
   1800190b4:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800190b9:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800190bf:	4c 8d 85 e0 03 00 00 	lea    0x3e0(%rbp),%r8
   1800190c6:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800190cb:	48 8b 0d be dc 08 00 	mov    0x8dcbe(%rip),%rcx        # 0x1800a6d90
   1800190d2:	ff 15 48 b0 05 00    	call   *0x5b048(%rip)        # 0x180074120
   1800190d8:	85 c0                	test   %eax,%eax
   1800190da:	75 24                	jne    0x180019100
   1800190dc:	ff 15 26 b0 05 00    	call   *0x5b026(%rip)        # 0x180074108
   1800190e2:	44 8b c0             	mov    %eax,%r8d
```

### Line 27536 (Address `0x180074120`)
```assembly
   180019291:	89 7c 24 68          	mov    %edi,0x68(%rsp)
   180019295:	c7 85 b0 00 00 00 03 	movl   $0x21003,0xb0(%rbp)
   18001929c:	10 02 00 
   18001929f:	66 89 b5 b4 00 00 00 	mov    %si,0xb4(%rbp)
   1800192a6:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   1800192ab:	48 8d 44 24 68       	lea    0x68(%rsp),%rax
   1800192b0:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800192b5:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800192bc:	00 
   1800192bd:	48 8d 85 c0 01 00 00 	lea    0x1c0(%rbp),%rax
   1800192c4:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800192c9:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800192cf:	4c 8d 85 b0 00 00 00 	lea    0xb0(%rbp),%r8
   1800192d6:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800192db:	48 8b 0d ae da 08 00 	mov    0x8daae(%rip),%rcx        # 0x1800a6d90
   1800192e2:	ff 15 38 ae 05 00    	call   *0x5ae38(%rip)        # 0x180074120
   1800192e8:	85 c0                	test   %eax,%eax
   1800192ea:	75 15                	jne    0x180019301
   1800192ec:	ff 15 16 ae 05 00    	call   *0x5ae16(%rip)        # 0x180074108
   1800192f2:	44 8b c0             	mov    %eax,%r8d
```

### Line 27570 (Address `0x180074120`)
```assembly
   18001933c:	89 7c 24 58          	mov    %edi,0x58(%rsp)
   180019340:	c7 85 d0 02 00 00 06 	movl   $0x21006,0x2d0(%rbp)
   180019347:	10 02 00 
   18001934a:	66 89 85 d4 02 00 00 	mov    %ax,0x2d4(%rbp)
   180019351:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   180019356:	48 8d 44 24 58       	lea    0x58(%rsp),%rax
   18001935b:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   180019360:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   180019367:	00 
   180019368:	48 8d 45 a0          	lea    -0x60(%rbp),%rax
   18001936c:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   180019371:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   180019377:	4c 8d 85 d0 02 00 00 	lea    0x2d0(%rbp),%r8
   18001937e:	ba 54 40 30 00       	mov    $0x304054,%edx
   180019383:	48 8b 0d 06 da 08 00 	mov    0x8da06(%rip),%rcx        # 0x1800a6d90
   18001938a:	ff 15 90 ad 05 00    	call   *0x5ad90(%rip)        # 0x180074120
   180019390:	85 c0                	test   %eax,%eax
   180019392:	0f 84 54 ff ff ff    	je     0x1800192ec
   180019398:	0f b7 45 a0          	movzwl -0x60(%rbp),%eax
   18001939c:	66 41 3b c5          	cmp    %r13w,%ax
```

### Line 27754 (Address `0x180074120`)
```assembly
   18001963f:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   180019644:	4c 8d 44 24 50       	lea    0x50(%rsp),%r8
   180019649:	48 8d 8c 24 60 01 00 	lea    0x160(%rsp),%rcx
   180019650:	00 
   180019651:	48 89 ac 24 98 04 00 	mov    %rbp,0x498(%rsp)
   180019658:	00 
   180019659:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   180019660:	00 
   180019661:	bd 01 10 00 00       	mov    $0x1001,%ebp
   180019666:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   18001966b:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   180019671:	48 8b c8             	mov    %rax,%rcx
   180019674:	89 74 24 40          	mov    %esi,0x40(%rsp)
   180019678:	ba 54 40 30 00       	mov    $0x304054,%edx
   18001967d:	89 6c 24 50          	mov    %ebp,0x50(%rsp)
   180019681:	ff 15 99 aa 05 00    	call   *0x5aa99(%rip)        # 0x180074120
   180019687:	85 c0                	test   %eax,%eax
   180019689:	75 12                	jne    0x18001969d
   18001968b:	ff 15 77 aa 05 00    	call   *0x5aa77(%rip)        # 0x180074108
   180019691:	44 8b c0             	mov    %eax,%r8d
```

### Line 36418 (Address `0x180074120`)
```assembly
   1800213a6:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800213ab:	48 8b d9             	mov    %rcx,%rbx
   1800213ae:	48 8b 0d db 59 08 00 	mov    0x859db(%rip),%rcx        # 0x1800a6d90
   1800213b5:	48 8d 84 24 70 02 00 	lea    0x270(%rsp),%rax
   1800213bc:	00 
   1800213bd:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800213c4:	00 
   1800213c5:	8d 7e 02             	lea    0x2(%rsi),%edi
   1800213c8:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800213ce:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800213d3:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800213d8:	89 74 24 40          	mov    %esi,0x40(%rsp)
   1800213dc:	bd 04 10 00 00       	mov    $0x1004,%ebp
   1800213e1:	c7 44 24 50 04 10 02 	movl   $0x21004,0x50(%rsp)
   1800213e8:	00 
   1800213e9:	ff 15 31 2d 05 00    	call   *0x52d31(%rip)        # 0x180074120
   1800213ef:	85 c0                	test   %eax,%eax
   1800213f1:	75 26                	jne    0x180021419
   1800213f3:	ff 15 0f 2d 05 00    	call   *0x52d0f(%rip)        # 0x180074108
   1800213f9:	48 8d 15 10 b4 07 00 	lea    0x7b410(%rip),%rdx        # 0x18009c810
```

### Line 36493 (Address `0x180074120`)
```assembly
   1800214df:	66 89 84 24 64 01 00 	mov    %ax,0x164(%rsp)
   1800214e6:	00 
   1800214e7:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800214ec:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800214f1:	48 8d 44 24 44       	lea    0x44(%rsp),%rax
   1800214f6:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800214fb:	bd 07 10 00 00       	mov    $0x1007,%ebp
   180021500:	48 8d 84 24 80 03 00 	lea    0x380(%rsp),%rax
   180021507:	00 
   180021508:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   18002150f:	00 
   180021510:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   180021515:	89 74 24 44          	mov    %esi,0x44(%rsp)
   180021519:	c7 84 24 60 01 00 00 	movl   $0x21007,0x160(%rsp)
   180021520:	07 10 02 00 
   180021524:	ff 15 f6 2b 05 00    	call   *0x52bf6(%rip)        # 0x180074120
   18002152a:	85 c0                	test   %eax,%eax
   18002152c:	75 12                	jne    0x180021540
   18002152e:	ff 15 d4 2b 05 00    	call   *0x52bd4(%rip)        # 0x180074108
   180021534:	48 8d 15 15 b2 07 00 	lea    0x7b215(%rip),%rdx        # 0x18009c750
```

## `KERNEL32.dll!EncodePointer` (1 Call Sites)

### Line 100495 (Address `0x180074250`)
```assembly
   180057fe6:	48 81 ec a0 00 00 00 	sub    $0xa0,%rsp
   180057fed:	81 39 03 00 00 80    	cmpl   $0x80000003,(%rcx)
   180057ff3:	4d 8b f9             	mov    %r9,%r15
   180057ff6:	49 8b e8             	mov    %r8,%rbp
   180057ff9:	4c 8b f2             	mov    %rdx,%r14
   180057ffc:	48 8b f1             	mov    %rcx,%rsi
   180057fff:	0f 84 d4 01 00 00    	je     0x1800581d9
   180058005:	e8 62 f5 ff ff       	call   0x18005756c
   18005800a:	44 8b ac 24 10 01 00 	mov    0x110(%rsp),%r13d
   180058011:	00 
   180058012:	48 8b bc 24 00 01 00 	mov    0x100(%rsp),%rdi
   180058019:	00 
   18005801a:	48 83 78 10 00       	cmpq   $0x0,0x10(%rax)
   18005801f:	74 56                	je     0x180058077
   180058021:	33 c9                	xor    %ecx,%ecx
   180058023:	ff 15 27 c2 01 00    	call   *0x1c227(%rip)        # 0x180074250
   180058029:	48 8b d8             	mov    %rax,%rbx
   18005802c:	e8 3b f5 ff ff       	call   0x18005756c
   180058031:	48 39 58 10          	cmp    %rbx,0x10(%rax)
   180058035:	74 40                	je     0x180058077
```

## `KERNEL32.dll!EnterCriticalSection` (4 Call Sites)

### Line 28944 (Address `0x1800740b8`)
```assembly
   18001a572:	48 83 ec 20          	sub    $0x20,%rsp
   18001a576:	48 8d 05 cb 0b 08 00 	lea    0x80bcb(%rip),%rax        # 0x18009b148
   18001a57d:	48 8b d9             	mov    %rcx,%rbx
   18001a580:	48 89 01             	mov    %rax,(%rcx)
   18001a583:	48 83 c1 08          	add    $0x8,%rcx
   18001a587:	ff 15 43 9b 05 00    	call   *0x59b43(%rip)        # 0x1800740d0
   18001a58d:	48 8d 05 d4 0b 08 00 	lea    0x80bd4(%rip),%rax        # 0x18009b168
   18001a594:	48 89 03             	mov    %rax,(%rbx)
   18001a597:	48 83 c4 20          	add    $0x20,%rsp
   18001a59b:	5b                   	pop    %rbx
   18001a59c:	c3                   	ret
   18001a59d:	cc                   	int3
   18001a59e:	cc                   	int3
   18001a59f:	cc                   	int3
   18001a5a0:	48 83 c1 08          	add    $0x8,%rcx
   18001a5a4:	48 ff 25 0d 9b 05 00 	rex.W jmp *0x59b0d(%rip)        # 0x1800740b8
   18001a5ab:	cc                   	int3
   18001a5ac:	cc                   	int3
   18001a5ad:	cc                   	int3
   18001a5ae:	cc                   	int3
```

### Line 109671 (Address `0x1800740b8`)
```assembly
   18005fae9:	48 8b 0c 03          	mov    (%rbx,%rax,1),%rcx
   18005faed:	48 83 c1 30          	add    $0x30,%rcx
   18005faf1:	ff 15 d9 45 01 00    	call   *0x145d9(%rip)        # 0x1800740d0
   18005faf7:	48 83 c3 08          	add    $0x8,%rbx
   18005fafb:	48 83 fb 18          	cmp    $0x18,%rbx
   18005faff:	75 d1                	jne    0x18005fad2
   18005fb01:	48 8b 0d 80 80 04 00 	mov    0x48080(%rip),%rcx        # 0x1800a7b88
   18005fb08:	e8 af 6d 00 00       	call   0x1800668bc
   18005fb0d:	48 83 25 73 80 04 00 	andq   $0x0,0x48073(%rip)        # 0x1800a7b88
   18005fb14:	00 
   18005fb15:	48 83 c4 20          	add    $0x20,%rsp
   18005fb19:	5b                   	pop    %rbx
   18005fb1a:	c3                   	ret
   18005fb1b:	cc                   	int3
   18005fb1c:	48 83 c1 30          	add    $0x30,%rcx
   18005fb20:	48 ff 25 91 45 01 00 	rex.W jmp *0x14591(%rip)        # 0x1800740b8
   18005fb27:	cc                   	int3
   18005fb28:	48 83 c1 30          	add    $0x30,%rcx
   18005fb2c:	48 ff 25 8d 45 01 00 	rex.W jmp *0x1458d(%rip)        # 0x1800740c0
   18005fb33:	cc                   	int3
```

### Line 121460 (Address `0x1800740b8`)
```assembly
   1800697c6:	ff c3                	inc    %ebx
   1800697c8:	83 fb 0e             	cmp    $0xe,%ebx
   1800697cb:	72 d3                	jb     0x1800697a0
   1800697cd:	b0 01                	mov    $0x1,%al
   1800697cf:	eb 09                	jmp    0x1800697da
   1800697d1:	33 c9                	xor    %ecx,%ecx
   1800697d3:	e8 24 00 00 00       	call   0x1800697fc
   1800697d8:	32 c0                	xor    %al,%al
   1800697da:	48 83 c4 20          	add    $0x20,%rsp
   1800697de:	5b                   	pop    %rbx
   1800697df:	c3                   	ret
   1800697e0:	48 63 c1             	movslq %ecx,%rax
   1800697e3:	48 8d 0c 80          	lea    (%rax,%rax,4),%rcx
   1800697e7:	48 8d 05 72 e9 03 00 	lea    0x3e972(%rip),%rax        # 0x1800a8160
   1800697ee:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   1800697f2:	48 ff 25 bf a8 00 00 	rex.W jmp *0xa8bf(%rip)        # 0x1800740b8
   1800697f9:	cc                   	int3
   1800697fa:	cc                   	int3
   1800697fb:	cc                   	int3
   1800697fc:	40 53                	rex push %rbx
```

### Line 128433 (Address `0x1800740b8`)
```assembly
   18006f8bf:	89 05 6b 88 03 00    	mov    %eax,0x3886b(%rip)        # 0x1800a8130
   18006f8c5:	48 ff c3             	inc    %rbx
   18006f8c8:	eb c1                	jmp    0x18006f88b
   18006f8ca:	b9 07 00 00 00       	mov    $0x7,%ecx
   18006f8cf:	e8 60 9f ff ff       	call   0x180069834
   18006f8d4:	8b c7                	mov    %edi,%eax
   18006f8d6:	eb 8a                	jmp    0x18006f862
   18006f8d8:	48 63 d1             	movslq %ecx,%rdx
   18006f8db:	4c 8d 05 4e 84 03 00 	lea    0x3844e(%rip),%r8        # 0x1800a7d30
   18006f8e2:	48 8b c2             	mov    %rdx,%rax
   18006f8e5:	83 e2 3f             	and    $0x3f,%edx
   18006f8e8:	48 c1 f8 06          	sar    $0x6,%rax
   18006f8ec:	48 8d 0c d2          	lea    (%rdx,%rdx,8),%rcx
   18006f8f0:	49 8b 04 c0          	mov    (%r8,%rax,8),%rax
   18006f8f4:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   18006f8f8:	48 ff 25 b9 47 00 00 	rex.W jmp *0x47b9(%rip)        # 0x1800740b8
   18006f8ff:	cc                   	int3
   18006f900:	48 63 d1             	movslq %ecx,%rdx
   18006f903:	4c 8d 05 26 84 03 00 	lea    0x38426(%rip),%r8        # 0x1800a7d30
   18006f90a:	48 8b c2             	mov    %rdx,%rax
```

## `KERNEL32.dll!ExitProcess` (1 Call Sites)

### Line 109518 (Address `0x1800742a8`)
```assembly
   18005f8b9:	83 f8 01             	cmp    $0x1,%eax
   18005f8bc:	74 28                	je     0x18005f8e6
   18005f8be:	65 48 8b 04 25 60 00 	mov    %gs:0x60,%rax
   18005f8c5:	00 00 
   18005f8c7:	8b 90 bc 00 00 00    	mov    0xbc(%rax),%edx
   18005f8cd:	c1 ea 08             	shr    $0x8,%edx
   18005f8d0:	f6 c2 01             	test   $0x1,%dl
   18005f8d3:	75 11                	jne    0x18005f8e6
   18005f8d5:	ff 15 8d 48 01 00    	call   *0x1488d(%rip)        # 0x180074168
   18005f8db:	48 8b c8             	mov    %rax,%rcx
   18005f8de:	8b d3                	mov    %ebx,%edx
   18005f8e0:	ff 15 12 49 01 00    	call   *0x14912(%rip)        # 0x1800741f8
   18005f8e6:	8b cb                	mov    %ebx,%ecx
   18005f8e8:	e8 0b 00 00 00       	call   0x18005f8f8
   18005f8ed:	8b cb                	mov    %ebx,%ecx
   18005f8ef:	ff 15 b3 49 01 00    	call   *0x149b3(%rip)        # 0x1800742a8
   18005f8f5:	cc                   	int3
   18005f8f6:	cc                   	int3
   18005f8f7:	cc                   	int3
   18005f8f8:	40 53                	rex push %rbx
```

## `KERNEL32.dll!FileTimeToLocalFileTime` (1 Call Sites)

### Line 23941 (Address `0x1800740a0`)
```assembly
   18001608f:	41 b6 02             	mov    $0x2,%r14b
   180016092:	eb 12                	jmp    0x1800160a6
   180016094:	b8 04 00 00 00       	mov    $0x4,%eax
   180016099:	41 be 09 00 00 00    	mov    $0x9,%r14d
   18001609f:	83 fb 02             	cmp    $0x2,%ebx
   1800160a2:	44 0f 44 f0          	cmove  %eax,%r14d
   1800160a6:	48 b8 00 68 b6 30 97 	movabs $0xa9730b66800,%rax
   1800160ad:	0a 00 00 
   1800160b0:	48 03 c2             	add    %rdx,%rax
   1800160b3:	48 69 c8 10 27 00 00 	imul   $0x2710,%rax,%rcx
   1800160ba:	89 4d d7             	mov    %ecx,-0x29(%rbp)
   1800160bd:	48 c1 e9 20          	shr    $0x20,%rcx
   1800160c1:	89 4d db             	mov    %ecx,-0x25(%rbp)
   1800160c4:	48 8d 55 e7          	lea    -0x19(%rbp),%rdx
   1800160c8:	48 8d 4d d7          	lea    -0x29(%rbp),%rcx
   1800160cc:	ff 15 ce df 05 00    	call   *0x5dfce(%rip)        # 0x1800740a0
   1800160d2:	48 8d 55 17          	lea    0x17(%rbp),%rdx
   1800160d6:	48 8d 4d d7          	lea    -0x29(%rbp),%rcx
   1800160da:	ff 15 b8 df 05 00    	call   *0x5dfb8(%rip)        # 0x180074098
   1800160e0:	0f b7 45 23          	movzwl 0x23(%rbp),%eax
```

## `KERNEL32.dll!FileTimeToSystemTime` (2 Call Sites)

### Line 23944 (Address `0x180074098`)
```assembly
   180016099:	41 be 09 00 00 00    	mov    $0x9,%r14d
   18001609f:	83 fb 02             	cmp    $0x2,%ebx
   1800160a2:	44 0f 44 f0          	cmove  %eax,%r14d
   1800160a6:	48 b8 00 68 b6 30 97 	movabs $0xa9730b66800,%rax
   1800160ad:	0a 00 00 
   1800160b0:	48 03 c2             	add    %rdx,%rax
   1800160b3:	48 69 c8 10 27 00 00 	imul   $0x2710,%rax,%rcx
   1800160ba:	89 4d d7             	mov    %ecx,-0x29(%rbp)
   1800160bd:	48 c1 e9 20          	shr    $0x20,%rcx
   1800160c1:	89 4d db             	mov    %ecx,-0x25(%rbp)
   1800160c4:	48 8d 55 e7          	lea    -0x19(%rbp),%rdx
   1800160c8:	48 8d 4d d7          	lea    -0x29(%rbp),%rcx
   1800160cc:	ff 15 ce df 05 00    	call   *0x5dfce(%rip)        # 0x1800740a0
   1800160d2:	48 8d 55 17          	lea    0x17(%rbp),%rdx
   1800160d6:	48 8d 4d d7          	lea    -0x29(%rbp),%rcx
   1800160da:	ff 15 b8 df 05 00    	call   *0x5dfb8(%rip)        # 0x180074098
   1800160e0:	0f b7 45 23          	movzwl 0x23(%rbp),%eax
   1800160e4:	0f b7 4d 21          	movzwl 0x21(%rbp),%ecx
   1800160e8:	0f b7 55 1f          	movzwl 0x1f(%rbp),%edx
   1800160ec:	44 0f b7 55 1d       	movzwl 0x1d(%rbp),%r10d
```

### Line 37298 (Address `0x180074098`)
```assembly
   180021f8d:	49 d1 f8             	sar    $1,%r8
   180021f90:	4d 03 c0             	add    %r8,%r8
   180021f93:	48 8d 15 36 c1 07 00 	lea    0x7c136(%rip),%rdx        # 0x18009e0d0
   180021f9a:	e8 31 4a 03 00       	call   0x1800569d0
   180021f9f:	90                   	nop
   180021fa0:	48 8b 03             	mov    (%rbx),%rax
   180021fa3:	48 b9 00 68 b6 30 97 	movabs $0xa9730b66800,%rcx
   180021faa:	0a 00 00 
   180021fad:	48 03 c1             	add    %rcx,%rax
   180021fb0:	48 69 c8 10 27 00 00 	imul   $0x2710,%rax,%rcx
   180021fb7:	89 4d d7             	mov    %ecx,-0x29(%rbp)
   180021fba:	48 c1 e9 20          	shr    $0x20,%rcx
   180021fbe:	89 4d db             	mov    %ecx,-0x25(%rbp)
   180021fc1:	48 8d 55 a7          	lea    -0x59(%rbp),%rdx
   180021fc5:	48 8d 4d d7          	lea    -0x29(%rbp),%rcx
   180021fc9:	ff 15 c9 20 05 00    	call   *0x520c9(%rip)        # 0x180074098
   180021fcf:	49 8b 85 98 00 00 00 	mov    0x98(%r13),%rax
   180021fd6:	49 8d 8d 98 00 00 00 	lea    0x98(%r13),%rcx
   180021fdd:	ff 50 08             	call   *0x8(%rax)
   180021fe0:	90                   	nop
```

## `KERNEL32.dll!FindClose` (1 Call Sites)

### Line 124896 (Address `0x180074188`)
```assembly
   18006c695:	48 2b d0             	sub    %rax,%rdx
   18006c698:	48 c1 fa 03          	sar    $0x3,%rdx
   18006c69c:	4c 3b f2             	cmp    %rdx,%r14
   18006c69f:	74 29                	je     0x18006c6ca
   18006c6a1:	49 2b d6             	sub    %r14,%rdx
   18006c6a4:	4a 8d 0c f0          	lea    (%rax,%r14,8),%rcx
   18006c6a8:	4c 8d 0d a5 f6 ff ff 	lea    -0x95b(%rip),%r9        # 0x18006bd54
   18006c6af:	41 b8 08 00 00 00    	mov    $0x8,%r8d
   18006c6b5:	e8 d6 40 00 00       	call   0x180070790
   18006c6ba:	eb 0e                	jmp    0x18006c6ca
   18006c6bc:	80 7d 98 00          	cmpb   $0x0,-0x68(%rbp)
   18006c6c0:	74 08                	je     0x18006c6ca
   18006c6c2:	49 8b cf             	mov    %r15,%rcx
   18006c6c5:	e8 f2 a1 ff ff       	call   0x1800668bc
   18006c6ca:	48 8b cb             	mov    %rbx,%rcx
   18006c6cd:	ff 15 b5 7a 00 00    	call   *0x7ab5(%rip)        # 0x180074188
   18006c6d3:	80 7d c8 00          	cmpb   $0x0,-0x38(%rbp)
   18006c6d7:	74 09                	je     0x18006c6e2
   18006c6d9:	48 8b 4d b0          	mov    -0x50(%rbp),%rcx
   18006c6dd:	e8 da a1 ff ff       	call   0x1800668bc
```

## `KERNEL32.dll!FindFirstFileExW` (1 Call Sites)

### Line 124799 (Address `0x1800742c8`)
```assembly
   18006c52d:	74 0c                	je     0x18006c53b
   18006c52f:	48 8b 44 24 30       	mov    0x30(%rsp),%rax
   18006c534:	83 a0 a8 03 00 00 fd 	andl   $0xfffffffd,0x3a8(%rax)
   18006c53b:	44 8b c7             	mov    %edi,%r8d
   18006c53e:	48 8d 55 a0          	lea    -0x60(%rbp),%rdx
   18006c542:	48 8b ce             	mov    %rsi,%rcx
   18006c545:	e8 1e f8 ff ff       	call   0x18006bd68
   18006c54a:	48 8b 4d b0          	mov    -0x50(%rbp),%rcx
   18006c54e:	4c 8d 45 d0          	lea    -0x30(%rbp),%r8
   18006c552:	85 c0                	test   %eax,%eax
   18006c554:	89 7c 24 28          	mov    %edi,0x28(%rsp)
   18006c558:	48 89 7c 24 20       	mov    %rdi,0x20(%rsp)
   18006c55d:	48 0f 45 cf          	cmovne %rdi,%rcx
   18006c561:	45 33 c9             	xor    %r9d,%r9d
   18006c564:	33 d2                	xor    %edx,%edx
   18006c566:	ff 15 5c 7d 00 00    	call   *0x7d5c(%rip)        # 0x1800742c8
   18006c56c:	48 8b d8             	mov    %rax,%rbx
   18006c56f:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18006c573:	75 17                	jne    0x18006c58c
   18006c575:	4d 8b cc             	mov    %r12,%r9
```

## `KERNEL32.dll!FindNextFileW` (1 Call Sites)

### Line 124875 (Address `0x180074180`)
```assembly
   18006c64b:	74 16                	je     0x18006c663
   18006c64d:	4d 8b cc             	mov    %r12,%r9
   18006c650:	4d 8b c5             	mov    %r13,%r8
   18006c653:	48 8b d6             	mov    %rsi,%rdx
   18006c656:	e8 1d fc ff ff       	call   0x18006c278
   18006c65b:	8b f8                	mov    %eax,%edi
   18006c65d:	85 c0                	test   %eax,%eax
   18006c65f:	75 5b                	jne    0x18006c6bc
   18006c661:	33 ff                	xor    %edi,%edi
   18006c663:	40 38 7d 98          	cmp    %dil,-0x68(%rbp)
   18006c667:	74 08                	je     0x18006c671
   18006c669:	49 8b cf             	mov    %r15,%rcx
   18006c66c:	e8 4b a2 ff ff       	call   0x1800668bc
   18006c671:	48 8d 55 d0          	lea    -0x30(%rbp),%rdx
   18006c675:	48 8b cb             	mov    %rbx,%rcx
   18006c678:	ff 15 02 7b 00 00    	call   *0x7b02(%rip)        # 0x180074180
   18006c67e:	41 bf e9 fd 00 00    	mov    $0xfde9,%r15d
   18006c684:	85 c0                	test   %eax,%eax
   18006c686:	0f 85 0d ff ff ff    	jne    0x18006c599
   18006c68c:	49 8b 04 24          	mov    (%r12),%rax
```

## `KERNEL32.dll!FlushFileBuffers` (1 Call Sites)

### Line 122838 (Address `0x180074110`)
```assembly
   18006aacf:	e8 04 4e 00 00       	call   0x18006f8d8
   18006aad4:	90                   	nop
   18006aad5:	48 8b 03             	mov    (%rbx),%rax
   18006aad8:	48 63 08             	movslq (%rax),%rcx
   18006aadb:	48 8b d1             	mov    %rcx,%rdx
   18006aade:	48 8b c1             	mov    %rcx,%rax
   18006aae1:	48 c1 f8 06          	sar    $0x6,%rax
   18006aae5:	4c 8d 05 44 d2 03 00 	lea    0x3d244(%rip),%r8        # 0x1800a7d30
   18006aaec:	83 e2 3f             	and    $0x3f,%edx
   18006aaef:	48 8d 14 d2          	lea    (%rdx,%rdx,8),%rdx
   18006aaf3:	49 8b 04 c0          	mov    (%r8,%rax,8),%rax
   18006aaf7:	f6 44 d0 38 01       	testb  $0x1,0x38(%rax,%rdx,8)
   18006aafc:	74 24                	je     0x18006ab22
   18006aafe:	e8 e1 4e 00 00       	call   0x18006f9e4
   18006ab03:	48 8b c8             	mov    %rax,%rcx
   18006ab06:	ff 15 04 96 00 00    	call   *0x9604(%rip)        # 0x180074110
   18006ab0c:	33 db                	xor    %ebx,%ebx
   18006ab0e:	85 c0                	test   %eax,%eax
   18006ab10:	75 1e                	jne    0x18006ab30
   18006ab12:	e8 2d 4a ff ff       	call   0x18005f544
```

## `KERNEL32.dll!FormatMessageW` (2 Call Sites)

### Line 39188 (Address `0x180074170`)
```assembly
   1800238a7:	48 89 84 24 40 08 00 	mov    %rax,0x840(%rsp)
   1800238ae:	00 
   1800238af:	48 8b f9             	mov    %rcx,%rdi
   1800238b2:	ff 15 50 08 05 00    	call   *0x50850(%rip)        # 0x180074108
   1800238b8:	48 c7 44 24 30 00 00 	movq   $0x0,0x30(%rsp)
   1800238bf:	00 00 
   1800238c1:	41 b9 09 04 00 00    	mov    $0x409,%r9d
   1800238c7:	8b d8                	mov    %eax,%ebx
   1800238c9:	c7 44 24 28 00 08 00 	movl   $0x800,0x28(%rsp)
   1800238d0:	00 
   1800238d1:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   1800238d6:	44 8b c3             	mov    %ebx,%r8d
   1800238d9:	33 d2                	xor    %edx,%edx
   1800238db:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800238e0:	b9 00 12 00 00       	mov    $0x1200,%ecx
   1800238e5:	ff 15 85 08 05 00    	call   *0x50885(%rip)        # 0x180074170
   1800238eb:	48 8b cf             	mov    %rdi,%rcx
   1800238ee:	85 c0                	test   %eax,%eax
   1800238f0:	75 11                	jne    0x180023903
   1800238f2:	44 8b c3             	mov    %ebx,%r8d
```

### Line 39388 (Address `0x180074170`)
```assembly
   180023b2e:	b3 01                	mov    $0x1,%bl
   180023b30:	33 d2                	xor    %edx,%edx
   180023b32:	41 b8 00 50 00 00    	mov    $0x5000,%r8d
   180023b38:	48 8d 4d a0          	lea    -0x60(%rbp),%rcx
   180023b3c:	e8 ef 32 03 00       	call   0x180056e30
   180023b41:	33 f6                	xor    %esi,%esi
   180023b43:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
   180023b48:	c7 44 24 28 00 50 00 	movl   $0x5000,0x28(%rsp)
   180023b4f:	00 
   180023b50:	48 8d 45 a0          	lea    -0x60(%rbp),%rax
   180023b54:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   180023b59:	41 b9 09 04 00 00    	mov    $0x409,%r9d
   180023b5f:	45 8b c4             	mov    %r12d,%r8d
   180023b62:	33 d2                	xor    %edx,%edx
   180023b64:	b9 00 12 00 00       	mov    $0x1200,%ecx
   180023b69:	ff 15 01 06 05 00    	call   *0x50601(%rip)        # 0x180074170
   180023b6f:	0f b6 cb             	movzbl %bl,%ecx
   180023b72:	85 c0                	test   %eax,%eax
   180023b74:	0f 44 ce             	cmove  %esi,%ecx
   180023b77:	89 4d 88             	mov    %ecx,-0x78(%rbp)
```

## `KERNEL32.dll!FreeEnvironmentStringsW` (1 Call Sites)

### Line 125760 (Address `0x180074010`)
```assembly
   18006d2df:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18006d2e4:	e8 17 c4 ff ff       	call   0x180069700
   18006d2e9:	85 c0                	test   %eax,%eax
   18006d2eb:	74 08                	je     0x18006d2f5
   18006d2ed:	48 8b f7             	mov    %rdi,%rsi
   18006d2f0:	49 8b fe             	mov    %r14,%rdi
   18006d2f3:	eb 03                	jmp    0x18006d2f8
   18006d2f5:	49 8b f6             	mov    %r14,%rsi
   18006d2f8:	48 8b cf             	mov    %rdi,%rcx
   18006d2fb:	e8 bc 95 ff ff       	call   0x1800668bc
   18006d300:	eb 03                	jmp    0x18006d305
   18006d302:	49 8b f6             	mov    %r14,%rsi
   18006d305:	48 85 db             	test   %rbx,%rbx
   18006d308:	74 09                	je     0x18006d313
   18006d30a:	48 8b cb             	mov    %rbx,%rcx
   18006d30d:	ff 15 fd 6c 00 00    	call   *0x6cfd(%rip)        # 0x180074010
   18006d313:	48 8b 5c 24 50       	mov    0x50(%rsp),%rbx
   18006d318:	48 8b c6             	mov    %rsi,%rax
   18006d31b:	48 8b 74 24 60       	mov    0x60(%rsp),%rsi
   18006d320:	48 8b 6c 24 58       	mov    0x58(%rsp),%rbp
```

## `KERNEL32.dll!FreeLibrary` (5 Call Sites)

### Line 101584 (Address `0x180074278`)
```assembly
   180058e60:	eb 02                	jmp    0x180058e64
   180058e62:	33 db                	xor    %ebx,%ebx
   180058e64:	4c 8d 35 95 71 fa ff 	lea    -0x58e6b(%rip),%r14        # 0x180000000
   180058e6b:	48 85 db             	test   %rbx,%rbx
   180058e6e:	75 0d                	jne    0x180058e7d
   180058e70:	48 8b c7             	mov    %rdi,%rax
   180058e73:	49 87 84 f6 b8 7a 0a 	xchg   %rax,0xa7ab8(%r14,%rsi,8)
   180058e7a:	00 
   180058e7b:	eb 1e                	jmp    0x180058e9b
   180058e7d:	48 8b c3             	mov    %rbx,%rax
   180058e80:	49 87 84 f6 b8 7a 0a 	xchg   %rax,0xa7ab8(%r14,%rsi,8)
   180058e87:	00 
   180058e88:	48 85 c0             	test   %rax,%rax
   180058e8b:	74 09                	je     0x180058e96
   180058e8d:	48 8b cb             	mov    %rbx,%rcx
   180058e90:	ff 15 e2 b3 01 00    	call   *0x1b3e2(%rip)        # 0x180074278
   180058e96:	48 85 db             	test   %rbx,%rbx
   180058e99:	75 55                	jne    0x180058ef0
   180058e9b:	48 83 c5 04          	add    $0x4,%rbp
   180058e9f:	49 3b ec             	cmp    %r12,%rbp
```

### Line 101767 (Address `0x180074278`)
```assembly
   1800590ef:	83 e1 05             	and    $0x5,%ecx
   1800590f2:	f3 48 ab             	rep stos %rax,(%rdi)
   1800590f5:	48 8b 7c 24 08       	mov    0x8(%rsp),%rdi
   1800590fa:	c3                   	ret
   1800590fb:	cc                   	int3
   1800590fc:	84 c9                	test   %cl,%cl
   1800590fe:	75 39                	jne    0x180059139
   180059100:	53                   	push   %rbx
   180059101:	48 83 ec 20          	sub    $0x20,%rsp
   180059105:	48 8d 1d ac e9 04 00 	lea    0x4e9ac(%rip),%rbx        # 0x1800a7ab8
   18005910c:	48 8b 0b             	mov    (%rbx),%rcx
   18005910f:	48 85 c9             	test   %rcx,%rcx
   180059112:	74 10                	je     0x180059124
   180059114:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   180059118:	74 06                	je     0x180059120
   18005911a:	ff 15 58 b1 01 00    	call   *0x1b158(%rip)        # 0x180074278
   180059120:	48 83 23 00          	andq   $0x0,(%rbx)
   180059124:	48 83 c3 08          	add    $0x8,%rbx
   180059128:	48 8d 05 a1 e9 04 00 	lea    0x4e9a1(%rip),%rax        # 0x1800a7ad0
   18005912f:	48 3b d8             	cmp    %rax,%rbx
```

### Line 109542 (Address `0x180074278`)
```assembly
   18005f90b:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x180093598
   18005f912:	33 c9                	xor    %ecx,%ecx
   18005f914:	ff 15 7e 49 01 00    	call   *0x1497e(%rip)        # 0x180074298
   18005f91a:	85 c0                	test   %eax,%eax
   18005f91c:	74 1f                	je     0x18005f93d
   18005f91e:	48 8b 4c 24 38       	mov    0x38(%rsp),%rcx
   18005f923:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x1800935b0
   18005f92a:	ff 15 98 48 01 00    	call   *0x14898(%rip)        # 0x1800741c8
   18005f930:	48 85 c0             	test   %rax,%rax
   18005f933:	74 08                	je     0x18005f93d
   18005f935:	8b cb                	mov    %ebx,%ecx
   18005f937:	ff 15 33 4a 01 00    	call   *0x14a33(%rip)        # 0x180074370
   18005f93d:	48 8b 4c 24 38       	mov    0x38(%rsp),%rcx
   18005f942:	48 85 c9             	test   %rcx,%rcx
   18005f945:	74 06                	je     0x18005f94d
   18005f947:	ff 15 2b 49 01 00    	call   *0x1492b(%rip)        # 0x180074278
   18005f94d:	48 83 c4 20          	add    $0x20,%rsp
   18005f951:	5b                   	pop    %rbx
   18005f952:	c3                   	ret
   18005f953:	cc                   	int3
```

### Line 122218 (Address `0x180074278`)
```assembly
   18006a1c8:	eb 02                	jmp    0x18006a1cc
   18006a1ca:	33 db                	xor    %ebx,%ebx
   18006a1cc:	4c 8d 35 2d 5e f9 ff 	lea    -0x6a1d3(%rip),%r14        # 0x180000000
   18006a1d3:	48 85 db             	test   %rbx,%rbx
   18006a1d6:	75 0d                	jne    0x18006a1e5
   18006a1d8:	48 8b c7             	mov    %rdi,%rax
   18006a1db:	49 87 84 f6 a0 83 0a 	xchg   %rax,0xa83a0(%r14,%rsi,8)
   18006a1e2:	00 
   18006a1e3:	eb 1e                	jmp    0x18006a203
   18006a1e5:	48 8b c3             	mov    %rbx,%rax
   18006a1e8:	49 87 84 f6 a0 83 0a 	xchg   %rax,0xa83a0(%r14,%rsi,8)
   18006a1ef:	00 
   18006a1f0:	48 85 c0             	test   %rax,%rax
   18006a1f3:	74 09                	je     0x18006a1fe
   18006a1f5:	48 8b cb             	mov    %rbx,%rcx
   18006a1f8:	ff 15 7a a0 00 00    	call   *0xa07a(%rip)        # 0x180074278
   18006a1fe:	48 85 db             	test   %rbx,%rbx
   18006a201:	75 55                	jne    0x18006a258
   18006a203:	48 83 c5 04          	add    $0x4,%rbp
   18006a207:	49 3b ec             	cmp    %r12,%rbp
```

### Line 122755 (Address `0x180074278`)
```assembly
   18006a9b8:	48 83 c4 50          	add    $0x50,%rsp
   18006a9bc:	5f                   	pop    %rdi
   18006a9bd:	c3                   	ret
   18006a9be:	cc                   	int3
   18006a9bf:	cc                   	int3
   18006a9c0:	40 53                	rex push %rbx
   18006a9c2:	48 83 ec 20          	sub    $0x20,%rsp
   18006a9c6:	84 c9                	test   %cl,%cl
   18006a9c8:	75 2f                	jne    0x18006a9f9
   18006a9ca:	48 8d 1d cf d9 03 00 	lea    0x3d9cf(%rip),%rbx        # 0x1800a83a0
   18006a9d1:	48 8b 0b             	mov    (%rbx),%rcx
   18006a9d4:	48 85 c9             	test   %rcx,%rcx
   18006a9d7:	74 10                	je     0x18006a9e9
   18006a9d9:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   18006a9dd:	74 06                	je     0x18006a9e5
   18006a9df:	ff 15 93 98 00 00    	call   *0x9893(%rip)        # 0x180074278
   18006a9e5:	48 83 23 00          	andq   $0x0,(%rbx)
   18006a9e9:	48 83 c3 08          	add    $0x8,%rbx
   18006a9ed:	48 8d 05 4c da 03 00 	lea    0x3da4c(%rip),%rax        # 0x1800a8440
   18006a9f4:	48 3b d8             	cmp    %rax,%rbx
```

## `KERNEL32.dll!GetACP` (1 Call Sites)

### Line 125059 (Address `0x180074040`)
```assembly
   18006c8da:	8b d9                	mov    %ecx,%ebx
   18006c8dc:	33 d2                	xor    %edx,%edx
   18006c8de:	48 8d 4c 24 20       	lea    0x20(%rsp),%rcx
   18006c8e3:	e8 d4 d6 fe ff       	call   0x180059fbc
   18006c8e8:	83 25 79 bc 03 00 00 	andl   $0x0,0x3bc79(%rip)        # 0x1800a8568
   18006c8ef:	83 fb fe             	cmp    $0xfffffffe,%ebx
   18006c8f2:	75 12                	jne    0x18006c906
   18006c8f4:	c7 05 6a bc 03 00 01 	movl   $0x1,0x3bc6a(%rip)        # 0x1800a8568
   18006c8fb:	00 00 00 
   18006c8fe:	ff 15 34 77 00 00    	call   *0x7734(%rip)        # 0x180074038
   18006c904:	eb 15                	jmp    0x18006c91b
   18006c906:	83 fb fd             	cmp    $0xfffffffd,%ebx
   18006c909:	75 14                	jne    0x18006c91f
   18006c90b:	c7 05 53 bc 03 00 01 	movl   $0x1,0x3bc53(%rip)        # 0x1800a8568
   18006c912:	00 00 00 
   18006c915:	ff 15 25 77 00 00    	call   *0x7725(%rip)        # 0x180074040
   18006c91b:	8b d8                	mov    %eax,%ebx
   18006c91d:	eb 17                	jmp    0x18006c936
   18006c91f:	83 fb fc             	cmp    $0xfffffffc,%ebx
   18006c922:	75 12                	jne    0x18006c936
```

## `KERNEL32.dll!GetCPInfo` (3 Call Sites)

### Line 125132 (Address `0x180074030`)
```assembly
   18006c9e3:	c3                   	ret
   18006c9e4:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   18006c9e9:	48 89 74 24 18       	mov    %rsi,0x18(%rsp)
   18006c9ee:	55                   	push   %rbp
   18006c9ef:	48 8d ac 24 80 f9 ff 	lea    -0x680(%rsp),%rbp
   18006c9f6:	ff 
   18006c9f7:	48 81 ec 80 07 00 00 	sub    $0x780,%rsp
   18006c9fe:	48 8b 05 5b 99 03 00 	mov    0x3995b(%rip),%rax        # 0x1800a6360
   18006ca05:	48 33 c4             	xor    %rsp,%rax
   18006ca08:	48 89 85 70 06 00 00 	mov    %rax,0x670(%rbp)
   18006ca0f:	48 8b d9             	mov    %rcx,%rbx
   18006ca12:	8b 49 04             	mov    0x4(%rcx),%ecx
   18006ca15:	81 f9 e9 fd 00 00    	cmp    $0xfde9,%ecx
   18006ca1b:	0f 84 3f 01 00 00    	je     0x18006cb60
   18006ca21:	48 8d 54 24 50       	lea    0x50(%rsp),%rdx
   18006ca26:	ff 15 04 76 00 00    	call   *0x7604(%rip)        # 0x180074030
   18006ca2c:	85 c0                	test   %eax,%eax
   18006ca2e:	0f 84 2c 01 00 00    	je     0x18006cb60
   18006ca34:	33 c0                	xor    %eax,%eax
   18006ca36:	48 8d 4c 24 70       	lea    0x70(%rsp),%rcx
```

### Line 125492 (Address `0x180074030`)
```assembly
   18006cf3e:	3b f8                	cmp    %eax,%edi
   18006cf40:	75 2e                	jne    0x18006cf70
   18006cf42:	48 89 46 04          	mov    %rax,0x4(%rsi)
   18006cf46:	48 89 9e 20 02 00 00 	mov    %rbx,0x220(%rsi)
   18006cf4d:	89 5e 18             	mov    %ebx,0x18(%rsi)
   18006cf50:	66 89 5e 1c          	mov    %bx,0x1c(%rsi)
   18006cf54:	48 8d 7e 0c          	lea    0xc(%rsi),%rdi
   18006cf58:	0f b7 c3             	movzwl %bx,%eax
   18006cf5b:	b9 06 00 00 00       	mov    $0x6,%ecx
   18006cf60:	66 f3 ab             	rep stos %ax,(%rdi)
   18006cf63:	48 8b ce             	mov    %rsi,%rcx
   18006cf66:	e8 79 fa ff ff       	call   0x18006c9e4
   18006cf6b:	e9 e2 01 00 00       	jmp    0x18006d152
   18006cf70:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   18006cf75:	8b cf                	mov    %edi,%ecx
   18006cf77:	ff 15 b3 70 00 00    	call   *0x70b3(%rip)        # 0x180074030
   18006cf7d:	85 c0                	test   %eax,%eax
   18006cf7f:	0f 84 c4 00 00 00    	je     0x18006d049
   18006cf85:	33 d2                	xor    %edx,%edx
   18006cf87:	48 8d 4e 18          	lea    0x18(%rsi),%rcx
```

### Line 129046 (Address `0x180074030`)
```assembly
   180070109:	75 07                	jne    0x180070112
   18007010b:	48 8b 07             	mov    (%rdi),%rax
   18007010e:	44 8b 70 0c          	mov    0xc(%rax),%r14d
   180070112:	85 db                	test   %ebx,%ebx
   180070114:	74 08                	je     0x18007011e
   180070116:	85 f6                	test   %esi,%esi
   180070118:	0f 85 a6 00 00 00    	jne    0x1800701c4
   18007011e:	3b de                	cmp    %esi,%ebx
   180070120:	0f 84 89 02 00 00    	je     0x1800703af
   180070126:	83 fe 01             	cmp    $0x1,%esi
   180070129:	0f 8f 8b 00 00 00    	jg     0x1800701ba
   18007012f:	83 fb 01             	cmp    $0x1,%ebx
   180070132:	7f 48                	jg     0x18007017c
   180070134:	48 8d 55 10          	lea    0x10(%rbp),%rdx
   180070138:	41 8b ce             	mov    %r14d,%ecx
   18007013b:	ff 15 ef 3e 00 00    	call   *0x3eef(%rip)        # 0x180074030
   180070141:	85 c0                	test   %eax,%eax
   180070143:	0f 84 6d 02 00 00    	je     0x1800703b6
   180070149:	85 db                	test   %ebx,%ebx
   18007014b:	7e 39                	jle    0x180070186
```

## `KERNEL32.dll!GetCommandLineA` (1 Call Sites)

### Line 125685 (Address `0x180074028`)
```assembly
   18006d1e6:	48 8b 74 24 58       	mov    0x58(%rsp),%rsi
   18006d1eb:	48 83 c4 40          	add    $0x40,%rsp
   18006d1ef:	5f                   	pop    %rdi
   18006d1f0:	c3                   	ret
   18006d1f1:	cc                   	int3
   18006d1f2:	cc                   	int3
   18006d1f3:	cc                   	int3
   18006d1f4:	8b d1                	mov    %ecx,%edx
   18006d1f6:	41 b9 04 00 00 00    	mov    $0x4,%r9d
   18006d1fc:	33 c9                	xor    %ecx,%ecx
   18006d1fe:	45 33 c0             	xor    %r8d,%r8d
   18006d201:	e9 76 ff ff ff       	jmp    0x18006d17c
   18006d206:	cc                   	int3
   18006d207:	cc                   	int3
   18006d208:	48 83 ec 28          	sub    $0x28,%rsp
   18006d20c:	ff 15 16 6e 00 00    	call   *0x6e16(%rip)        # 0x180074028
   18006d212:	48 89 05 77 b3 03 00 	mov    %rax,0x3b377(%rip)        # 0x1800a8590
   18006d219:	ff 15 01 6e 00 00    	call   *0x6e01(%rip)        # 0x180074020
   18006d21f:	48 89 05 72 b3 03 00 	mov    %rax,0x3b372(%rip)        # 0x1800a8598
   18006d226:	b0 01                	mov    $0x1,%al
```

## `KERNEL32.dll!GetCommandLineW` (1 Call Sites)

### Line 125687 (Address `0x180074020`)
```assembly
   18006d1ef:	5f                   	pop    %rdi
   18006d1f0:	c3                   	ret
   18006d1f1:	cc                   	int3
   18006d1f2:	cc                   	int3
   18006d1f3:	cc                   	int3
   18006d1f4:	8b d1                	mov    %ecx,%edx
   18006d1f6:	41 b9 04 00 00 00    	mov    $0x4,%r9d
   18006d1fc:	33 c9                	xor    %ecx,%ecx
   18006d1fe:	45 33 c0             	xor    %r8d,%r8d
   18006d201:	e9 76 ff ff ff       	jmp    0x18006d17c
   18006d206:	cc                   	int3
   18006d207:	cc                   	int3
   18006d208:	48 83 ec 28          	sub    $0x28,%rsp
   18006d20c:	ff 15 16 6e 00 00    	call   *0x6e16(%rip)        # 0x180074028
   18006d212:	48 89 05 77 b3 03 00 	mov    %rax,0x3b377(%rip)        # 0x1800a8590
   18006d219:	ff 15 01 6e 00 00    	call   *0x6e01(%rip)        # 0x180074020
   18006d21f:	48 89 05 72 b3 03 00 	mov    %rax,0x3b372(%rip)        # 0x1800a8598
   18006d226:	b0 01                	mov    $0x1,%al
   18006d228:	48 83 c4 28          	add    $0x28,%rsp
   18006d22c:	c3                   	ret
```

## `KERNEL32.dll!GetConsoleCP` (1 Call Sites)

### Line 122927 (Address `0x180074198`)
```assembly
   18006ac0b:	48 89 4d ff          	mov    %rcx,-0x1(%rbp)
   18006ac0f:	83 e0 3f             	and    $0x3f,%eax
   18006ac12:	45 8b e9             	mov    %r9d,%r13d
   18006ac15:	48 8d 0d e4 53 f9 ff 	lea    -0x6ac1c(%rip),%rcx        # 0x180000000
   18006ac1c:	4c 89 45 e7          	mov    %r8,-0x19(%rbp)
   18006ac20:	4d 03 e8             	add    %r8,%r13
   18006ac23:	48 89 5d f7          	mov    %rbx,-0x9(%rbp)
   18006ac27:	4c 8b e3             	mov    %rbx,%r12
   18006ac2a:	4c 89 6d b7          	mov    %r13,-0x49(%rbp)
   18006ac2e:	4c 8d 34 c0          	lea    (%rax,%rax,8),%r14
   18006ac32:	49 c1 fc 06          	sar    $0x6,%r12
   18006ac36:	4a 8b 84 e1 30 7d 0a 	mov    0xa7d30(%rcx,%r12,8),%rax
   18006ac3d:	00 
   18006ac3e:	4a 8b 44 f0 28       	mov    0x28(%rax,%r14,8),%rax
   18006ac43:	48 89 45 bf          	mov    %rax,-0x41(%rbp)
   18006ac47:	ff 15 4b 95 00 00    	call   *0x954b(%rip)        # 0x180074198
   18006ac4d:	33 d2                	xor    %edx,%edx
   18006ac4f:	48 8d 4c 24 50       	lea    0x50(%rsp),%rcx
   18006ac54:	89 45 a7             	mov    %eax,-0x59(%rbp)
   18006ac57:	e8 60 f3 fe ff       	call   0x180059fbc
```

## `KERNEL32.dll!GetConsoleMode` (1 Call Sites)

### Line 123643 (Address `0x1800741a8`)
```assembly
   18006b5e2:	4a 8b 04 e8          	mov    (%rax,%r13,8),%rax
   18006b5e6:	42 38 5c f8 38       	cmp    %bl,0x38(%rax,%r15,8)
   18006b5eb:	0f 8d ed 00 00 00    	jge    0x18006b6de
   18006b5f1:	e8 06 be ff ff       	call   0x1800673fc
   18006b5f6:	48 8b 88 90 00 00 00 	mov    0x90(%rax),%rcx
   18006b5fd:	48 39 99 38 01 00 00 	cmp    %rbx,0x138(%rcx)
   18006b604:	75 16                	jne    0x18006b61c
   18006b606:	48 8d 05 23 c7 03 00 	lea    0x3c723(%rip),%rax        # 0x1800a7d30
   18006b60d:	4a 8b 04 e8          	mov    (%rax,%r13,8),%rax
   18006b611:	42 38 5c f8 39       	cmp    %bl,0x39(%rax,%r15,8)
   18006b616:	0f 84 c2 00 00 00    	je     0x18006b6de
   18006b61c:	48 8d 05 0d c7 03 00 	lea    0x3c70d(%rip),%rax        # 0x1800a7d30
   18006b623:	4a 8b 0c e8          	mov    (%rax,%r13,8),%rcx
   18006b627:	48 8d 55 f0          	lea    -0x10(%rbp),%rdx
   18006b62b:	4a 8b 4c f9 28       	mov    0x28(%rcx,%r15,8),%rcx
   18006b630:	ff 15 72 8b 00 00    	call   *0x8b72(%rip)        # 0x1800741a8
   18006b636:	85 c0                	test   %eax,%eax
   18006b638:	0f 84 a0 00 00 00    	je     0x18006b6de
   18006b63e:	40 84 f6             	test   %sil,%sil
   18006b641:	74 7d                	je     0x18006b6c0
```

## `KERNEL32.dll!GetCurrentProcess` (3 Call Sites)

### Line 97004 (Address `0x180074168`)
```assembly
   180055190:	48 8d 0d c1 21 05 00 	lea    0x521c1(%rip),%rcx        # 0x1800a7358
   180055197:	ff 15 33 ef 01 00    	call   *0x1ef33(%rip)        # 0x1800740d0
   18005519d:	48 8b 0d e4 21 05 00 	mov    0x521e4(%rip),%rcx        # 0x1800a7388
   1800551a4:	48 85 c9             	test   %rcx,%rcx
   1800551a7:	74 06                	je     0x1800551af
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
   1800551af:	48 83 c4 28          	add    $0x28,%rsp
   1800551b3:	c3                   	ret
   1800551b4:	40 53                	rex push %rbx
   1800551b6:	48 83 ec 20          	sub    $0x20,%rsp
   1800551ba:	48 8b d9             	mov    %rcx,%rbx
   1800551bd:	33 c9                	xor    %ecx,%ecx
   1800551bf:	ff 15 2b f0 01 00    	call   *0x1f02b(%rip)        # 0x1800741f0
   1800551c5:	48 8b cb             	mov    %rbx,%rcx
   1800551c8:	ff 15 1a f0 01 00    	call   *0x1f01a(%rip)        # 0x1800741e8
   1800551ce:	ff 15 94 ef 01 00    	call   *0x1ef94(%rip)        # 0x180074168
   1800551d4:	48 8b c8             	mov    %rax,%rcx
   1800551d7:	ba 09 04 00 c0       	mov    $0xc0000409,%edx
   1800551dc:	48 83 c4 20          	add    $0x20,%rsp
   1800551e0:	5b                   	pop    %rbx
```

### Line 107538 (Address `0x180074168`)
```assembly
   18005de2b:	33 c9                	xor    %ecx,%ecx
   18005de2d:	e8 02 00 00 00       	call   0x18005de34
   18005de32:	cc                   	int3
   18005de33:	cc                   	int3
   18005de34:	48 83 ec 28          	sub    $0x28,%rsp
   18005de38:	b9 17 00 00 00       	mov    $0x17,%ecx
   18005de3d:	ff 15 bd 63 01 00    	call   *0x163bd(%rip)        # 0x180074200
   18005de43:	85 c0                	test   %eax,%eax
   18005de45:	74 07                	je     0x18005de4e
   18005de47:	b9 05 00 00 00       	mov    $0x5,%ecx
   18005de4c:	cd 29                	int    $0x29
   18005de4e:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   18005de54:	ba 17 04 00 c0       	mov    $0xc0000417,%edx
   18005de59:	41 8d 48 01          	lea    0x1(%r8),%ecx
   18005de5d:	e8 6e fd ff ff       	call   0x18005dbd0
   18005de62:	ff 15 00 63 01 00    	call   *0x16300(%rip)        # 0x180074168
   18005de68:	48 8b c8             	mov    %rax,%rcx
   18005de6b:	ba 17 04 00 c0       	mov    $0xc0000417,%edx
   18005de70:	48 83 c4 28          	add    $0x28,%rsp
   18005de74:	48 ff 25 7d 63 01 00 	rex.W jmp *0x1637d(%rip)        # 0x1800741f8
```

### Line 109511 (Address `0x180074168`)
```assembly
   18005f8a4:	8b cb                	mov    %ebx,%ecx
   18005f8a6:	e8 01 00 00 00       	call   0x18005f8ac
   18005f8ab:	cc                   	int3
   18005f8ac:	40 53                	rex push %rbx
   18005f8ae:	48 83 ec 20          	sub    $0x20,%rsp
   18005f8b2:	8b d9                	mov    %ecx,%ebx
   18005f8b4:	e8 6b a7 00 00       	call   0x18006a024
   18005f8b9:	83 f8 01             	cmp    $0x1,%eax
   18005f8bc:	74 28                	je     0x18005f8e6
   18005f8be:	65 48 8b 04 25 60 00 	mov    %gs:0x60,%rax
   18005f8c5:	00 00 
   18005f8c7:	8b 90 bc 00 00 00    	mov    0xbc(%rax),%edx
   18005f8cd:	c1 ea 08             	shr    $0x8,%edx
   18005f8d0:	f6 c2 01             	test   $0x1,%dl
   18005f8d3:	75 11                	jne    0x18005f8e6
   18005f8d5:	ff 15 8d 48 01 00    	call   *0x1488d(%rip)        # 0x180074168
   18005f8db:	48 8b c8             	mov    %rax,%rcx
   18005f8de:	8b d3                	mov    %ebx,%edx
   18005f8e0:	ff 15 12 49 01 00    	call   *0x14912(%rip)        # 0x1800741f8
   18005f8e6:	8b cb                	mov    %ebx,%ecx
```

## `KERNEL32.dll!GetCurrentProcessId` (3 Call Sites)

### Line 29004 (Address `0x1800740e0`)
```assembly
   18001a60f:	cc                   	int3
   18001a610:	40 53                	rex push %rbx
   18001a612:	56                   	push   %rsi
   18001a613:	57                   	push   %rdi
   18001a614:	41 56                	push   %r14
   18001a616:	41 57                	push   %r15
   18001a618:	48 83 ec 60          	sub    $0x60,%rsp
   18001a61c:	48 c7 44 24 38 fe ff 	movq   $0xfffffffffffffffe,0x38(%rsp)
   18001a623:	ff ff 
   18001a625:	48 8b 05 34 bd 08 00 	mov    0x8bd34(%rip),%rax        # 0x1800a6360
   18001a62c:	48 33 c4             	xor    %rsp,%rax
   18001a62f:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
   18001a634:	4d 8b f8             	mov    %r8,%r15
   18001a637:	44 8b f2             	mov    %edx,%r14d
   18001a63a:	48 8b f1             	mov    %rcx,%rsi
   18001a63d:	ff 15 9d 9a 05 00    	call   *0x59a9d(%rip)        # 0x1800740e0
   18001a643:	8b f8                	mov    %eax,%edi
   18001a645:	ff 15 8d 9a 05 00    	call   *0x59a8d(%rip)        # 0x1800740d8
   18001a64b:	8b d8                	mov    %eax,%ebx
   18001a64d:	33 c0                	xor    %eax,%eax
```

### Line 37203 (Address `0x1800740e0`)
```assembly
   180021e3b:	cc                   	int3
   180021e3c:	cc                   	int3
   180021e3d:	cc                   	int3
   180021e3e:	cc                   	int3
   180021e3f:	cc                   	int3
   180021e40:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   180021e45:	56                   	push   %rsi
   180021e46:	57                   	push   %rdi
   180021e47:	41 56                	push   %r14
   180021e49:	48 83 ec 60          	sub    $0x60,%rsp
   180021e4d:	48 8b 05 0c 45 08 00 	mov    0x8450c(%rip),%rax        # 0x1800a6360
   180021e54:	48 33 c4             	xor    %rsp,%rax
   180021e57:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180021e5c:	49 8b f0             	mov    %r8,%rsi
   180021e5f:	4c 8b f1             	mov    %rcx,%r14
   180021e62:	ff 15 78 22 05 00    	call   *0x52278(%rip)        # 0x1800740e0
   180021e68:	8b f8                	mov    %eax,%edi
   180021e6a:	ff 15 68 22 05 00    	call   *0x52268(%rip)        # 0x1800740d8
   180021e70:	8b d8                	mov    %eax,%ebx
   180021e72:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
```

### Line 97665 (Address `0x1800740e0`)
```assembly
   180055a9a:	48 8b ec             	mov    %rsp,%rbp
   180055a9d:	48 83 ec 20          	sub    $0x20,%rsp
   180055aa1:	48 8b 05 b8 08 05 00 	mov    0x508b8(%rip),%rax        # 0x1800a6360
   180055aa8:	48 bb 32 a2 df 2d 99 	movabs $0x2b992ddfa232,%rbx
   180055aaf:	2b 00 00 
   180055ab2:	48 3b c3             	cmp    %rbx,%rax
   180055ab5:	75 74                	jne    0x180055b2b
   180055ab7:	48 83 65 18 00       	andq   $0x0,0x18(%rbp)
   180055abc:	48 8d 4d 18          	lea    0x18(%rbp),%rcx
   180055ac0:	ff 15 4a e7 01 00    	call   *0x1e74a(%rip)        # 0x180074210
   180055ac6:	48 8b 45 18          	mov    0x18(%rbp),%rax
   180055aca:	48 89 45 10          	mov    %rax,0x10(%rbp)
   180055ace:	ff 15 04 e6 01 00    	call   *0x1e604(%rip)        # 0x1800740d8
   180055ad4:	8b c0                	mov    %eax,%eax
   180055ad6:	48 31 45 10          	xor    %rax,0x10(%rbp)
   180055ada:	ff 15 00 e6 01 00    	call   *0x1e600(%rip)        # 0x1800740e0
   180055ae0:	8b c0                	mov    %eax,%eax
   180055ae2:	48 8d 4d 20          	lea    0x20(%rbp),%rcx
   180055ae6:	48 31 45 10          	xor    %rax,0x10(%rbp)
   180055aea:	ff 15 18 e7 01 00    	call   *0x1e718(%rip)        # 0x180074208
```

## `KERNEL32.dll!GetCurrentThreadId` (3 Call Sites)

### Line 29006 (Address `0x1800740d8`)
```assembly
   18001a612:	56                   	push   %rsi
   18001a613:	57                   	push   %rdi
   18001a614:	41 56                	push   %r14
   18001a616:	41 57                	push   %r15
   18001a618:	48 83 ec 60          	sub    $0x60,%rsp
   18001a61c:	48 c7 44 24 38 fe ff 	movq   $0xfffffffffffffffe,0x38(%rsp)
   18001a623:	ff ff 
   18001a625:	48 8b 05 34 bd 08 00 	mov    0x8bd34(%rip),%rax        # 0x1800a6360
   18001a62c:	48 33 c4             	xor    %rsp,%rax
   18001a62f:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
   18001a634:	4d 8b f8             	mov    %r8,%r15
   18001a637:	44 8b f2             	mov    %edx,%r14d
   18001a63a:	48 8b f1             	mov    %rcx,%rsi
   18001a63d:	ff 15 9d 9a 05 00    	call   *0x59a9d(%rip)        # 0x1800740e0
   18001a643:	8b f8                	mov    %eax,%edi
   18001a645:	ff 15 8d 9a 05 00    	call   *0x59a8d(%rip)        # 0x1800740d8
   18001a64b:	8b d8                	mov    %eax,%ebx
   18001a64d:	33 c0                	xor    %eax,%eax
   18001a64f:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001a654:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
```

### Line 37205 (Address `0x1800740d8`)
```assembly
   180021e3d:	cc                   	int3
   180021e3e:	cc                   	int3
   180021e3f:	cc                   	int3
   180021e40:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   180021e45:	56                   	push   %rsi
   180021e46:	57                   	push   %rdi
   180021e47:	41 56                	push   %r14
   180021e49:	48 83 ec 60          	sub    $0x60,%rsp
   180021e4d:	48 8b 05 0c 45 08 00 	mov    0x8450c(%rip),%rax        # 0x1800a6360
   180021e54:	48 33 c4             	xor    %rsp,%rax
   180021e57:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180021e5c:	49 8b f0             	mov    %r8,%rsi
   180021e5f:	4c 8b f1             	mov    %rcx,%r14
   180021e62:	ff 15 78 22 05 00    	call   *0x52278(%rip)        # 0x1800740e0
   180021e68:	8b f8                	mov    %eax,%edi
   180021e6a:	ff 15 68 22 05 00    	call   *0x52268(%rip)        # 0x1800740d8
   180021e70:	8b d8                	mov    %eax,%ebx
   180021e72:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180021e77:	33 c0                	xor    %eax,%eax
   180021e79:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
```

### Line 97662 (Address `0x1800740d8`)
```assembly
   180055a93:	cc                   	int3
   180055a94:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180055a99:	55                   	push   %rbp
   180055a9a:	48 8b ec             	mov    %rsp,%rbp
   180055a9d:	48 83 ec 20          	sub    $0x20,%rsp
   180055aa1:	48 8b 05 b8 08 05 00 	mov    0x508b8(%rip),%rax        # 0x1800a6360
   180055aa8:	48 bb 32 a2 df 2d 99 	movabs $0x2b992ddfa232,%rbx
   180055aaf:	2b 00 00 
   180055ab2:	48 3b c3             	cmp    %rbx,%rax
   180055ab5:	75 74                	jne    0x180055b2b
   180055ab7:	48 83 65 18 00       	andq   $0x0,0x18(%rbp)
   180055abc:	48 8d 4d 18          	lea    0x18(%rbp),%rcx
   180055ac0:	ff 15 4a e7 01 00    	call   *0x1e74a(%rip)        # 0x180074210
   180055ac6:	48 8b 45 18          	mov    0x18(%rbp),%rax
   180055aca:	48 89 45 10          	mov    %rax,0x10(%rbp)
   180055ace:	ff 15 04 e6 01 00    	call   *0x1e604(%rip)        # 0x1800740d8
   180055ad4:	8b c0                	mov    %eax,%eax
   180055ad6:	48 31 45 10          	xor    %rax,0x10(%rbp)
   180055ada:	ff 15 00 e6 01 00    	call   *0x1e600(%rip)        # 0x1800740e0
   180055ae0:	8b c0                	mov    %eax,%eax
```

## `KERNEL32.dll!GetEnvironmentStringsW` (1 Call Sites)

### Line 125702 (Address `0x180074018`)
```assembly
   18006d219:	ff 15 01 6e 00 00    	call   *0x6e01(%rip)        # 0x180074020
   18006d21f:	48 89 05 72 b3 03 00 	mov    %rax,0x3b372(%rip)        # 0x1800a8598
   18006d226:	b0 01                	mov    $0x1,%al
   18006d228:	48 83 c4 28          	add    $0x28,%rsp
   18006d22c:	c3                   	ret
   18006d22d:	cc                   	int3
   18006d22e:	cc                   	int3
   18006d22f:	cc                   	int3
   18006d230:	48 8b c4             	mov    %rsp,%rax
   18006d233:	48 89 58 08          	mov    %rbx,0x8(%rax)
   18006d237:	48 89 68 10          	mov    %rbp,0x10(%rax)
   18006d23b:	48 89 70 18          	mov    %rsi,0x18(%rax)
   18006d23f:	48 89 78 20          	mov    %rdi,0x20(%rax)
   18006d243:	41 56                	push   %r14
   18006d245:	48 83 ec 40          	sub    $0x40,%rsp
   18006d249:	ff 15 c9 6d 00 00    	call   *0x6dc9(%rip)        # 0x180074018
   18006d24f:	45 33 f6             	xor    %r14d,%r14d
   18006d252:	48 8b d8             	mov    %rax,%rbx
   18006d255:	48 85 c0             	test   %rax,%rax
   18006d258:	0f 84 a4 00 00 00    	je     0x18006d302
```

## `KERNEL32.dll!GetFileSizeEx` (3 Call Sites)

### Line 25191 (Address `0x180074048`)
```assembly
   18001711e:	c7 44 24 28 80 00 00 	movl   $0x80,0x28(%rsp)
   180017125:	00 
   180017126:	c7 44 24 20 03 00 00 	movl   $0x3,0x20(%rsp)
   18001712d:	00 
   18001712e:	45 33 c9             	xor    %r9d,%r9d
   180017131:	ba 00 00 00 80       	mov    $0x80000000,%edx
   180017136:	45 8d 41 01          	lea    0x1(%r9),%r8d
   18001713a:	48 8b 4e 18          	mov    0x18(%rsi),%rcx
   18001713e:	ff 15 bc cf 05 00    	call   *0x5cfbc(%rip)        # 0x180074100
   180017144:	48 89 46 08          	mov    %rax,0x8(%rsi)
   180017148:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18001714c:	0f 84 61 02 00 00    	je     0x1800173b3
   180017152:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180017157:	48 8d 54 24 50       	lea    0x50(%rsp),%rdx
   18001715c:	48 8b c8             	mov    %rax,%rcx
   18001715f:	ff 15 e3 ce 05 00    	call   *0x5cee3(%rip)        # 0x180074048
   180017165:	83 7c 24 50 00       	cmpl   $0x0,0x50(%rsp)
   18001716a:	0f 86 ac 00 00 00    	jbe    0x18001721c
   180017170:	8b df                	mov    %edi,%ebx
   180017172:	44 8b f7             	mov    %edi,%r14d
```

### Line 37888 (Address `0x180074048`)
```assembly
   180022810:	41 b9 02 00 00 00    	mov    $0x2,%r9d
   180022816:	45 33 c0             	xor    %r8d,%r8d
   180022819:	33 d2                	xor    %edx,%edx
   18002281b:	48 8b c8             	mov    %rax,%rcx
   18002281e:	ff 15 d4 18 05 00    	call   *0x518d4(%rip)        # 0x1800740f8
   180022824:	8b d8                	mov    %eax,%ebx
   180022826:	ff 15 dc 18 05 00    	call   *0x518dc(%rip)        # 0x180074108
   18002282c:	83 fb ff             	cmp    $0xffffffff,%ebx
   18002282f:	75 08                	jne    0x180022839
   180022831:	85 c0                	test   %eax,%eax
   180022833:	0f 85 6b 03 00 00    	jne    0x180022ba4
   180022839:	4c 89 be 90 00 00 00 	mov    %r15,0x90(%rsi)
   180022840:	48 8d 94 24 08 02 00 	lea    0x208(%rsp),%rdx
   180022847:	00 
   180022848:	49 8b 4f 08          	mov    0x8(%r15),%rcx
   18002284c:	ff 15 f6 17 05 00    	call   *0x517f6(%rip)        # 0x180074048
   180022852:	48 81 bc 24 08 02 00 	cmpq   $0x100000,0x208(%rsp)
   180022859:	00 00 00 10 00 
   18002285e:	0f 8e ac 00 00 00    	jle    0x180022910
   180022864:	48 8b 8e 90 00 00 00 	mov    0x90(%rsi),%rcx
```

### Line 123944 (Address `0x180074048`)
```assembly
   18006b9fb:	74 4a                	je     0x18006ba47
   18006b9fd:	8b 49 18             	mov    0x18(%rcx),%ecx
   18006ba00:	e8 df 3f 00 00       	call   0x18006f9e4
   18006ba05:	48 8b d8             	mov    %rax,%rbx
   18006ba08:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18006ba0c:	74 39                	je     0x18006ba47
   18006ba0e:	33 d2                	xor    %edx,%edx
   18006ba10:	4c 8d 44 24 38       	lea    0x38(%rsp),%r8
   18006ba15:	48 8b c8             	mov    %rax,%rcx
   18006ba18:	44 8d 4a 01          	lea    0x1(%rdx),%r9d
   18006ba1c:	ff 15 6e 87 00 00    	call   *0x876e(%rip)        # 0x180074190
   18006ba22:	85 c0                	test   %eax,%eax
   18006ba24:	74 21                	je     0x18006ba47
   18006ba26:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   18006ba2b:	48 8b cb             	mov    %rbx,%rcx
   18006ba2e:	ff 15 14 86 00 00    	call   *0x8614(%rip)        # 0x180074048
   18006ba34:	85 c0                	test   %eax,%eax
   18006ba36:	74 0f                	je     0x18006ba47
   18006ba38:	48 8b 44 24 30       	mov    0x30(%rsp),%rax
   18006ba3d:	48 39 44 24 38       	cmp    %rax,0x38(%rsp)
```

## `KERNEL32.dll!GetFileType` (3 Call Sites)

### Line 109023 (Address `0x180074290`)
```assembly
   18005f245:	48 33 c4             	xor    %rsp,%rax
   18005f248:	48 89 85 e0 03 00 00 	mov    %rax,0x3e0(%rbp)
   18005f24f:	48 8b f9             	mov    %rcx,%rdi
   18005f252:	48 89 4c 24 48       	mov    %rcx,0x48(%rsp)
   18005f257:	b9 f4 ff ff ff       	mov    $0xfffffff4,%ecx
   18005f25c:	48 89 54 24 40       	mov    %rdx,0x40(%rsp)
   18005f261:	45 8b f0             	mov    %r8d,%r14d
   18005f264:	44 89 44 24 38       	mov    %r8d,0x38(%rsp)
   18005f269:	48 8b f2             	mov    %rdx,%rsi
   18005f26c:	ff 15 16 50 01 00    	call   *0x15016(%rip)        # 0x180074288
   18005f272:	48 8b d8             	mov    %rax,%rbx
   18005f275:	48 8d 48 ff          	lea    -0x1(%rax),%rcx
   18005f279:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
   18005f27d:	77 72                	ja     0x18005f2f1
   18005f27f:	48 8b c8             	mov    %rax,%rcx
   18005f282:	ff 15 08 50 01 00    	call   *0x15008(%rip)        # 0x180074290
   18005f288:	83 f8 02             	cmp    $0x2,%eax
   18005f28b:	75 64                	jne    0x18005f2f1
   18005f28d:	44 89 74 24 28       	mov    %r14d,0x28(%rsp)
   18005f292:	4c 8d 05 b7 3e 03 00 	lea    0x33eb7(%rip),%r8        # 0x180093150
```

### Line 120214 (Address `0x180074290`)
```assembly
   180068735:	e8 f6 70 00 00       	call   0x18006f830
   18006873a:	3b 3d f0 f9 03 00    	cmp    0x3f9f0(%rip),%edi        # 0x1800a8130
   180068740:	0f 4f 3d e9 f9 03 00 	cmovg  0x3f9e9(%rip),%edi        # 0x1800a8130
   180068747:	85 ff                	test   %edi,%edi
   180068749:	74 60                	je     0x1800687ab
   18006874b:	41 8b ee             	mov    %r14d,%ebp
   18006874e:	48 83 3b ff          	cmpq   $0xffffffffffffffff,(%rbx)
   180068752:	74 47                	je     0x18006879b
   180068754:	48 83 3b fe          	cmpq   $0xfffffffffffffffe,(%rbx)
   180068758:	74 41                	je     0x18006879b
   18006875a:	f6 06 01             	testb  $0x1,(%rsi)
   18006875d:	74 3c                	je     0x18006879b
   18006875f:	f6 06 08             	testb  $0x8,(%rsi)
   180068762:	75 0d                	jne    0x180068771
   180068764:	48 8b 0b             	mov    (%rbx),%rcx
   180068767:	ff 15 23 bb 00 00    	call   *0xbb23(%rip)        # 0x180074290
   18006876d:	85 c0                	test   %eax,%eax
   18006876f:	74 2a                	je     0x18006879b
   180068771:	48 8b c5             	mov    %rbp,%rax
   180068774:	4c 8d 05 b5 f5 03 00 	lea    0x3f5b5(%rip),%r8        # 0x1800a7d30
```

### Line 120285 (Address `0x180074290`)
```assembly
   180068828:	74 16                	je     0x180068840
   18006882a:	83 e9 01             	sub    $0x1,%ecx
   18006882d:	74 0a                	je     0x180068839
   18006882f:	83 f9 01             	cmp    $0x1,%ecx
   180068832:	b9 f4 ff ff ff       	mov    $0xfffffff4,%ecx
   180068837:	eb 0c                	jmp    0x180068845
   180068839:	b9 f5 ff ff ff       	mov    $0xfffffff5,%ecx
   18006883e:	eb 05                	jmp    0x180068845
   180068840:	b9 f6 ff ff ff       	mov    $0xfffffff6,%ecx
   180068845:	ff 15 3d ba 00 00    	call   *0xba3d(%rip)        # 0x180074288
   18006884b:	48 8b e8             	mov    %rax,%rbp
   18006884e:	48 8d 48 01          	lea    0x1(%rax),%rcx
   180068852:	48 83 f9 01          	cmp    $0x1,%rcx
   180068856:	76 0b                	jbe    0x180068863
   180068858:	48 8b c8             	mov    %rax,%rcx
   18006885b:	ff 15 2f ba 00 00    	call   *0xba2f(%rip)        # 0x180074290
   180068861:	eb 02                	jmp    0x180068865
   180068863:	33 c0                	xor    %eax,%eax
   180068865:	85 c0                	test   %eax,%eax
   180068867:	74 20                	je     0x180068889
```

## `KERNEL32.dll!GetLastError` (39 Call Sites)

### Line 26916 (Address `0x180074108`)
```assembly
   180018947:	48 8b 0d 42 e4 08 00 	mov    0x8e442(%rip),%rcx        # 0x1800a6d90
   18001894e:	48 8d 44 24 54       	lea    0x54(%rsp),%rax
   180018953:	48 c7 44 24 38 00 00 	movq   $0x0,0x38(%rsp)
   18001895a:	00 00 
   18001895c:	44 8b cf             	mov    %edi,%r9d
   18001895f:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   180018964:	4c 8b c3             	mov    %rbx,%r8
   180018967:	48 8d 44 24 60       	lea    0x60(%rsp),%rax
   18001896c:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   180018973:	00 
   180018974:	ba 54 40 30 00       	mov    $0x304054,%edx
   180018979:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001897e:	ff 15 9c b7 05 00    	call   *0x5b79c(%rip)        # 0x180074120
   180018984:	85 c0                	test   %eax,%eax
   180018986:	75 2f                	jne    0x1800189b7
   180018988:	ff 15 7a b7 05 00    	call   *0x5b77a(%rip)        # 0x180074108
   18001898e:	48 8b 0d 73 fc 08 00 	mov    0x8fc73(%rip),%rcx        # 0x1800a8608
   180018995:	48 8d 15 34 3f 08 00 	lea    0x83f34(%rip),%rdx        # 0x18009c8d0
   18001899c:	44 8b c0             	mov    %eax,%r8d
   18001899f:	e8 ec d8 ff ff       	call   0x180016290
```

### Line 27427 (Address `0x180074108`)
```assembly
   180019090:	89 9d e0 03 00 00    	mov    %ebx,0x3e0(%rbp)
   180019096:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   18001909b:	48 8d 44 24 60       	lea    0x60(%rsp),%rax
   1800190a0:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800190a5:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800190ac:	00 
   1800190ad:	48 8d 85 f0 04 00 00 	lea    0x4f0(%rbp),%rax
   1800190b4:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800190b9:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800190bf:	4c 8d 85 e0 03 00 00 	lea    0x3e0(%rbp),%r8
   1800190c6:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800190cb:	48 8b 0d be dc 08 00 	mov    0x8dcbe(%rip),%rcx        # 0x1800a6d90
   1800190d2:	ff 15 48 b0 05 00    	call   *0x5b048(%rip)        # 0x180074120
   1800190d8:	85 c0                	test   %eax,%eax
   1800190da:	75 24                	jne    0x180019100
   1800190dc:	ff 15 26 b0 05 00    	call   *0x5b026(%rip)        # 0x180074108
   1800190e2:	44 8b c0             	mov    %eax,%r8d
   1800190e5:	48 8d 15 a4 35 08 00 	lea    0x835a4(%rip),%rdx        # 0x18009c690
   1800190ec:	48 8b 0d 15 f5 08 00 	mov    0x8f515(%rip),%rcx        # 0x1800a8608
   1800190f3:	e8 98 d1 ff ff       	call   0x180016290
```

### Line 27539 (Address `0x180074108`)
```assembly
   18001929f:	66 89 b5 b4 00 00 00 	mov    %si,0xb4(%rbp)
   1800192a6:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   1800192ab:	48 8d 44 24 68       	lea    0x68(%rsp),%rax
   1800192b0:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800192b5:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800192bc:	00 
   1800192bd:	48 8d 85 c0 01 00 00 	lea    0x1c0(%rbp),%rax
   1800192c4:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800192c9:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800192cf:	4c 8d 85 b0 00 00 00 	lea    0xb0(%rbp),%r8
   1800192d6:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800192db:	48 8b 0d ae da 08 00 	mov    0x8daae(%rip),%rcx        # 0x1800a6d90
   1800192e2:	ff 15 38 ae 05 00    	call   *0x5ae38(%rip)        # 0x180074120
   1800192e8:	85 c0                	test   %eax,%eax
   1800192ea:	75 15                	jne    0x180019301
   1800192ec:	ff 15 16 ae 05 00    	call   *0x5ae16(%rip)        # 0x180074108
   1800192f2:	44 8b c0             	mov    %eax,%r8d
   1800192f5:	48 8d 15 54 34 08 00 	lea    0x83454(%rip),%rdx        # 0x18009c750
   1800192fc:	e9 b0 00 00 00       	jmp    0x1800193b1
   180019301:	0f b7 85 c0 01 00 00 	movzwl 0x1c0(%rbp),%eax
```

### Line 27726 (Address `0x180074108`)
```assembly
   1800195bc:	33 f6                	xor    %esi,%esi
   1800195be:	48 8d 8c 24 70 02 00 	lea    0x270(%rsp),%rcx
   1800195c5:	00 
   1800195c6:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
   1800195cb:	45 33 c9             	xor    %r9d,%r9d
   1800195ce:	c7 44 24 28 20 00 00 	movl   $0x20,0x28(%rsp)
   1800195d5:	00 
   1800195d6:	ba 00 00 00 10       	mov    $0x10000000,%edx
   1800195db:	c7 44 24 20 01 00 00 	movl   $0x1,0x20(%rsp)
   1800195e2:	00 
   1800195e3:	44 8d 46 03          	lea    0x3(%rsi),%r8d
   1800195e7:	ff 15 13 ab 05 00    	call   *0x5ab13(%rip)        # 0x180074100
   1800195ed:	48 89 05 9c d7 08 00 	mov    %rax,0x8d79c(%rip)        # 0x1800a6d90
   1800195f4:	48 3b c3             	cmp    %rbx,%rax
   1800195f7:	75 3c                	jne    0x180019635
   1800195f9:	ff 15 09 ab 05 00    	call   *0x5ab09(%rip)        # 0x180074108
   1800195ff:	48 8b 0d 02 f0 08 00 	mov    0x8f002(%rip),%rcx        # 0x1800a8608
   180019606:	48 8d 15 93 2f 08 00 	lea    0x82f93(%rip),%rdx        # 0x18009c5a0
   18001960d:	44 8b c0             	mov    %eax,%r8d
   180019610:	e8 7b cc ff ff       	call   0x180016290
```

### Line 27757 (Address `0x180074108`)
```assembly
   180019650:	00 
   180019651:	48 89 ac 24 98 04 00 	mov    %rbp,0x498(%rsp)
   180019658:	00 
   180019659:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   180019660:	00 
   180019661:	bd 01 10 00 00       	mov    $0x1001,%ebp
   180019666:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   18001966b:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   180019671:	48 8b c8             	mov    %rax,%rcx
   180019674:	89 74 24 40          	mov    %esi,0x40(%rsp)
   180019678:	ba 54 40 30 00       	mov    $0x304054,%edx
   18001967d:	89 6c 24 50          	mov    %ebp,0x50(%rsp)
   180019681:	ff 15 99 aa 05 00    	call   *0x5aa99(%rip)        # 0x180074120
   180019687:	85 c0                	test   %eax,%eax
   180019689:	75 12                	jne    0x18001969d
   18001968b:	ff 15 77 aa 05 00    	call   *0x5aa77(%rip)        # 0x180074108
   180019691:	44 8b c0             	mov    %eax,%r8d
   180019694:	48 8d 15 35 2f 08 00 	lea    0x82f35(%rip),%rdx        # 0x18009c5d0
   18001969b:	eb 18                	jmp    0x1800196b5
   18001969d:	0f b7 84 24 60 01 00 	movzwl 0x160(%rsp),%eax
```

### Line 29233 (Address `0x180074108`)
```assembly
   18001a8f0:	4c 8b dc             	mov    %rsp,%r11
   18001a8f3:	48 81 ec 98 00 00 00 	sub    $0x98,%rsp
   18001a8fa:	49 c7 43 98 fe ff ff 	movq   $0xfffffffffffffffe,-0x68(%r11)
   18001a901:	ff 
   18001a902:	41 8b c0             	mov    %r8d,%eax
   18001a905:	4c 3b c0             	cmp    %rax,%r8
   18001a908:	75 74                	jne    0x18001a97e
   18001a90a:	33 c0                	xor    %eax,%eax
   18001a90c:	41 89 43 18          	mov    %eax,0x18(%r11)
   18001a910:	49 89 43 88          	mov    %rax,-0x78(%r11)
   18001a914:	4d 8d 4b 18          	lea    0x18(%r11),%r9
   18001a918:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   18001a91c:	ff 15 c6 97 05 00    	call   *0x597c6(%rip)        # 0x1800740e8
   18001a922:	85 c0                	test   %eax,%eax
   18001a924:	75 0d                	jne    0x18001a933
   18001a926:	ff 15 dc 97 05 00    	call   *0x597dc(%rip)        # 0x180074108
   18001a92c:	83 f8 26             	cmp    $0x26,%eax
   18001a92f:	74 31                	je     0x18001a962
   18001a931:	eb 6e                	jmp    0x18001a9a1
   18001a933:	8b 84 24 b0 00 00 00 	mov    0xb0(%rsp),%eax
```

### Line 29440 (Address `0x180074108`)
```assembly
   18001abf0:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001abf5:	4c 8d 05 84 c1 08 00 	lea    0x8c184(%rip),%r8        # 0x1800a6d80
   18001abfc:	33 d2                	xor    %edx,%edx
   18001abfe:	48 8b cd             	mov    %rbp,%rcx
   18001ac01:	ff 15 d1 96 05 00    	call   *0x596d1(%rip)        # 0x1800742d8
   18001ac07:	85 c0                	test   %eax,%eax
   18001ac09:	0f 84 7c 01 00 00    	je     0x18001ad8b
   18001ac0f:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001ac14:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
   18001ac19:	45 33 c9             	xor    %r9d,%r9d
   18001ac1c:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001ac21:	45 33 c0             	xor    %r8d,%r8d
   18001ac24:	48 8d 54 24 38       	lea    0x38(%rsp),%rdx
   18001ac29:	48 8b cd             	mov    %rbp,%rcx
   18001ac2c:	ff 15 be 96 05 00    	call   *0x596be(%rip)        # 0x1800742f0
   18001ac32:	ff 15 d0 94 05 00    	call   *0x594d0(%rip)        # 0x180074108
   18001ac38:	83 f8 7a             	cmp    $0x7a,%eax
   18001ac3b:	74 21                	je     0x18001ac5e
   18001ac3d:	ff 15 c5 94 05 00    	call   *0x594c5(%rip)        # 0x180074108
   18001ac43:	48 8b 0d be d9 08 00 	mov    0x8d9be(%rip),%rcx        # 0x1800a8608
```

### Line 29443 (Address `0x180074108`)
```assembly
   18001abfe:	48 8b cd             	mov    %rbp,%rcx
   18001ac01:	ff 15 d1 96 05 00    	call   *0x596d1(%rip)        # 0x1800742d8
   18001ac07:	85 c0                	test   %eax,%eax
   18001ac09:	0f 84 7c 01 00 00    	je     0x18001ad8b
   18001ac0f:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001ac14:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
   18001ac19:	45 33 c9             	xor    %r9d,%r9d
   18001ac1c:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001ac21:	45 33 c0             	xor    %r8d,%r8d
   18001ac24:	48 8d 54 24 38       	lea    0x38(%rsp),%rdx
   18001ac29:	48 8b cd             	mov    %rbp,%rcx
   18001ac2c:	ff 15 be 96 05 00    	call   *0x596be(%rip)        # 0x1800742f0
   18001ac32:	ff 15 d0 94 05 00    	call   *0x594d0(%rip)        # 0x180074108
   18001ac38:	83 f8 7a             	cmp    $0x7a,%eax
   18001ac3b:	74 21                	je     0x18001ac5e
   18001ac3d:	ff 15 c5 94 05 00    	call   *0x594c5(%rip)        # 0x180074108
   18001ac43:	48 8b 0d be d9 08 00 	mov    0x8d9be(%rip),%rcx        # 0x1800a8608
   18001ac4a:	48 8d 15 9f 17 08 00 	lea    0x8179f(%rip),%rdx        # 0x18009c3f0
   18001ac51:	44 8b c0             	mov    %eax,%r8d
   18001ac54:	e8 37 b6 ff ff       	call   0x180016290
```

### Line 29473 (Address `0x180074108`)
```assembly
   18001ac84:	ff 15 9e 94 05 00    	call   *0x5949e(%rip)        # 0x180074128
   18001ac8a:	48 8b d8             	mov    %rax,%rbx
   18001ac8d:	48 85 c0             	test   %rax,%rax
   18001ac90:	0f 84 c9 00 00 00    	je     0x18001ad5f
   18001ac96:	c7 00 08 00 00 00    	movl   $0x8,(%rax)
   18001ac9c:	48 8d 54 24 38       	lea    0x38(%rsp),%rdx
   18001aca1:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001aca6:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
   18001acab:	45 8b ce             	mov    %r14d,%r9d
   18001acae:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001acb3:	4c 8b c3             	mov    %rbx,%r8
   18001acb6:	48 8b cd             	mov    %rbp,%rcx
   18001acb9:	ff 15 31 96 05 00    	call   *0x59631(%rip)        # 0x1800742f0
   18001acbf:	85 c0                	test   %eax,%eax
   18001acc1:	75 1e                	jne    0x18001ace1
   18001acc3:	ff 15 3f 94 05 00    	call   *0x5943f(%rip)        # 0x180074108
   18001acc9:	48 8b 0d 38 d9 08 00 	mov    0x8d938(%rip),%rcx        # 0x1800a8608
   18001acd0:	48 8d 15 19 17 08 00 	lea    0x81719(%rip),%rdx        # 0x18009c3f0
   18001acd7:	44 8b c0             	mov    %eax,%r8d
   18001acda:	e8 b1 b5 ff ff       	call   0x180016290
```

### Line 29512 (Address `0x180074108`)
```assembly
   18001ad24:	45 0f 45 c7          	cmovne %r15d,%r8d
   18001ad28:	66 44 89 38          	mov    %r15w,(%rax)
   18001ad2c:	75 18                	jne    0x18001ad46
   18001ad2e:	48 8b 0d d3 d8 08 00 	mov    0x8d8d3(%rip),%rcx        # 0x1800a8608
   18001ad35:	48 8d 15 b4 17 08 00 	lea    0x817b4(%rip),%rdx        # 0x18009c4f0
   18001ad3c:	e8 4f b5 ff ff       	call   0x180016290
   18001ad41:	40 32 f6             	xor    %sil,%sil
   18001ad44:	eb 03                	jmp    0x18001ad49
   18001ad46:	40 b6 01             	mov    $0x1,%sil
   18001ad49:	ff 15 e1 93 05 00    	call   *0x593e1(%rip)        # 0x180074130
   18001ad4f:	4c 8b c3             	mov    %rbx,%r8
   18001ad52:	33 d2                	xor    %edx,%edx
   18001ad54:	48 8b c8             	mov    %rax,%rcx
   18001ad57:	ff 15 bb 93 05 00    	call   *0x593bb(%rip)        # 0x180074118
   18001ad5d:	eb 1c                	jmp    0x18001ad7b
   18001ad5f:	ff 15 a3 93 05 00    	call   *0x593a3(%rip)        # 0x180074108
   18001ad65:	48 8b 0d 9c d8 08 00 	mov    0x8d89c(%rip),%rcx        # 0x1800a8608
   18001ad6c:	48 8d 15 0d 17 08 00 	lea    0x8170d(%rip),%rdx        # 0x18009c480
   18001ad73:	44 8b c0             	mov    %eax,%r8d
   18001ad76:	e8 15 b5 ff ff       	call   0x180016290
```

### Line 36421 (Address `0x180074108`)
```assembly
   1800213b5:	48 8d 84 24 70 02 00 	lea    0x270(%rsp),%rax
   1800213bc:	00 
   1800213bd:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   1800213c4:	00 
   1800213c5:	8d 7e 02             	lea    0x2(%rsi),%edi
   1800213c8:	41 b9 04 01 00 00    	mov    $0x104,%r9d
   1800213ce:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800213d3:	ba 54 40 30 00       	mov    $0x304054,%edx
   1800213d8:	89 74 24 40          	mov    %esi,0x40(%rsp)
   1800213dc:	bd 04 10 00 00       	mov    $0x1004,%ebp
   1800213e1:	c7 44 24 50 04 10 02 	movl   $0x21004,0x50(%rsp)
   1800213e8:	00 
   1800213e9:	ff 15 31 2d 05 00    	call   *0x52d31(%rip)        # 0x180074120
   1800213ef:	85 c0                	test   %eax,%eax
   1800213f1:	75 26                	jne    0x180021419
   1800213f3:	ff 15 0f 2d 05 00    	call   *0x52d0f(%rip)        # 0x180074108
   1800213f9:	48 8d 15 10 b4 07 00 	lea    0x7b410(%rip),%rdx        # 0x18009c810
   180021400:	48 8b 0d 01 72 08 00 	mov    0x87201(%rip),%rcx        # 0x1800a8608
   180021407:	44 8b c0             	mov    %eax,%r8d
   18002140a:	e8 81 4e ff ff       	call   0x180016290
```

### Line 36496 (Address `0x180074108`)
```assembly
   1800214ec:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800214f1:	48 8d 44 24 44       	lea    0x44(%rsp),%rax
   1800214f6:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   1800214fb:	bd 07 10 00 00       	mov    $0x1007,%ebp
   180021500:	48 8d 84 24 80 03 00 	lea    0x380(%rsp),%rax
   180021507:	00 
   180021508:	c7 44 24 28 04 01 00 	movl   $0x104,0x28(%rsp)
   18002150f:	00 
   180021510:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   180021515:	89 74 24 44          	mov    %esi,0x44(%rsp)
   180021519:	c7 84 24 60 01 00 00 	movl   $0x21007,0x160(%rsp)
   180021520:	07 10 02 00 
   180021524:	ff 15 f6 2b 05 00    	call   *0x52bf6(%rip)        # 0x180074120
   18002152a:	85 c0                	test   %eax,%eax
   18002152c:	75 12                	jne    0x180021540
   18002152e:	ff 15 d4 2b 05 00    	call   *0x52bd4(%rip)        # 0x180074108
   180021534:	48 8d 15 15 b2 07 00 	lea    0x7b215(%rip),%rdx        # 0x18009c750
   18002153b:	e9 c0 fe ff ff       	jmp    0x180021400
   180021540:	0f b7 84 24 80 03 00 	movzwl 0x380(%rsp),%eax
   180021547:	00 
```

### Line 37879 (Address `0x180074108`)
```assembly
   1800227eb:	00 
   1800227ec:	45 33 c9             	xor    %r9d,%r9d
   1800227ef:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   1800227f4:	45 8d 41 01          	lea    0x1(%r9),%r8d
   1800227f8:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   1800227fc:	ff 15 fe 18 05 00    	call   *0x518fe(%rip)        # 0x180074100
   180022802:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022806:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18002280a:	0f 84 78 03 00 00    	je     0x180022b88
   180022810:	41 b9 02 00 00 00    	mov    $0x2,%r9d
   180022816:	45 33 c0             	xor    %r8d,%r8d
   180022819:	33 d2                	xor    %edx,%edx
   18002281b:	48 8b c8             	mov    %rax,%rcx
   18002281e:	ff 15 d4 18 05 00    	call   *0x518d4(%rip)        # 0x1800740f8
   180022824:	8b d8                	mov    %eax,%ebx
   180022826:	ff 15 dc 18 05 00    	call   *0x518dc(%rip)        # 0x180074108
   18002282c:	83 fb ff             	cmp    $0xffffffff,%ebx
   18002282f:	75 08                	jne    0x180022839
   180022831:	85 c0                	test   %eax,%eax
   180022833:	0f 85 6b 03 00 00    	jne    0x180022ba4
```

### Line 38063 (Address `0x180074108`)
```assembly
   180022ab0:	00 
   180022ab1:	45 33 c9             	xor    %r9d,%r9d
   180022ab4:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   180022ab9:	45 8d 41 01          	lea    0x1(%r9),%r8d
   180022abd:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   180022ac1:	ff 15 39 16 05 00    	call   *0x51639(%rip)        # 0x180074100
   180022ac7:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022acb:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   180022acf:	0f 84 15 01 00 00    	je     0x180022bea
   180022ad5:	41 b9 02 00 00 00    	mov    $0x2,%r9d
   180022adb:	45 33 c0             	xor    %r8d,%r8d
   180022ade:	33 d2                	xor    %edx,%edx
   180022ae0:	48 8b c8             	mov    %rax,%rcx
   180022ae3:	ff 15 0f 16 05 00    	call   *0x5160f(%rip)        # 0x1800740f8
   180022ae9:	8b d8                	mov    %eax,%ebx
   180022aeb:	ff 15 17 16 05 00    	call   *0x51617(%rip)        # 0x180074108
   180022af1:	83 fb ff             	cmp    $0xffffffff,%ebx
   180022af4:	75 08                	jne    0x180022afe
   180022af6:	85 c0                	test   %eax,%eax
   180022af8:	0f 85 0e 01 00 00    	jne    0x180022c0c
```

### Line 39176 (Address `0x180074108`)
```assembly
   18002387d:	cc                   	int3
   18002387e:	cc                   	int3
   18002387f:	cc                   	int3
   180023880:	48 8d 05 49 8b 07 00 	lea    0x78b49(%rip),%rax        # 0x18009c3d0
   180023887:	48 89 01             	mov    %rax,(%rcx)
   18002388a:	e9 41 e0 ff ff       	jmp    0x1800218d0
   18002388f:	cc                   	int3
   180023890:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   180023895:	57                   	push   %rdi
   180023896:	48 81 ec 50 08 00 00 	sub    $0x850,%rsp
   18002389d:	48 8b 05 bc 2a 08 00 	mov    0x82abc(%rip),%rax        # 0x1800a6360
   1800238a4:	48 33 c4             	xor    %rsp,%rax
   1800238a7:	48 89 84 24 40 08 00 	mov    %rax,0x840(%rsp)
   1800238ae:	00 
   1800238af:	48 8b f9             	mov    %rcx,%rdi
   1800238b2:	ff 15 50 08 05 00    	call   *0x50850(%rip)        # 0x180074108
   1800238b8:	48 c7 44 24 30 00 00 	movq   $0x0,0x30(%rsp)
   1800238bf:	00 00 
   1800238c1:	41 b9 09 04 00 00    	mov    $0x409,%r9d
   1800238c7:	8b d8                	mov    %eax,%ebx
```

### Line 39239 (Address `0x180074108`)
```assembly
   18002395b:	48 8d 05 d6 77 07 00 	lea    0x777d6(%rip),%rax        # 0x18009b138
   180023962:	48 89 01             	mov    %rax,(%rcx)
   180023965:	48 83 c1 08          	add    $0x8,%rcx
   180023969:	e8 e2 64 ff ff       	call   0x180019e50
   18002396e:	90                   	nop
   18002396f:	48 8b 47 08          	mov    0x8(%rdi),%rax
   180023973:	48 8d 15 62 70 07 00 	lea    0x77062(%rip),%rdx        # 0x18009a9dc
   18002397a:	48 8d 4f 08          	lea    0x8(%rdi),%rcx
   18002397e:	ff 50 08             	call   *0x8(%rax)
   180023981:	90                   	nop
   180023982:	48 8d 05 57 8a 07 00 	lea    0x78a57(%rip),%rax        # 0x18009c3e0
   180023989:	48 89 07             	mov    %rax,(%rdi)
   18002398c:	48 8d 4f 28          	lea    0x28(%rdi),%rcx
   180023990:	e8 bb 64 ff ff       	call   0x180019e50
   180023995:	90                   	nop
   180023996:	ff 15 6c 07 05 00    	call   *0x5076c(%rip)        # 0x180074108
   18002399c:	89 47 48             	mov    %eax,0x48(%rdi)
   18002399f:	44 8b c0             	mov    %eax,%r8d
   1800239a2:	33 d2                	xor    %edx,%edx
   1800239a4:	48 8b cf             	mov    %rdi,%rcx
```

### Line 98054 (Address `0x180074108`)
```assembly
   180056020:	48 8d 05 d9 9f fa ff 	lea    -0x56027(%rip),%rax        # 0x180000000
   180056027:	83 67 58 00          	andl   $0x0,0x58(%rdi)
   18005602b:	48 8d 4f 28          	lea    0x28(%rdi),%rcx
   18005602f:	83 67 5c 00          	andl   $0x0,0x5c(%rdi)
   180056033:	45 33 c0             	xor    %r8d,%r8d
   180056036:	48 89 47 10          	mov    %rax,0x10(%rdi)
   18005603a:	33 d2                	xor    %edx,%edx
   18005603c:	48 89 47 08          	mov    %rax,0x8(%rdi)
   180056040:	48 8d 05 59 c3 03 00 	lea    0x3c359(%rip),%rax        # 0x1800923a0
   180056047:	48 89 47 20          	mov    %rax,0x20(%rdi)
   18005604b:	c7 07 60 00 00 00    	movl   $0x60,(%rdi)
   180056051:	c7 47 18 00 0e 00 00 	movl   $0xe00,0x18(%rdi)
   180056058:	e8 63 4d fc ff       	call   0x18001adc0
   18005605d:	85 c0                	test   %eax,%eax
   18005605f:	75 36                	jne    0x180056097
   180056061:	ff 15 a1 e0 01 00    	call   *0x1e0a1(%rip)        # 0x180074108
   180056067:	0f b7 c8             	movzwl %ax,%ecx
   18005606a:	81 c9 00 00 07 80    	or     $0x80070000,%ecx
   180056070:	85 c0                	test   %eax,%eax
   180056072:	0f 4e c8             	cmovle %eax,%ecx
```

### Line 99730 (Address `0x180074108`)
```assembly
   18005757a:	48 83 c4 28          	add    $0x28,%rsp
   18005757e:	c3                   	ret
   18005757f:	e8 e4 ef 00 00       	call   0x180066568
   180057584:	cc                   	int3
   180057585:	cc                   	int3
   180057586:	cc                   	int3
   180057587:	cc                   	int3
   180057588:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18005758d:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
   180057592:	57                   	push   %rdi
   180057593:	48 83 ec 20          	sub    $0x20,%rsp
   180057597:	83 3d e2 ed 04 00 ff 	cmpl   $0xffffffff,0x4ede2(%rip)        # 0x1800a6380
   18005759e:	75 07                	jne    0x1800575a7
   1800575a0:	33 c0                	xor    %eax,%eax
   1800575a2:	e9 9c 00 00 00       	jmp    0x180057643
   1800575a7:	ff 15 5b cb 01 00    	call   *0x1cb5b(%rip)        # 0x180074108
   1800575ad:	8b 0d cd ed 04 00    	mov    0x4edcd(%rip),%ecx        # 0x1800a6380
   1800575b3:	8b f8                	mov    %eax,%edi
   1800575b5:	e8 12 1a 00 00       	call   0x180058fcc
   1800575ba:	48 83 ca ff          	or     $0xffffffffffffffff,%rdx
```

### Line 101548 (Address `0x180074108`)
```assembly
   180058de0:	00 
   180058de1:	48 85 db             	test   %rbx,%rbx
   180058de4:	74 0e                	je     0x180058df4
   180058de6:	48 3b df             	cmp    %rdi,%rbx
   180058de9:	0f 84 ac 00 00 00    	je     0x180058e9b
   180058def:	e9 a2 00 00 00       	jmp    0x180058e96
   180058df4:	4d 8b b4 f6 48 25 09 	mov    0x92548(%r14,%rsi,8),%r14
   180058dfb:	00 
   180058dfc:	33 d2                	xor    %edx,%edx
   180058dfe:	49 8b ce             	mov    %r14,%rcx
   180058e01:	41 b8 00 08 00 00    	mov    $0x800,%r8d
   180058e07:	ff 15 73 b4 01 00    	call   *0x1b473(%rip)        # 0x180074280
   180058e0d:	48 8b d8             	mov    %rax,%rbx
   180058e10:	48 85 c0             	test   %rax,%rax
   180058e13:	75 4f                	jne    0x180058e64
   180058e15:	ff 15 ed b2 01 00    	call   *0x1b2ed(%rip)        # 0x180074108
   180058e1b:	83 f8 57             	cmp    $0x57,%eax
   180058e1e:	75 42                	jne    0x180058e62
   180058e20:	8d 58 b0             	lea    -0x50(%rax),%ebx
   180058e23:	49 8b ce             	mov    %r14,%rcx
```

### Line 117944 (Address `0x180074108`)
```assembly
   1800668b9:	c3                   	ret
   1800668ba:	cc                   	int3
   1800668bb:	cc                   	int3
   1800668bc:	48 85 c9             	test   %rcx,%rcx
   1800668bf:	74 37                	je     0x1800668f8
   1800668c1:	53                   	push   %rbx
   1800668c2:	48 83 ec 20          	sub    $0x20,%rsp
   1800668c6:	4c 8b c1             	mov    %rcx,%r8
   1800668c9:	33 d2                	xor    %edx,%edx
   1800668cb:	48 8b 0d ce 1c 04 00 	mov    0x41cce(%rip),%rcx        # 0x1800a85a0
   1800668d2:	ff 15 40 d8 00 00    	call   *0xd840(%rip)        # 0x180074118
   1800668d8:	85 c0                	test   %eax,%eax
   1800668da:	75 17                	jne    0x1800668f3
   1800668dc:	e8 83 8c ff ff       	call   0x18005f564
   1800668e1:	48 8b d8             	mov    %rax,%rbx
   1800668e4:	ff 15 1e d8 00 00    	call   *0xd81e(%rip)        # 0x180074108
   1800668ea:	8b c8                	mov    %eax,%ecx
   1800668ec:	e8 bb 8b ff ff       	call   0x18005f4ac
   1800668f1:	89 03                	mov    %eax,(%rbx)
   1800668f3:	48 83 c4 20          	add    $0x20,%rsp
```

### Line 118241 (Address `0x180074108`)
```assembly
   180066c94:	48 83 64 24 30 00    	andq   $0x0,0x30(%rsp)
   180066c9a:	41 b9 01 00 00 00    	mov    $0x1,%r9d
   180066ca0:	89 74 24 28          	mov    %esi,0x28(%rsp)
   180066ca4:	33 d2                	xor    %edx,%edx
   180066ca6:	48 89 7c 24 20       	mov    %rdi,0x20(%rsp)
   180066cab:	e8 50 2a 00 00       	call   0x180069700
   180066cb0:	85 c0                	test   %eax,%eax
   180066cb2:	74 11                	je     0x180066cc5
   180066cb4:	83 7d 28 00          	cmpl   $0x0,0x28(%rbp)
   180066cb8:	75 81                	jne    0x180066c3b
   180066cba:	48 85 db             	test   %rbx,%rbx
   180066cbd:	74 02                	je     0x180066cc1
   180066cbf:	89 03                	mov    %eax,(%rbx)
   180066cc1:	33 db                	xor    %ebx,%ebx
   180066cc3:	eb 82                	jmp    0x180066c47
   180066cc5:	ff 15 3d d4 00 00    	call   *0xd43d(%rip)        # 0x180074108
   180066ccb:	83 f8 7a             	cmp    $0x7a,%eax
   180066cce:	0f 85 67 ff ff ff    	jne    0x180066c3b
   180066cd4:	48 85 ff             	test   %rdi,%rdi
   180066cd7:	74 12                	je     0x180066ceb
```

### Line 118796 (Address `0x180074108`)
```assembly
   1800673de:	e8 a1 31 00 00       	call   0x18006a584
   1800673e3:	48 8b cb             	mov    %rbx,%rcx
   1800673e6:	e8 6d fe ff ff       	call   0x180067258
   1800673eb:	48 8b cb             	mov    %rbx,%rcx
   1800673ee:	e8 c9 f4 ff ff       	call   0x1800668bc
   1800673f3:	48 83 c4 20          	add    $0x20,%rsp
   1800673f7:	5b                   	pop    %rbx
   1800673f8:	c3                   	ret
   1800673f9:	cc                   	int3
   1800673fa:	cc                   	int3
   1800673fb:	cc                   	int3
   1800673fc:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   180067401:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
   180067406:	57                   	push   %rdi
   180067407:	48 83 ec 20          	sub    $0x20,%rsp
   18006740b:	ff 15 f7 cc 00 00    	call   *0xccf7(%rip)        # 0x180074108
   180067411:	8b 0d 99 f0 03 00    	mov    0x3f099(%rip),%ecx        # 0x1800a64b0
   180067417:	8b d8                	mov    %eax,%ebx
   180067419:	83 f9 ff             	cmp    $0xffffffff,%ecx
   18006741c:	74 1f                	je     0x18006743d
```

### Line 118909 (Address `0x180074108`)
```assembly
   18006755c:	33 c9                	xor    %ecx,%ecx
   18006755e:	e8 59 f3 ff ff       	call   0x1800668bc
   180067563:	48 85 db             	test   %rbx,%rbx
   180067566:	74 09                	je     0x180067571
   180067568:	48 8b c3             	mov    %rbx,%rax
   18006756b:	48 83 c4 20          	add    $0x20,%rsp
   18006756f:	5b                   	pop    %rbx
   180067570:	c3                   	ret
   180067571:	e8 f2 ef ff ff       	call   0x180066568
   180067576:	cc                   	int3
   180067577:	cc                   	int3
   180067578:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18006757d:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
   180067582:	57                   	push   %rdi
   180067583:	48 83 ec 20          	sub    $0x20,%rsp
   180067587:	ff 15 7b cb 00 00    	call   *0xcb7b(%rip)        # 0x180074108
   18006758d:	8b 0d 1d ef 03 00    	mov    0x3ef1d(%rip),%ecx        # 0x1800a64b0
   180067593:	8b d8                	mov    %eax,%ebx
   180067595:	83 f9 ff             	cmp    $0xffffffff,%ecx
   180067598:	74 1f                	je     0x1800675b9
```

### Line 120819 (Address `0x180074108`)
```assembly
   180068efe:	48 8b 42 10          	mov    0x10(%rdx),%rax
   180068f02:	88 18                	mov    %bl,(%rax)
   180068f04:	eb c2                	jmp    0x180068ec8
   180068f06:	48 89 5c 24 38       	mov    %rbx,0x38(%rsp)
   180068f0b:	41 83 c9 ff          	or     $0xffffffff,%r9d
   180068f0f:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   180068f14:	4c 8b c6             	mov    %rsi,%r8
   180068f17:	89 5c 24 28          	mov    %ebx,0x28(%rsp)
   180068f1b:	33 d2                	xor    %edx,%edx
   180068f1d:	8b cd                	mov    %ebp,%ecx
   180068f1f:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180068f24:	e8 d7 07 00 00       	call   0x180069700
   180068f29:	48 63 d0             	movslq %eax,%rdx
   180068f2c:	85 c0                	test   %eax,%eax
   180068f2e:	75 16                	jne    0x180068f46
   180068f30:	ff 15 d2 b1 00 00    	call   *0xb1d2(%rip)        # 0x180074108
   180068f36:	8b c8                	mov    %eax,%ecx
   180068f38:	e8 b7 65 ff ff       	call   0x18005f4f4
   180068f3d:	e8 22 66 ff ff       	call   0x18005f564
   180068f42:	8b 18                	mov    (%rax),%ebx
```

### Line 120873 (Address `0x180074108`)
```assembly
   180068fad:	48 89 7c 24 18       	mov    %rdi,0x18(%rsp)
   180068fb2:	55                   	push   %rbp
   180068fb3:	48 8d ac 24 70 fe ff 	lea    -0x190(%rsp),%rbp
   180068fba:	ff 
   180068fbb:	48 81 ec 90 02 00 00 	sub    $0x290,%rsp
   180068fc2:	48 8b 05 97 d3 03 00 	mov    0x3d397(%rip),%rax        # 0x1800a6360
   180068fc9:	48 33 c4             	xor    %rsp,%rax
   180068fcc:	48 89 85 80 01 00 00 	mov    %rax,0x180(%rbp)
   180068fd3:	41 8b f8             	mov    %r8d,%edi
   180068fd6:	48 8b da             	mov    %rdx,%rbx
   180068fd9:	41 b8 05 01 00 00    	mov    $0x105,%r8d
   180068fdf:	48 8d 54 24 70       	lea    0x70(%rsp),%rdx
   180068fe4:	ff 15 66 b0 00 00    	call   *0xb066(%rip)        # 0x180074050
   180068fea:	85 c0                	test   %eax,%eax
   180068fec:	75 14                	jne    0x180069002
   180068fee:	ff 15 14 b1 00 00    	call   *0xb114(%rip)        # 0x180074108
   180068ff4:	8b c8                	mov    %eax,%ecx
   180068ff6:	e8 f9 64 ff ff       	call   0x18005f4f4
   180068ffb:	33 c0                	xor    %eax,%eax
   180068ffd:	e9 a0 00 00 00       	jmp    0x1800690a2
```

### Line 121907 (Address `0x180074108`)
```assembly
   180069dce:	75 20                	jne    0x180069df0
   180069dd0:	f6 80 80 00 00 00 01 	testb  $0x1,0x80(%rax)
   180069dd7:	74 17                	je     0x180069df0
   180069dd9:	e8 06 5c 00 00       	call   0x18006f9e4
   180069dde:	b9 01 00 00 00       	mov    $0x1,%ecx
   180069de3:	48 8b d8             	mov    %rax,%rbx
   180069de6:	e8 f9 5b 00 00       	call   0x18006f9e4
   180069deb:	48 3b c3             	cmp    %rbx,%rax
   180069dee:	74 be                	je     0x180069dae
   180069df0:	8b cf                	mov    %edi,%ecx
   180069df2:	e8 ed 5b 00 00       	call   0x18006f9e4
   180069df7:	48 8b c8             	mov    %rax,%rcx
   180069dfa:	ff 15 88 a2 00 00    	call   *0xa288(%rip)        # 0x180074088
   180069e00:	85 c0                	test   %eax,%eax
   180069e02:	75 aa                	jne    0x180069dae
   180069e04:	ff 15 fe a2 00 00    	call   *0xa2fe(%rip)        # 0x180074108
   180069e0a:	8b d8                	mov    %eax,%ebx
   180069e0c:	8b cf                	mov    %edi,%ecx
   180069e0e:	e8 15 5b 00 00       	call   0x18006f928
   180069e13:	48 8b d7             	mov    %rdi,%rdx
```

### Line 122182 (Address `0x180074108`)
```assembly
   18006a148:	00 
   18006a149:	48 85 db             	test   %rbx,%rbx
   18006a14c:	74 0e                	je     0x18006a15c
   18006a14e:	48 3b df             	cmp    %rdi,%rbx
   18006a151:	0f 84 ac 00 00 00    	je     0x18006a203
   18006a157:	e9 a2 00 00 00       	jmp    0x18006a1fe
   18006a15c:	4d 8b b4 f6 80 52 09 	mov    0x95280(%r14,%rsi,8),%r14
   18006a163:	00 
   18006a164:	33 d2                	xor    %edx,%edx
   18006a166:	49 8b ce             	mov    %r14,%rcx
   18006a169:	41 b8 00 08 00 00    	mov    $0x800,%r8d
   18006a16f:	ff 15 0b a1 00 00    	call   *0xa10b(%rip)        # 0x180074280
   18006a175:	48 8b d8             	mov    %rax,%rbx
   18006a178:	48 85 c0             	test   %rax,%rax
   18006a17b:	75 4f                	jne    0x18006a1cc
   18006a17d:	ff 15 85 9f 00 00    	call   *0x9f85(%rip)        # 0x180074108
   18006a183:	83 f8 57             	cmp    $0x57,%eax
   18006a186:	75 42                	jne    0x18006a1ca
   18006a188:	8d 58 b0             	lea    -0x50(%rax),%ebx
   18006a18b:	49 8b ce             	mov    %r14,%rcx
```

### Line 122844 (Address `0x180074108`)
```assembly
   18006aae1:	48 c1 f8 06          	sar    $0x6,%rax
   18006aae5:	4c 8d 05 44 d2 03 00 	lea    0x3d244(%rip),%r8        # 0x1800a7d30
   18006aaec:	83 e2 3f             	and    $0x3f,%edx
   18006aaef:	48 8d 14 d2          	lea    (%rdx,%rdx,8),%rdx
   18006aaf3:	49 8b 04 c0          	mov    (%r8,%rax,8),%rax
   18006aaf7:	f6 44 d0 38 01       	testb  $0x1,0x38(%rax,%rdx,8)
   18006aafc:	74 24                	je     0x18006ab22
   18006aafe:	e8 e1 4e 00 00       	call   0x18006f9e4
   18006ab03:	48 8b c8             	mov    %rax,%rcx
   18006ab06:	ff 15 04 96 00 00    	call   *0x9604(%rip)        # 0x180074110
   18006ab0c:	33 db                	xor    %ebx,%ebx
   18006ab0e:	85 c0                	test   %eax,%eax
   18006ab10:	75 1e                	jne    0x18006ab30
   18006ab12:	e8 2d 4a ff ff       	call   0x18005f544
   18006ab17:	48 8b d8             	mov    %rax,%rbx
   18006ab1a:	ff 15 e8 95 00 00    	call   *0x95e8(%rip)        # 0x180074108
   18006ab20:	89 03                	mov    %eax,(%rbx)
   18006ab22:	e8 3d 4a ff ff       	call   0x18005f564
   18006ab27:	c7 00 09 00 00 00    	movl   $0x9,(%rax)
   18006ab2d:	83 cb ff             	or     $0xffffffff,%ebx
```

### Line 123227 (Address `0x180074108`)
```assembly
   18006b052:	44 38 75 8f          	cmp    %r14b,-0x71(%rbp)
   18006b056:	89 5d 9b             	mov    %ebx,-0x65(%rbp)
   18006b059:	e9 61 ff ff ff       	jmp    0x18006afbf
   18006b05e:	8a 06                	mov    (%rsi),%al
   18006b060:	4c 8d 05 99 4f f9 ff 	lea    -0x6b067(%rip),%r8        # 0x180000000
   18006b067:	4b 8b 8c e0 30 7d 0a 	mov    0xa7d30(%r8,%r12,8),%rcx
   18006b06e:	00 
   18006b06f:	ff c3                	inc    %ebx
   18006b071:	89 5d 9b             	mov    %ebx,-0x65(%rbp)
   18006b074:	42 88 44 f1 3e       	mov    %al,0x3e(%rcx,%r14,8)
   18006b079:	4b 8b 84 e0 30 7d 0a 	mov    0xa7d30(%r8,%r12,8),%rax
   18006b080:	00 
   18006b081:	42 80 4c f0 3d 04    	orb    $0x4,0x3d(%rax,%r14,8)
   18006b087:	38 55 8f             	cmp    %dl,-0x71(%rbp)
   18006b08a:	e9 30 ff ff ff       	jmp    0x18006afbf
   18006b08f:	ff 15 73 90 00 00    	call   *0x9073(%rip)        # 0x180074108
   18006b095:	89 45 97             	mov    %eax,-0x69(%rbp)
   18006b098:	80 7d 8f 00          	cmpb   $0x0,-0x71(%rbp)
   18006b09c:	e9 1e ff ff ff       	jmp    0x18006afbf
   18006b0a1:	ff 15 61 90 00 00    	call   *0x9061(%rip)        # 0x180074108
```

### Line 123231 (Address `0x180074108`)
```assembly
   18006b060:	4c 8d 05 99 4f f9 ff 	lea    -0x6b067(%rip),%r8        # 0x180000000
   18006b067:	4b 8b 8c e0 30 7d 0a 	mov    0xa7d30(%r8,%r12,8),%rcx
   18006b06e:	00 
   18006b06f:	ff c3                	inc    %ebx
   18006b071:	89 5d 9b             	mov    %ebx,-0x65(%rbp)
   18006b074:	42 88 44 f1 3e       	mov    %al,0x3e(%rcx,%r14,8)
   18006b079:	4b 8b 84 e0 30 7d 0a 	mov    0xa7d30(%r8,%r12,8),%rax
   18006b080:	00 
   18006b081:	42 80 4c f0 3d 04    	orb    $0x4,0x3d(%rax,%r14,8)
   18006b087:	38 55 8f             	cmp    %dl,-0x71(%rbp)
   18006b08a:	e9 30 ff ff ff       	jmp    0x18006afbf
   18006b08f:	ff 15 73 90 00 00    	call   *0x9073(%rip)        # 0x180074108
   18006b095:	89 45 97             	mov    %eax,-0x69(%rbp)
   18006b098:	80 7d 8f 00          	cmpb   $0x0,-0x71(%rbp)
   18006b09c:	e9 1e ff ff ff       	jmp    0x18006afbf
   18006b0a1:	ff 15 61 90 00 00    	call   *0x9061(%rip)        # 0x180074108
   18006b0a7:	89 45 97             	mov    %eax,-0x69(%rbp)
   18006b0aa:	38 5d 8f             	cmp    %bl,-0x71(%rbp)
   18006b0ad:	e9 0d ff ff ff       	jmp    0x18006afbf
   18006b0b2:	cc                   	int3
```

### Line 123299 (Address `0x180074108`)
```assembly
   18006b155:	2b d8                	sub    %eax,%ebx
   18006b157:	4c 8d 4c 24 30       	lea    0x30(%rsp),%r9
   18006b15c:	44 8b c3             	mov    %ebx,%r8d
   18006b15f:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18006b164:	49 8b ce             	mov    %r14,%rcx
   18006b167:	ff 15 83 8f 00 00    	call   *0x8f83(%rip)        # 0x1800740f0
   18006b16d:	85 c0                	test   %eax,%eax
   18006b16f:	74 12                	je     0x18006b183
   18006b171:	8b 44 24 30          	mov    0x30(%rsp),%eax
   18006b175:	01 47 04             	add    %eax,0x4(%rdi)
   18006b178:	3b c3                	cmp    %ebx,%eax
   18006b17a:	72 0f                	jb     0x18006b18b
   18006b17c:	48 3b f5             	cmp    %rbp,%rsi
   18006b17f:	72 9b                	jb     0x18006b11c
   18006b181:	eb 08                	jmp    0x18006b18b
   18006b183:	ff 15 7f 8f 00 00    	call   *0x8f7f(%rip)        # 0x180074108
   18006b189:	89 07                	mov    %eax,(%rdi)
   18006b18b:	48 8b c7             	mov    %rdi,%rax
   18006b18e:	48 8b 8c 24 40 14 00 	mov    0x1440(%rsp),%rcx
   18006b195:	00 
```

### Line 123382 (Address `0x180074108`)
```assembly
   18006b272:	48 d1 fb             	sar    $1,%rbx
   18006b275:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18006b27a:	03 db                	add    %ebx,%ebx
   18006b27c:	49 8b ce             	mov    %r14,%rcx
   18006b27f:	44 8b c3             	mov    %ebx,%r8d
   18006b282:	ff 15 68 8e 00 00    	call   *0x8e68(%rip)        # 0x1800740f0
   18006b288:	85 c0                	test   %eax,%eax
   18006b28a:	74 12                	je     0x18006b29e
   18006b28c:	8b 44 24 30          	mov    0x30(%rsp),%eax
   18006b290:	01 47 04             	add    %eax,0x4(%rdi)
   18006b293:	3b c3                	cmp    %ebx,%eax
   18006b295:	72 0f                	jb     0x18006b2a6
   18006b297:	48 3b f5             	cmp    %rbp,%rsi
   18006b29a:	72 88                	jb     0x18006b224
   18006b29c:	eb 08                	jmp    0x18006b2a6
   18006b29e:	ff 15 64 8e 00 00    	call   *0x8e64(%rip)        # 0x180074108
   18006b2a4:	89 07                	mov    %eax,(%rdi)
   18006b2a6:	48 8b c7             	mov    %rdi,%rax
   18006b2a9:	48 8b 8c 24 40 14 00 	mov    0x1440(%rsp),%rcx
   18006b2b0:	00 
```

### Line 123490 (Address `0x180074108`)
```assembly
   18006b3df:	44 8b c5             	mov    %ebp,%r8d
   18006b3e2:	48 03 d1             	add    %rcx,%rdx
   18006b3e5:	49 8b cc             	mov    %r12,%rcx
   18006b3e8:	44 2b c6             	sub    %esi,%r8d
   18006b3eb:	ff 15 ff 8c 00 00    	call   *0x8cff(%rip)        # 0x1800740f0
   18006b3f1:	85 c0                	test   %eax,%eax
   18006b3f3:	74 18                	je     0x18006b40d
   18006b3f5:	03 74 24 40          	add    0x40(%rsp),%esi
   18006b3f9:	3b f5                	cmp    %ebp,%esi
   18006b3fb:	72 cd                	jb     0x18006b3ca
   18006b3fd:	8b c7                	mov    %edi,%eax
   18006b3ff:	41 2b c7             	sub    %r15d,%eax
   18006b402:	89 43 04             	mov    %eax,0x4(%rbx)
   18006b405:	49 3b fe             	cmp    %r14,%rdi
   18006b408:	e9 34 ff ff ff       	jmp    0x18006b341
   18006b40d:	ff 15 f5 8c 00 00    	call   *0x8cf5(%rip)        # 0x180074108
   18006b413:	89 03                	mov    %eax,(%rbx)
   18006b415:	48 8b c3             	mov    %rbx,%rax
   18006b418:	48 8b 8c 24 60 14 00 	mov    0x1460(%rsp),%rcx
   18006b41f:	00 
```

### Line 123681 (Address `0x180074108`)
```assembly
   18006b681:	89 5d d4             	mov    %ebx,-0x2c(%rbp)
   18006b684:	66 83 f9 0a          	cmp    $0xa,%cx
   18006b688:	75 1b                	jne    0x18006b6a5
   18006b68a:	b9 0d 00 00 00       	mov    $0xd,%ecx
   18006b68f:	e8 a8 49 00 00       	call   0x18007003c
   18006b694:	b9 0d 00 00 00       	mov    $0xd,%ecx
   18006b699:	66 3b c1             	cmp    %cx,%ax
   18006b69c:	75 12                	jne    0x18006b6b0
   18006b69e:	ff c3                	inc    %ebx
   18006b6a0:	89 5d d4             	mov    %ebx,-0x2c(%rbp)
   18006b6a3:	ff c6                	inc    %esi
   18006b6a5:	49 83 c6 02          	add    $0x2,%r14
   18006b6a9:	4d 3b f4             	cmp    %r12,%r14
   18006b6ac:	73 0b                	jae    0x18006b6b9
   18006b6ae:	eb b5                	jmp    0x18006b665
   18006b6b0:	ff 15 52 8a 00 00    	call   *0x8a52(%rip)        # 0x180074108
   18006b6b6:	89 45 d0             	mov    %eax,-0x30(%rbp)
   18006b6b9:	8b de                	mov    %esi,%ebx
   18006b6bb:	e9 b2 00 00 00       	jmp    0x18006b772
   18006b6c0:	45 8b ce             	mov    %r14d,%r9d
```

### Line 123733 (Address `0x180074108`)
```assembly
   18006b732:	4c 8b c7             	mov    %rdi,%r8
   18006b735:	41 8b d4             	mov    %r12d,%edx
   18006b738:	e8 77 f9 ff ff       	call   0x18006b0b4
   18006b73d:	eb 93                	jmp    0x18006b6d2
   18006b73f:	4a 8b 4c f9 28       	mov    0x28(%rcx,%r15,8),%rcx
   18006b744:	4c 8d 4d d4          	lea    -0x2c(%rbp),%r9
   18006b748:	33 c0                	xor    %eax,%eax
   18006b74a:	45 8b c6             	mov    %r14d,%r8d
   18006b74d:	48 21 44 24 20       	and    %rax,0x20(%rsp)
   18006b752:	48 8b d7             	mov    %rdi,%rdx
   18006b755:	48 89 45 d0          	mov    %rax,-0x30(%rbp)
   18006b759:	89 45 d8             	mov    %eax,-0x28(%rbp)
   18006b75c:	ff 15 8e 89 00 00    	call   *0x898e(%rip)        # 0x1800740f0
   18006b762:	85 c0                	test   %eax,%eax
   18006b764:	75 09                	jne    0x18006b76f
   18006b766:	ff 15 9c 89 00 00    	call   *0x899c(%rip)        # 0x180074108
   18006b76c:	89 45 d0             	mov    %eax,-0x30(%rbp)
   18006b76f:	8b 5d d8             	mov    -0x28(%rbp),%ebx
   18006b772:	f2 0f 10 45 d0       	movsd  -0x30(%rbp),%xmm0
   18006b777:	f2 0f 11 45 e0       	movsd  %xmm0,-0x20(%rbp)
```

### Line 124244 (Address `0x180074108`)
```assembly
   18006bdfc:	8b da                	mov    %edx,%ebx
   18006bdfe:	e9 be 00 00 00       	jmp    0x18006bec1
   18006be03:	48 8b 47 10          	mov    0x10(%rdi),%rax
   18006be07:	66 89 18             	mov    %bx,(%rax)
   18006be0a:	eb 9e                	jmp    0x18006bdaa
   18006be0c:	41 83 c9 ff          	or     $0xffffffff,%r9d
   18006be10:	89 5c 24 28          	mov    %ebx,0x28(%rsp)
   18006be14:	4c 8b c6             	mov    %rsi,%r8
   18006be17:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   18006be1c:	8b cd                	mov    %ebp,%ecx
   18006be1e:	41 8d 51 0a          	lea    0xa(%r9),%edx
   18006be22:	e8 7d d8 ff ff       	call   0x1800696a4
   18006be27:	4c 63 f0             	movslq %eax,%r14
   18006be2a:	85 c0                	test   %eax,%eax
   18006be2c:	75 16                	jne    0x18006be44
   18006be2e:	ff 15 d4 82 00 00    	call   *0x82d4(%rip)        # 0x180074108
   18006be34:	8b c8                	mov    %eax,%ecx
   18006be36:	e8 b9 36 ff ff       	call   0x18005f4f4
   18006be3b:	e8 24 37 ff ff       	call   0x18005f564
   18006be40:	8b 18                	mov    (%rax),%ebx
```

### Line 124359 (Address `0x180074108`)
```assembly
   18006bf7c:	48 8b 47 10          	mov    0x10(%rdi),%rax
   18006bf80:	88 18                	mov    %bl,(%rax)
   18006bf82:	eb 9e                	jmp    0x18006bf22
   18006bf84:	48 89 5c 24 38       	mov    %rbx,0x38(%rsp)
   18006bf89:	41 83 c9 ff          	or     $0xffffffff,%r9d
   18006bf8d:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   18006bf92:	4c 8b c6             	mov    %rsi,%r8
   18006bf95:	89 5c 24 28          	mov    %ebx,0x28(%rsp)
   18006bf99:	33 d2                	xor    %edx,%edx
   18006bf9b:	41 8b ce             	mov    %r14d,%ecx
   18006bf9e:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   18006bfa3:	e8 58 d7 ff ff       	call   0x180069700
   18006bfa8:	48 63 e8             	movslq %eax,%rbp
   18006bfab:	85 c0                	test   %eax,%eax
   18006bfad:	75 19                	jne    0x18006bfc8
   18006bfaf:	ff 15 53 81 00 00    	call   *0x8153(%rip)        # 0x180074108
   18006bfb5:	8b c8                	mov    %eax,%ecx
   18006bfb7:	e8 38 35 ff ff       	call   0x18005f4f4
   18006bfbc:	e8 a3 35 ff ff       	call   0x18005f564
   18006bfc1:	8b 18                	mov    (%rax),%ebx
```

### Line 128942 (Address `0x180074108`)
```assembly
   18006ffa7:	48 8b f2             	mov    %rdx,%rsi
   18006ffaa:	e8 35 fa ff ff       	call   0x18006f9e4
   18006ffaf:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18006ffb3:	75 11                	jne    0x18006ffc6
   18006ffb5:	e8 aa f5 fe ff       	call   0x18005f564
   18006ffba:	c7 00 09 00 00 00    	movl   $0x9,(%rax)
   18006ffc0:	48 83 c8 ff          	or     $0xffffffffffffffff,%rax
   18006ffc4:	eb 53                	jmp    0x180070019
   18006ffc6:	44 8b cf             	mov    %edi,%r9d
   18006ffc9:	4c 8d 44 24 48       	lea    0x48(%rsp),%r8
   18006ffce:	48 8b d6             	mov    %rsi,%rdx
   18006ffd1:	48 8b c8             	mov    %rax,%rcx
   18006ffd4:	ff 15 b6 41 00 00    	call   *0x41b6(%rip)        # 0x180074190
   18006ffda:	85 c0                	test   %eax,%eax
   18006ffdc:	75 0f                	jne    0x18006ffed
   18006ffde:	ff 15 24 41 00 00    	call   *0x4124(%rip)        # 0x180074108
   18006ffe4:	8b c8                	mov    %eax,%ecx
   18006ffe6:	e8 09 f5 fe ff       	call   0x18005f4f4
   18006ffeb:	eb d3                	jmp    0x18006ffc0
   18006ffed:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
```

### Line 130910 (Address `0x180074108`)
```assembly
   180071a27:	48 89 70 18          	mov    %rsi,0x18(%rax)
   180071a2b:	57                   	push   %rdi
   180071a2c:	48 83 ec 40          	sub    $0x40,%rsp
   180071a30:	48 83 60 d8 00       	andq   $0x0,-0x28(%rax)
   180071a35:	49 8b f8             	mov    %r8,%rdi
   180071a38:	4d 8b c8             	mov    %r8,%r9
   180071a3b:	8b f2                	mov    %edx,%esi
   180071a3d:	44 8b c2             	mov    %edx,%r8d
   180071a40:	48 8b e9             	mov    %rcx,%rbp
   180071a43:	48 8b d1             	mov    %rcx,%rdx
   180071a46:	48 8b 0d 13 53 03 00 	mov    0x35313(%rip),%rcx        # 0x1800a6d60
   180071a4d:	ff 15 4d 28 00 00    	call   *0x284d(%rip)        # 0x1800742a0
   180071a53:	8b d8                	mov    %eax,%ebx
   180071a55:	85 c0                	test   %eax,%eax
   180071a57:	75 6a                	jne    0x180071ac3
   180071a59:	ff 15 a9 26 00 00    	call   *0x26a9(%rip)        # 0x180074108
   180071a5f:	83 f8 06             	cmp    $0x6,%eax
   180071a62:	75 5f                	jne    0x180071ac3
   180071a64:	48 8b 0d f5 52 03 00 	mov    0x352f5(%rip),%rcx        # 0x1800a6d60
   180071a6b:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
```

## `KERNEL32.dll!GetLocalTime` (4 Call Sites)

### Line 23272 (Address `0x1800740a8`)
```assembly
   180015617:	4c 89 3b             	mov    %r15,(%rbx)
   18001561a:	ff 15 a8 ea 05 00    	call   *0x5eaa8(%rip)        # 0x1800740c8
   180015620:	4c 89 73 30          	mov    %r14,0x30(%rbx)
   180015624:	4c 89 73 38          	mov    %r14,0x38(%rbx)
   180015628:	e8 83 16 00 00       	call   0x180016cb0
   18001562d:	48 89 43 30          	mov    %rax,0x30(%rbx)
   180015631:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   180015636:	4c 89 73 58          	mov    %r14,0x58(%rbx)
   18001563a:	48 b8 00 00 00 00 00 	movabs $0x4014000000000000,%rax
   180015641:	00 14 40 
   180015644:	48 89 43 60          	mov    %rax,0x60(%rbx)
   180015648:	33 c0                	xor    %eax,%eax
   18001564a:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001564f:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180015654:	4c 89 73 68          	mov    %r14,0x68(%rbx)
   180015658:	ff 15 4a ea 05 00    	call   *0x5ea4a(%rip)        # 0x1800740a8
   18001565e:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   180015663:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   180015668:	ff 15 42 ea 05 00    	call   *0x5ea42(%rip)        # 0x1800740b0
   18001566e:	48 8b 44 24 40       	mov    0x40(%rsp),%rax
```

### Line 23903 (Address `0x1800740a8`)
```assembly
   180016003:	8d 50 01             	lea    0x1(%rax),%edx
   180016006:	48 8d 4d ff          	lea    -0x1(%rbp),%rcx
   18001600a:	e8 f1 42 00 00       	call   0x18001a300
   18001600f:	4c 8b 45 07          	mov    0x7(%rbp),%r8
   180016013:	48 8b 4d ff          	mov    -0x1(%rbp),%rcx
   180016017:	4c 2b c1             	sub    %rcx,%r8
   18001601a:	49 d1 f8             	sar    $1,%r8
   18001601d:	4d 03 c0             	add    %r8,%r8
   180016020:	48 8d 15 b5 49 08 00 	lea    0x849b5(%rip),%rdx        # 0x18009a9dc
   180016027:	e8 a4 09 04 00       	call   0x1800569d0
   18001602c:	90                   	nop
   18001602d:	33 c0                	xor    %eax,%eax
   18001602f:	48 89 45 e7          	mov    %rax,-0x19(%rbp)
   180016033:	48 89 45 ef          	mov    %rax,-0x11(%rbp)
   180016037:	48 8d 4d e7          	lea    -0x19(%rbp),%rcx
   18001603b:	ff 15 67 e0 05 00    	call   *0x5e067(%rip)        # 0x1800740a8
   180016041:	48 8d 55 d7          	lea    -0x29(%rbp),%rdx
   180016045:	48 8d 4d e7          	lea    -0x19(%rbp),%rcx
   180016049:	ff 15 61 e0 05 00    	call   *0x5e061(%rip)        # 0x1800740b0
   18001604f:	48 8b 45 d7          	mov    -0x29(%rbp),%rax
```

### Line 29012 (Address `0x1800740a8`)
```assembly
   18001a623:	ff ff 
   18001a625:	48 8b 05 34 bd 08 00 	mov    0x8bd34(%rip),%rax        # 0x1800a6360
   18001a62c:	48 33 c4             	xor    %rsp,%rax
   18001a62f:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
   18001a634:	4d 8b f8             	mov    %r8,%r15
   18001a637:	44 8b f2             	mov    %edx,%r14d
   18001a63a:	48 8b f1             	mov    %rcx,%rsi
   18001a63d:	ff 15 9d 9a 05 00    	call   *0x59a9d(%rip)        # 0x1800740e0
   18001a643:	8b f8                	mov    %eax,%edi
   18001a645:	ff 15 8d 9a 05 00    	call   *0x59a8d(%rip)        # 0x1800740d8
   18001a64b:	8b d8                	mov    %eax,%ebx
   18001a64d:	33 c0                	xor    %eax,%eax
   18001a64f:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001a654:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   18001a659:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18001a65e:	ff 15 44 9a 05 00    	call   *0x59a44(%rip)        # 0x1800740a8
   18001a664:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   18001a669:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18001a66e:	ff 15 3c 9a 05 00    	call   *0x59a3c(%rip)        # 0x1800740b0
   18001a674:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
```

### Line 37211 (Address `0x1800740a8`)
```assembly
   180021e47:	41 56                	push   %r14
   180021e49:	48 83 ec 60          	sub    $0x60,%rsp
   180021e4d:	48 8b 05 0c 45 08 00 	mov    0x8450c(%rip),%rax        # 0x1800a6360
   180021e54:	48 33 c4             	xor    %rsp,%rax
   180021e57:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180021e5c:	49 8b f0             	mov    %r8,%rsi
   180021e5f:	4c 8b f1             	mov    %rcx,%r14
   180021e62:	ff 15 78 22 05 00    	call   *0x52278(%rip)        # 0x1800740e0
   180021e68:	8b f8                	mov    %eax,%edi
   180021e6a:	ff 15 68 22 05 00    	call   *0x52268(%rip)        # 0x1800740d8
   180021e70:	8b d8                	mov    %eax,%ebx
   180021e72:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180021e77:	33 c0                	xor    %eax,%eax
   180021e79:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   180021e7e:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   180021e83:	ff 15 1f 22 05 00    	call   *0x5221f(%rip)        # 0x1800740a8
   180021e89:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   180021e8e:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180021e93:	ff 15 17 22 05 00    	call   *0x52217(%rip)        # 0x1800740b0
   180021e99:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
```

## `KERNEL32.dll!GetModuleFileNameW` (3 Call Sites)

### Line 25035 (Address `0x180074050`)
```assembly
   180016ebd:	48 89 70 10          	mov    %rsi,0x10(%rax)
   180016ec1:	48 89 78 18          	mov    %rdi,0x18(%rax)
   180016ec5:	4c 89 60 20          	mov    %r12,0x20(%rax)
   180016ec9:	48 8b 05 90 f4 08 00 	mov    0x8f490(%rip),%rax        # 0x1800a6360
   180016ed0:	48 33 c4             	xor    %rsp,%rax
   180016ed3:	48 89 84 24 30 04 00 	mov    %rax,0x430(%rsp)
   180016eda:	00 
   180016edb:	4c 8b 25 fe 16 09 00 	mov    0x916fe(%rip),%r12        # 0x1800a85e0
   180016ee2:	4c 89 64 24 58       	mov    %r12,0x58(%rsp)
   180016ee7:	33 c9                	xor    %ecx,%ecx
   180016ee9:	ff 15 69 d1 05 00    	call   *0x5d169(%rip)        # 0x180074058
   180016eef:	41 b8 04 01 00 00    	mov    $0x104,%r8d
   180016ef5:	48 8d 94 24 20 02 00 	lea    0x220(%rsp),%rdx
   180016efc:	00 
   180016efd:	48 8b c8             	mov    %rax,%rcx
   180016f00:	ff 15 4a d1 05 00    	call   *0x5d14a(%rip)        # 0x180074050
   180016f06:	33 ff                	xor    %edi,%edi
   180016f08:	48 89 bc 24 c8 00 00 	mov    %rdi,0xc8(%rsp)
   180016f0f:	00 
   180016f10:	48 c7 84 24 d0 00 00 	movq   $0x7,0xd0(%rsp)
```

### Line 108716 (Address `0x180074050`)
```assembly
   18005edb3:	44 8b c6             	mov    %esi,%r8d
   18005edb6:	33 d2                	xor    %edx,%edx
   18005edb8:	e8 73 80 ff ff       	call   0x180056e30
   18005edbd:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
   18005edc2:	4c 89 74 24 30       	mov    %r14,0x30(%rsp)
   18005edc7:	48 8b d5             	mov    %rbp,%rdx
   18005edca:	41 8d 4e 06          	lea    0x6(%r14),%ecx
   18005edce:	ff 15 c4 54 01 00    	call   *0x154c4(%rip)        # 0x180074298
   18005edd4:	bd 05 01 00 00       	mov    $0x105,%ebp
   18005edd9:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18005edde:	f7 d8                	neg    %eax
   18005ede0:	44 8b c5             	mov    %ebp,%r8d
   18005ede3:	48 1b c9             	sbb    %rcx,%rcx
   18005ede6:	48 23 4c 24 30       	and    0x30(%rsp),%rcx
   18005edeb:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   18005edf0:	ff 15 5a 52 01 00    	call   *0x1525a(%rip)        # 0x180074050
   18005edf6:	85 c0                	test   %eax,%eax
   18005edf8:	75 1b                	jne    0x18005ee15
   18005edfa:	4c 8d 05 f7 45 03 00 	lea    0x345f7(%rip),%r8        # 0x1800933f8
   18005ee01:	8b d5                	mov    %ebp,%edx
```

### Line 120870 (Address `0x180074050`)
```assembly
   180068fa6:	cc                   	int3
   180068fa7:	cc                   	int3
   180068fa8:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
   180068fad:	48 89 7c 24 18       	mov    %rdi,0x18(%rsp)
   180068fb2:	55                   	push   %rbp
   180068fb3:	48 8d ac 24 70 fe ff 	lea    -0x190(%rsp),%rbp
   180068fba:	ff 
   180068fbb:	48 81 ec 90 02 00 00 	sub    $0x290,%rsp
   180068fc2:	48 8b 05 97 d3 03 00 	mov    0x3d397(%rip),%rax        # 0x1800a6360
   180068fc9:	48 33 c4             	xor    %rsp,%rax
   180068fcc:	48 89 85 80 01 00 00 	mov    %rax,0x180(%rbp)
   180068fd3:	41 8b f8             	mov    %r8d,%edi
   180068fd6:	48 8b da             	mov    %rdx,%rbx
   180068fd9:	41 b8 05 01 00 00    	mov    $0x105,%r8d
   180068fdf:	48 8d 54 24 70       	lea    0x70(%rsp),%rdx
   180068fe4:	ff 15 66 b0 00 00    	call   *0xb066(%rip)        # 0x180074050
   180068fea:	85 c0                	test   %eax,%eax
   180068fec:	75 14                	jne    0x180069002
   180068fee:	ff 15 14 b1 00 00    	call   *0xb114(%rip)        # 0x180074108
   180068ff4:	8b c8                	mov    %eax,%ecx
```

## `KERNEL32.dll!GetModuleHandleExW` (2 Call Sites)

### Line 108708 (Address `0x180074298`)
```assembly
   18005ed8f:	4c 8d 05 92 44 03 00 	lea    0x34492(%rip),%r8        # 0x180093228
   18005ed96:	48 8b d7             	mov    %rdi,%rdx
   18005ed99:	48 8b cb             	mov    %rbx,%rcx
   18005ed9c:	e8 73 9f 00 00       	call   0x180068d14
   18005eda1:	85 c0                	test   %eax,%eax
   18005eda3:	0f 85 3b 04 00 00    	jne    0x18005f1e4
   18005eda9:	be 0a 02 00 00       	mov    $0x20a,%esi
   18005edae:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   18005edb3:	44 8b c6             	mov    %esi,%r8d
   18005edb6:	33 d2                	xor    %edx,%edx
   18005edb8:	e8 73 80 ff ff       	call   0x180056e30
   18005edbd:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
   18005edc2:	4c 89 74 24 30       	mov    %r14,0x30(%rsp)
   18005edc7:	48 8b d5             	mov    %rbp,%rdx
   18005edca:	41 8d 4e 06          	lea    0x6(%r14),%ecx
   18005edce:	ff 15 c4 54 01 00    	call   *0x154c4(%rip)        # 0x180074298
   18005edd4:	bd 05 01 00 00       	mov    $0x105,%ebp
   18005edd9:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18005edde:	f7 d8                	neg    %eax
   18005ede0:	44 8b c5             	mov    %ebp,%r8d
```

### Line 109529 (Address `0x180074298`)
```assembly
   18005f8e0:	ff 15 12 49 01 00    	call   *0x14912(%rip)        # 0x1800741f8
   18005f8e6:	8b cb                	mov    %ebx,%ecx
   18005f8e8:	e8 0b 00 00 00       	call   0x18005f8f8
   18005f8ed:	8b cb                	mov    %ebx,%ecx
   18005f8ef:	ff 15 b3 49 01 00    	call   *0x149b3(%rip)        # 0x1800742a8
   18005f8f5:	cc                   	int3
   18005f8f6:	cc                   	int3
   18005f8f7:	cc                   	int3
   18005f8f8:	40 53                	rex push %rbx
   18005f8fa:	48 83 ec 20          	sub    $0x20,%rsp
   18005f8fe:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   18005f904:	4c 8d 44 24 38       	lea    0x38(%rsp),%r8
   18005f909:	8b d9                	mov    %ecx,%ebx
   18005f90b:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x180093598
   18005f912:	33 c9                	xor    %ecx,%ecx
   18005f914:	ff 15 7e 49 01 00    	call   *0x1497e(%rip)        # 0x180074298
   18005f91a:	85 c0                	test   %eax,%eax
   18005f91c:	74 1f                	je     0x18005f93d
   18005f91e:	48 8b 4c 24 38       	mov    0x38(%rsp),%rcx
   18005f923:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x1800935b0
```

## `KERNEL32.dll!GetModuleHandleW` (4 Call Sites)

### Line 25030 (Address `0x180074058`)
```assembly
   180016ea7:	41 57                	push   %r15
   180016ea9:	48 81 ec 40 04 00 00 	sub    $0x440,%rsp
   180016eb0:	48 c7 44 24 60 fe ff 	movq   $0xfffffffffffffffe,0x60(%rsp)
   180016eb7:	ff ff 
   180016eb9:	48 89 58 08          	mov    %rbx,0x8(%rax)
   180016ebd:	48 89 70 10          	mov    %rsi,0x10(%rax)
   180016ec1:	48 89 78 18          	mov    %rdi,0x18(%rax)
   180016ec5:	4c 89 60 20          	mov    %r12,0x20(%rax)
   180016ec9:	48 8b 05 90 f4 08 00 	mov    0x8f490(%rip),%rax        # 0x1800a6360
   180016ed0:	48 33 c4             	xor    %rsp,%rax
   180016ed3:	48 89 84 24 30 04 00 	mov    %rax,0x430(%rsp)
   180016eda:	00 
   180016edb:	4c 8b 25 fe 16 09 00 	mov    0x916fe(%rip),%r12        # 0x1800a85e0
   180016ee2:	4c 89 64 24 58       	mov    %r12,0x58(%rsp)
   180016ee7:	33 c9                	xor    %ecx,%ecx
   180016ee9:	ff 15 69 d1 05 00    	call   *0x5d169(%rip)        # 0x180074058
   180016eef:	41 b8 04 01 00 00    	mov    $0x104,%r8d
   180016ef5:	48 8d 94 24 20 02 00 	lea    0x220(%rsp),%rdx
   180016efc:	00 
   180016efd:	48 8b c8             	mov    %rax,%rcx
```

### Line 96902 (Address `0x180074058`)
```assembly
   180055024:	e9 1b 9c 00 00       	jmp    0x18005ec44
   180055029:	cc                   	int3
   18005502a:	cc                   	int3
   18005502b:	cc                   	int3
   18005502c:	40 57                	rex push %rdi
   18005502e:	48 83 ec 30          	sub    $0x30,%rsp
   180055032:	48 c7 44 24 20 fe ff 	movq   $0xfffffffffffffffe,0x20(%rsp)
   180055039:	ff ff 
   18005503b:	48 89 5c 24 40       	mov    %rbx,0x40(%rsp)
   180055040:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180055045:	ba a0 0f 00 00       	mov    $0xfa0,%edx
   18005504a:	48 8d 0d 07 23 05 00 	lea    0x52307(%rip),%rcx        # 0x1800a7358
   180055051:	ff 15 61 f1 01 00    	call   *0x1f161(%rip)        # 0x1800741b8
   180055057:	90                   	nop
   180055058:	48 8d 0d b1 d1 03 00 	lea    0x3d1b1(%rip),%rcx        # 0x180092210
   18005505f:	ff 15 f3 ef 01 00    	call   *0x1eff3(%rip)        # 0x180074058
   180055065:	90                   	nop
   180055066:	48 8b d8             	mov    %rax,%rbx
   180055069:	48 85 c0             	test   %rax,%rax
   18005506c:	75 1a                	jne    0x180055088
```

### Line 96908 (Address `0x180074058`)
```assembly
   180055032:	48 c7 44 24 20 fe ff 	movq   $0xfffffffffffffffe,0x20(%rsp)
   180055039:	ff ff 
   18005503b:	48 89 5c 24 40       	mov    %rbx,0x40(%rsp)
   180055040:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180055045:	ba a0 0f 00 00       	mov    $0xfa0,%edx
   18005504a:	48 8d 0d 07 23 05 00 	lea    0x52307(%rip),%rcx        # 0x1800a7358
   180055051:	ff 15 61 f1 01 00    	call   *0x1f161(%rip)        # 0x1800741b8
   180055057:	90                   	nop
   180055058:	48 8d 0d b1 d1 03 00 	lea    0x3d1b1(%rip),%rcx        # 0x180092210
   18005505f:	ff 15 f3 ef 01 00    	call   *0x1eff3(%rip)        # 0x180074058
   180055065:	90                   	nop
   180055066:	48 8b d8             	mov    %rax,%rbx
   180055069:	48 85 c0             	test   %rax,%rax
   18005506c:	75 1a                	jne    0x180055088
   18005506e:	48 8d 0d e3 d1 03 00 	lea    0x3d1e3(%rip),%rcx        # 0x180092258
   180055075:	ff 15 dd ef 01 00    	call   *0x1efdd(%rip)        # 0x180074058
   18005507b:	90                   	nop
   18005507c:	48 8b d8             	mov    %rax,%rbx
   18005507f:	48 85 c0             	test   %rax,%rax
   180055082:	0f 84 f6 00 00 00    	je     0x18005517e
```

### Line 109456 (Address `0x180074058`)
```assembly
   18005f7e3:	cc                   	int3
   18005f7e4:	33 c0                	xor    %eax,%eax
   18005f7e6:	81 f9 63 73 6d e0    	cmp    $0xe06d7363,%ecx
   18005f7ec:	0f 94 c0             	sete   %al
   18005f7ef:	c3                   	ret
   18005f7f0:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18005f7f5:	44 89 44 24 18       	mov    %r8d,0x18(%rsp)
   18005f7fa:	89 54 24 10          	mov    %edx,0x10(%rsp)
   18005f7fe:	55                   	push   %rbp
   18005f7ff:	48 8b ec             	mov    %rsp,%rbp
   18005f802:	48 83 ec 50          	sub    $0x50,%rsp
   18005f806:	8b d9                	mov    %ecx,%ebx
   18005f808:	45 85 c0             	test   %r8d,%r8d
   18005f80b:	75 4a                	jne    0x18005f857
   18005f80d:	33 c9                	xor    %ecx,%ecx
   18005f80f:	ff 15 43 48 01 00    	call   *0x14843(%rip)        # 0x180074058
   18005f815:	48 85 c0             	test   %rax,%rax
   18005f818:	74 3d                	je     0x18005f857
   18005f81a:	b9 4d 5a 00 00       	mov    $0x5a4d,%ecx
   18005f81f:	66 39 08             	cmp    %cx,(%rax)
```

## `KERNEL32.dll!GetOEMCP` (1 Call Sites)

### Line 125053 (Address `0x180074038`)
```assembly
   18006c8d0:	5f                   	pop    %rdi
   18006c8d1:	c3                   	ret
   18006c8d2:	cc                   	int3
   18006c8d3:	cc                   	int3
   18006c8d4:	40 53                	rex push %rbx
   18006c8d6:	48 83 ec 40          	sub    $0x40,%rsp
   18006c8da:	8b d9                	mov    %ecx,%ebx
   18006c8dc:	33 d2                	xor    %edx,%edx
   18006c8de:	48 8d 4c 24 20       	lea    0x20(%rsp),%rcx
   18006c8e3:	e8 d4 d6 fe ff       	call   0x180059fbc
   18006c8e8:	83 25 79 bc 03 00 00 	andl   $0x0,0x3bc79(%rip)        # 0x1800a8568
   18006c8ef:	83 fb fe             	cmp    $0xfffffffe,%ebx
   18006c8f2:	75 12                	jne    0x18006c906
   18006c8f4:	c7 05 6a bc 03 00 01 	movl   $0x1,0x3bc6a(%rip)        # 0x1800a8568
   18006c8fb:	00 00 00 
   18006c8fe:	ff 15 34 77 00 00    	call   *0x7734(%rip)        # 0x180074038
   18006c904:	eb 15                	jmp    0x18006c91b
   18006c906:	83 fb fd             	cmp    $0xfffffffd,%ebx
   18006c909:	75 14                	jne    0x18006c91f
   18006c90b:	c7 05 53 bc 03 00 01 	movl   $0x1,0x3bc53(%rip)        # 0x1800a8568
```

## `KERNEL32.dll!GetProcAddress` (6 Call Sites)

### Line 96915 (Address `0x1800741c8`)
```assembly
   180055057:	90                   	nop
   180055058:	48 8d 0d b1 d1 03 00 	lea    0x3d1b1(%rip),%rcx        # 0x180092210
   18005505f:	ff 15 f3 ef 01 00    	call   *0x1eff3(%rip)        # 0x180074058
   180055065:	90                   	nop
   180055066:	48 8b d8             	mov    %rax,%rbx
   180055069:	48 85 c0             	test   %rax,%rax
   18005506c:	75 1a                	jne    0x180055088
   18005506e:	48 8d 0d e3 d1 03 00 	lea    0x3d1e3(%rip),%rcx        # 0x180092258
   180055075:	ff 15 dd ef 01 00    	call   *0x1efdd(%rip)        # 0x180074058
   18005507b:	90                   	nop
   18005507c:	48 8b d8             	mov    %rax,%rbx
   18005507f:	48 85 c0             	test   %rax,%rax
   180055082:	0f 84 f6 00 00 00    	je     0x18005517e
   180055088:	48 8d 15 e9 d1 03 00 	lea    0x3d1e9(%rip),%rdx        # 0x180092278
   18005508f:	48 8b cb             	mov    %rbx,%rcx
   180055092:	ff 15 30 f1 01 00    	call   *0x1f130(%rip)        # 0x1800741c8
   180055098:	90                   	nop
   180055099:	48 8b f0             	mov    %rax,%rsi
   18005509c:	48 8d 15 f5 d1 03 00 	lea    0x3d1f5(%rip),%rdx        # 0x180092298
   1800550a3:	48 8b cb             	mov    %rbx,%rcx
```

### Line 96920 (Address `0x1800741c8`)
```assembly
   180055069:	48 85 c0             	test   %rax,%rax
   18005506c:	75 1a                	jne    0x180055088
   18005506e:	48 8d 0d e3 d1 03 00 	lea    0x3d1e3(%rip),%rcx        # 0x180092258
   180055075:	ff 15 dd ef 01 00    	call   *0x1efdd(%rip)        # 0x180074058
   18005507b:	90                   	nop
   18005507c:	48 8b d8             	mov    %rax,%rbx
   18005507f:	48 85 c0             	test   %rax,%rax
   180055082:	0f 84 f6 00 00 00    	je     0x18005517e
   180055088:	48 8d 15 e9 d1 03 00 	lea    0x3d1e9(%rip),%rdx        # 0x180092278
   18005508f:	48 8b cb             	mov    %rbx,%rcx
   180055092:	ff 15 30 f1 01 00    	call   *0x1f130(%rip)        # 0x1800741c8
   180055098:	90                   	nop
   180055099:	48 8b f0             	mov    %rax,%rsi
   18005509c:	48 8d 15 f5 d1 03 00 	lea    0x3d1f5(%rip),%rdx        # 0x180092298
   1800550a3:	48 8b cb             	mov    %rbx,%rcx
   1800550a6:	ff 15 1c f1 01 00    	call   *0x1f11c(%rip)        # 0x1800741c8
   1800550ac:	90                   	nop
   1800550ad:	48 8b f8             	mov    %rax,%rdi
   1800550b0:	48 8d 15 01 d2 03 00 	lea    0x3d201(%rip),%rdx        # 0x1800922b8
   1800550b7:	48 8b cb             	mov    %rbx,%rcx
```

### Line 96925 (Address `0x1800741c8`)
```assembly
   18005507c:	48 8b d8             	mov    %rax,%rbx
   18005507f:	48 85 c0             	test   %rax,%rax
   180055082:	0f 84 f6 00 00 00    	je     0x18005517e
   180055088:	48 8d 15 e9 d1 03 00 	lea    0x3d1e9(%rip),%rdx        # 0x180092278
   18005508f:	48 8b cb             	mov    %rbx,%rcx
   180055092:	ff 15 30 f1 01 00    	call   *0x1f130(%rip)        # 0x1800741c8
   180055098:	90                   	nop
   180055099:	48 8b f0             	mov    %rax,%rsi
   18005509c:	48 8d 15 f5 d1 03 00 	lea    0x3d1f5(%rip),%rdx        # 0x180092298
   1800550a3:	48 8b cb             	mov    %rbx,%rcx
   1800550a6:	ff 15 1c f1 01 00    	call   *0x1f11c(%rip)        # 0x1800741c8
   1800550ac:	90                   	nop
   1800550ad:	48 8b f8             	mov    %rax,%rdi
   1800550b0:	48 8d 15 01 d2 03 00 	lea    0x3d201(%rip),%rdx        # 0x1800922b8
   1800550b7:	48 8b cb             	mov    %rbx,%rcx
   1800550ba:	ff 15 08 f1 01 00    	call   *0x1f108(%rip)        # 0x1800741c8
   1800550c0:	90                   	nop
   1800550c1:	48 8b d8             	mov    %rax,%rbx
   1800550c4:	48 85 f6             	test   %rsi,%rsi
   1800550c7:	74 7e                	je     0x180055147
```

### Line 101596 (Address `0x1800741c8`)
```assembly
   180058e88:	48 85 c0             	test   %rax,%rax
   180058e8b:	74 09                	je     0x180058e96
   180058e8d:	48 8b cb             	mov    %rbx,%rcx
   180058e90:	ff 15 e2 b3 01 00    	call   *0x1b3e2(%rip)        # 0x180074278
   180058e96:	48 85 db             	test   %rbx,%rbx
   180058e99:	75 55                	jne    0x180058ef0
   180058e9b:	48 83 c5 04          	add    $0x4,%rbp
   180058e9f:	49 3b ec             	cmp    %r12,%rbp
   180058ea2:	0f 85 2e ff ff ff    	jne    0x180058dd6
   180058ea8:	4c 8b 15 b1 d4 04 00 	mov    0x4d4b1(%rip),%r10        # 0x1800a6360
   180058eaf:	33 db                	xor    %ebx,%ebx
   180058eb1:	48 85 db             	test   %rbx,%rbx
   180058eb4:	74 4a                	je     0x180058f00
   180058eb6:	49 8b d5             	mov    %r13,%rdx
   180058eb9:	48 8b cb             	mov    %rbx,%rcx
   180058ebc:	ff 15 06 b3 01 00    	call   *0x1b306(%rip)        # 0x1800741c8
   180058ec2:	48 85 c0             	test   %rax,%rax
   180058ec5:	74 32                	je     0x180058ef9
   180058ec7:	4c 8b 05 92 d4 04 00 	mov    0x4d492(%rip),%r8        # 0x1800a6360
   180058ece:	ba 40 00 00 00       	mov    $0x40,%edx
```

### Line 109534 (Address `0x1800741c8`)
```assembly
   18005f8f5:	cc                   	int3
   18005f8f6:	cc                   	int3
   18005f8f7:	cc                   	int3
   18005f8f8:	40 53                	rex push %rbx
   18005f8fa:	48 83 ec 20          	sub    $0x20,%rsp
   18005f8fe:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   18005f904:	4c 8d 44 24 38       	lea    0x38(%rsp),%r8
   18005f909:	8b d9                	mov    %ecx,%ebx
   18005f90b:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x180093598
   18005f912:	33 c9                	xor    %ecx,%ecx
   18005f914:	ff 15 7e 49 01 00    	call   *0x1497e(%rip)        # 0x180074298
   18005f91a:	85 c0                	test   %eax,%eax
   18005f91c:	74 1f                	je     0x18005f93d
   18005f91e:	48 8b 4c 24 38       	mov    0x38(%rsp),%rcx
   18005f923:	48 8d 15 86 3c 03 00 	lea    0x33c86(%rip),%rdx        # 0x1800935b0
   18005f92a:	ff 15 98 48 01 00    	call   *0x14898(%rip)        # 0x1800741c8
   18005f930:	48 85 c0             	test   %rax,%rax
   18005f933:	74 08                	je     0x18005f93d
   18005f935:	8b cb                	mov    %ebx,%ecx
   18005f937:	ff 15 33 4a 01 00    	call   *0x14a33(%rip)        # 0x180074370
```

### Line 122230 (Address `0x1800741c8`)
```assembly
   18006a1f0:	48 85 c0             	test   %rax,%rax
   18006a1f3:	74 09                	je     0x18006a1fe
   18006a1f5:	48 8b cb             	mov    %rbx,%rcx
   18006a1f8:	ff 15 7a a0 00 00    	call   *0xa07a(%rip)        # 0x180074278
   18006a1fe:	48 85 db             	test   %rbx,%rbx
   18006a201:	75 55                	jne    0x18006a258
   18006a203:	48 83 c5 04          	add    $0x4,%rbp
   18006a207:	49 3b ec             	cmp    %r12,%rbp
   18006a20a:	0f 85 2e ff ff ff    	jne    0x18006a13e
   18006a210:	4c 8b 15 49 c1 03 00 	mov    0x3c149(%rip),%r10        # 0x1800a6360
   18006a217:	33 db                	xor    %ebx,%ebx
   18006a219:	48 85 db             	test   %rbx,%rbx
   18006a21c:	74 4a                	je     0x18006a268
   18006a21e:	49 8b d5             	mov    %r13,%rdx
   18006a221:	48 8b cb             	mov    %rbx,%rcx
   18006a224:	ff 15 9e 9f 00 00    	call   *0x9f9e(%rip)        # 0x1800741c8
   18006a22a:	48 85 c0             	test   %rax,%rax
   18006a22d:	74 32                	je     0x18006a261
   18006a22f:	4c 8b 05 2a c1 03 00 	mov    0x3c12a(%rip),%r8        # 0x1800a6360
   18006a236:	ba 40 00 00 00       	mov    $0x40,%edx
```

## `KERNEL32.dll!GetProcessHeap` (3 Call Sites)

### Line 29454 (Address `0x180074130`)
```assembly
   18001ac2c:	ff 15 be 96 05 00    	call   *0x596be(%rip)        # 0x1800742f0
   18001ac32:	ff 15 d0 94 05 00    	call   *0x594d0(%rip)        # 0x180074108
   18001ac38:	83 f8 7a             	cmp    $0x7a,%eax
   18001ac3b:	74 21                	je     0x18001ac5e
   18001ac3d:	ff 15 c5 94 05 00    	call   *0x594c5(%rip)        # 0x180074108
   18001ac43:	48 8b 0d be d9 08 00 	mov    0x8d9be(%rip),%rcx        # 0x1800a8608
   18001ac4a:	48 8d 15 9f 17 08 00 	lea    0x8179f(%rip),%rdx        # 0x18009c3f0
   18001ac51:	44 8b c0             	mov    %eax,%r8d
   18001ac54:	e8 37 b6 ff ff       	call   0x180016290
   18001ac59:	e9 2d 01 00 00       	jmp    0x18001ad8b
   18001ac5e:	48 89 9c 24 80 00 00 	mov    %rbx,0x80(%rsp)
   18001ac65:	00 
   18001ac66:	4c 89 b4 24 90 00 00 	mov    %r14,0x90(%rsp)
   18001ac6d:	00 
   18001ac6e:	44 8b 74 24 30       	mov    0x30(%rsp),%r14d
   18001ac73:	ff 15 b7 94 05 00    	call   *0x594b7(%rip)        # 0x180074130
   18001ac79:	45 8b c6             	mov    %r14d,%r8d
   18001ac7c:	ba 08 00 00 00       	mov    $0x8,%edx
   18001ac81:	48 8b c8             	mov    %rax,%rcx
   18001ac84:	ff 15 9e 94 05 00    	call   *0x5949e(%rip)        # 0x180074128
```

### Line 29506 (Address `0x180074130`)
```assembly
   18001ad0d:	48 83 e9 01          	sub    $0x1,%rcx
   18001ad11:	75 dd                	jne    0x18001acf0
   18001ad13:	48 85 c9             	test   %rcx,%rcx
   18001ad16:	48 8d 47 fe          	lea    -0x2(%rdi),%rax
   18001ad1a:	41 b8 7a 00 07 80    	mov    $0x8007007a,%r8d
   18001ad20:	48 0f 45 c7          	cmovne %rdi,%rax
   18001ad24:	45 0f 45 c7          	cmovne %r15d,%r8d
   18001ad28:	66 44 89 38          	mov    %r15w,(%rax)
   18001ad2c:	75 18                	jne    0x18001ad46
   18001ad2e:	48 8b 0d d3 d8 08 00 	mov    0x8d8d3(%rip),%rcx        # 0x1800a8608
   18001ad35:	48 8d 15 b4 17 08 00 	lea    0x817b4(%rip),%rdx        # 0x18009c4f0
   18001ad3c:	e8 4f b5 ff ff       	call   0x180016290
   18001ad41:	40 32 f6             	xor    %sil,%sil
   18001ad44:	eb 03                	jmp    0x18001ad49
   18001ad46:	40 b6 01             	mov    $0x1,%sil
   18001ad49:	ff 15 e1 93 05 00    	call   *0x593e1(%rip)        # 0x180074130
   18001ad4f:	4c 8b c3             	mov    %rbx,%r8
   18001ad52:	33 d2                	xor    %edx,%edx
   18001ad54:	48 8b c8             	mov    %rax,%rcx
   18001ad57:	ff 15 bb 93 05 00    	call   *0x593bb(%rip)        # 0x180074118
```

### Line 125773 (Address `0x180074130`)
```assembly
   18006d308:	74 09                	je     0x18006d313
   18006d30a:	48 8b cb             	mov    %rbx,%rcx
   18006d30d:	ff 15 fd 6c 00 00    	call   *0x6cfd(%rip)        # 0x180074010
   18006d313:	48 8b 5c 24 50       	mov    0x50(%rsp),%rbx
   18006d318:	48 8b c6             	mov    %rsi,%rax
   18006d31b:	48 8b 74 24 60       	mov    0x60(%rsp),%rsi
   18006d320:	48 8b 6c 24 58       	mov    0x58(%rsp),%rbp
   18006d325:	48 8b 7c 24 68       	mov    0x68(%rsp),%rdi
   18006d32a:	48 83 c4 40          	add    $0x40,%rsp
   18006d32e:	41 5e                	pop    %r14
   18006d330:	c3                   	ret
   18006d331:	cc                   	int3
   18006d332:	cc                   	int3
   18006d333:	cc                   	int3
   18006d334:	48 83 ec 28          	sub    $0x28,%rsp
   18006d338:	ff 15 f2 6d 00 00    	call   *0x6df2(%rip)        # 0x180074130
   18006d33e:	48 85 c0             	test   %rax,%rax
   18006d341:	48 89 05 58 b2 03 00 	mov    %rax,0x3b258(%rip)        # 0x1800a85a0
   18006d348:	0f 95 c0             	setne  %al
   18006d34b:	48 83 c4 28          	add    $0x28,%rsp
```

## `KERNEL32.dll!GetStartupInfoW` (1 Call Sites)

### Line 120185 (Address `0x180074228`)
```assembly
   1800686c8:	89 44 24 40          	mov    %eax,0x40(%rsp)
   1800686cc:	49 8d 4b 08          	lea    0x8(%r11),%rcx
   1800686d0:	e8 5b ff ff ff       	call   0x180068630
   1800686d5:	48 83 c4 28          	add    $0x28,%rsp
   1800686d9:	c3                   	ret
   1800686da:	cc                   	int3
   1800686db:	cc                   	int3
   1800686dc:	48 8b c4             	mov    %rsp,%rax
   1800686df:	48 89 58 08          	mov    %rbx,0x8(%rax)
   1800686e3:	48 89 68 10          	mov    %rbp,0x10(%rax)
   1800686e7:	48 89 70 18          	mov    %rsi,0x18(%rax)
   1800686eb:	48 89 78 20          	mov    %rdi,0x20(%rax)
   1800686ef:	41 56                	push   %r14
   1800686f1:	48 81 ec 90 00 00 00 	sub    $0x90,%rsp
   1800686f8:	48 8d 48 88          	lea    -0x78(%rax),%rcx
   1800686fc:	ff 15 26 bb 00 00    	call   *0xbb26(%rip)        # 0x180074228
   180068702:	45 33 f6             	xor    %r14d,%r14d
   180068705:	66 44 39 74 24 62    	cmp    %r14w,0x62(%rsp)
   18006870b:	0f 84 9a 00 00 00    	je     0x1800687ab
   180068711:	48 8b 44 24 68       	mov    0x68(%rsp),%rax
```

## `KERNEL32.dll!GetStdHandle` (2 Call Sites)

### Line 109017 (Address `0x180074288`)
```assembly
   18005f22c:	57                   	push   %rdi
   18005f22d:	41 56                	push   %r14
   18005f22f:	48 8d ac 24 10 fc ff 	lea    -0x3f0(%rsp),%rbp
   18005f236:	ff 
   18005f237:	48 81 ec f0 04 00 00 	sub    $0x4f0,%rsp
   18005f23e:	48 8b 05 1b 71 04 00 	mov    0x4711b(%rip),%rax        # 0x1800a6360
   18005f245:	48 33 c4             	xor    %rsp,%rax
   18005f248:	48 89 85 e0 03 00 00 	mov    %rax,0x3e0(%rbp)
   18005f24f:	48 8b f9             	mov    %rcx,%rdi
   18005f252:	48 89 4c 24 48       	mov    %rcx,0x48(%rsp)
   18005f257:	b9 f4 ff ff ff       	mov    $0xfffffff4,%ecx
   18005f25c:	48 89 54 24 40       	mov    %rdx,0x40(%rsp)
   18005f261:	45 8b f0             	mov    %r8d,%r14d
   18005f264:	44 89 44 24 38       	mov    %r8d,0x38(%rsp)
   18005f269:	48 8b f2             	mov    %rdx,%rsi
   18005f26c:	ff 15 16 50 01 00    	call   *0x15016(%rip)        # 0x180074288
   18005f272:	48 8b d8             	mov    %rax,%rbx
   18005f275:	48 8d 48 ff          	lea    -0x1(%rax),%rcx
   18005f279:	48 83 f9 fd          	cmp    $0xfffffffffffffffd,%rcx
   18005f27d:	77 72                	ja     0x18005f2f1
```

### Line 120279 (Address `0x180074288`)
```assembly
   180068813:	76 0a                	jbe    0x18006881f
   180068815:	80 4c df 38 80       	orb    $0x80,0x38(%rdi,%rbx,8)
   18006881a:	e9 8f 00 00 00       	jmp    0x1800688ae
   18006881f:	c6 44 df 38 81       	movb   $0x81,0x38(%rdi,%rbx,8)
   180068824:	8b ce                	mov    %esi,%ecx
   180068826:	85 f6                	test   %esi,%esi
   180068828:	74 16                	je     0x180068840
   18006882a:	83 e9 01             	sub    $0x1,%ecx
   18006882d:	74 0a                	je     0x180068839
   18006882f:	83 f9 01             	cmp    $0x1,%ecx
   180068832:	b9 f4 ff ff ff       	mov    $0xfffffff4,%ecx
   180068837:	eb 0c                	jmp    0x180068845
   180068839:	b9 f5 ff ff ff       	mov    $0xfffffff5,%ecx
   18006883e:	eb 05                	jmp    0x180068845
   180068840:	b9 f6 ff ff ff       	mov    $0xfffffff6,%ecx
   180068845:	ff 15 3d ba 00 00    	call   *0xba3d(%rip)        # 0x180074288
   18006884b:	48 8b e8             	mov    %rax,%rbp
   18006884e:	48 8d 48 01          	lea    0x1(%rax),%rcx
   180068852:	48 83 f9 01          	cmp    $0x1,%rcx
   180068856:	76 0b                	jbe    0x180068863
```

## `KERNEL32.dll!GetStringTypeW` (2 Call Sites)

### Line 128275 (Address `0x180074008`)
```assembly
   18006f6a2:	48 8b cb             	mov    %rbx,%rcx
   18006f6a5:	e8 86 77 fe ff       	call   0x180056e30
   18006f6aa:	45 8b cf             	mov    %r15d,%r9d
   18006f6ad:	44 89 74 24 28       	mov    %r14d,0x28(%rsp)
   18006f6b2:	4d 8b c4             	mov    %r12,%r8
   18006f6b5:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   18006f6ba:	ba 01 00 00 00       	mov    $0x1,%edx
   18006f6bf:	8b cf                	mov    %edi,%ecx
   18006f6c1:	e8 de 9f ff ff       	call   0x1800696a4
   18006f6c6:	85 c0                	test   %eax,%eax
   18006f6c8:	74 1a                	je     0x18006f6e4
   18006f6ca:	4c 8b 8d 80 00 00 00 	mov    0x80(%rbp),%r9
   18006f6d1:	44 8b c0             	mov    %eax,%r8d
   18006f6d4:	48 8b d3             	mov    %rbx,%rdx
   18006f6d7:	41 8b cd             	mov    %r13d,%ecx
   18006f6da:	ff 15 28 49 00 00    	call   *0x4928(%rip)        # 0x180074008
   18006f6e0:	8b f8                	mov    %eax,%edi
   18006f6e2:	eb 02                	jmp    0x18006f6e6
   18006f6e4:	33 ff                	xor    %edi,%edi
   18006f6e6:	48 85 db             	test   %rbx,%rbx
```

### Line 128533 (Address `0x180074008`)
```assembly
   18006fa2a:	f6 44 d0 38 01       	testb  $0x1,0x38(%rax,%rdx,8)
   18006fa2f:	74 07                	je     0x18006fa38
   18006fa31:	48 8b 44 d0 28       	mov    0x28(%rax,%rdx,8),%rax
   18006fa36:	eb 1c                	jmp    0x18006fa54
   18006fa38:	e8 07 fb fe ff       	call   0x18005f544
   18006fa3d:	83 20 00             	andl   $0x0,(%rax)
   18006fa40:	e8 1f fb fe ff       	call   0x18005f564
   18006fa45:	c7 00 09 00 00 00    	movl   $0x9,(%rax)
   18006fa4b:	e8 94 e3 fe ff       	call   0x18005dde4
   18006fa50:	48 83 c8 ff          	or     $0xffffffffffffffff,%rax
   18006fa54:	48 83 c4 28          	add    $0x28,%rsp
   18006fa58:	c3                   	ret
   18006fa59:	cc                   	int3
   18006fa5a:	cc                   	int3
   18006fa5b:	cc                   	int3
   18006fa5c:	48 ff 25 a5 45 00 00 	rex.W jmp *0x45a5(%rip)        # 0x180074008
   18006fa63:	cc                   	int3
   18006fa64:	48 8b c4             	mov    %rsp,%rax
   18006fa67:	48 89 58 08          	mov    %rbx,0x8(%rax)
   18006fa6b:	48 89 70 10          	mov    %rsi,0x10(%rax)
```

## `KERNEL32.dll!GetSystemTimeAsFileTime` (1 Call Sites)

### Line 97659 (Address `0x180074210`)
```assembly
   180055a8f:	f2 c3                	bnd ret
   180055a91:	cc                   	int3
   180055a92:	cc                   	int3
   180055a93:	cc                   	int3
   180055a94:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180055a99:	55                   	push   %rbp
   180055a9a:	48 8b ec             	mov    %rsp,%rbp
   180055a9d:	48 83 ec 20          	sub    $0x20,%rsp
   180055aa1:	48 8b 05 b8 08 05 00 	mov    0x508b8(%rip),%rax        # 0x1800a6360
   180055aa8:	48 bb 32 a2 df 2d 99 	movabs $0x2b992ddfa232,%rbx
   180055aaf:	2b 00 00 
   180055ab2:	48 3b c3             	cmp    %rbx,%rax
   180055ab5:	75 74                	jne    0x180055b2b
   180055ab7:	48 83 65 18 00       	andq   $0x0,0x18(%rbp)
   180055abc:	48 8d 4d 18          	lea    0x18(%rbp),%rcx
   180055ac0:	ff 15 4a e7 01 00    	call   *0x1e74a(%rip)        # 0x180074210
   180055ac6:	48 8b 45 18          	mov    0x18(%rbp),%rax
   180055aca:	48 89 45 10          	mov    %rax,0x10(%rbp)
   180055ace:	ff 15 04 e6 01 00    	call   *0x1e604(%rip)        # 0x1800740d8
   180055ad4:	8b c0                	mov    %eax,%eax
```

## `KERNEL32.dll!GetTickCount` (7 Call Sites)

### Line 22309 (Address `0x180074160`)
```assembly
   1800149a6:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   1800149ab:	48 8d 84 24 90 00 00 	lea    0x90(%rsp),%rax
   1800149b2:	00 
   1800149b3:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800149b8:	e8 63 8b 00 00       	call   0x18001d520
   1800149bd:	8b f8                	mov    %eax,%edi
   1800149bf:	85 c0                	test   %eax,%eax
   1800149c1:	78 6c                	js     0x180014a2f
   1800149c3:	8b 84 24 90 00 00 00 	mov    0x90(%rsp),%eax
   1800149ca:	89 83 34 02 00 00    	mov    %eax,0x234(%rbx)
   1800149d0:	8b 84 24 98 00 00 00 	mov    0x98(%rsp),%eax
   1800149d7:	89 83 38 02 00 00    	mov    %eax,0x238(%rbx)
   1800149dd:	8b 44 24 40          	mov    0x40(%rsp),%eax
   1800149e1:	89 83 30 02 00 00    	mov    %eax,0x230(%rbx)
   1800149e7:	c6 83 3c 02 00 00 01 	movb   $0x1,0x23c(%rbx)
   1800149ee:	ff 15 6c f7 05 00    	call   *0x5f76c(%rip)        # 0x180074160
   1800149f4:	44 8b 4b 18          	mov    0x18(%rbx),%r9d
   1800149f8:	89 83 98 05 00 00    	mov    %eax,0x598(%rbx)
   1800149fe:	41 83 f9 03          	cmp    $0x3,%r9d
   180014a02:	74 29                	je     0x180014a2d
```

### Line 30247 (Address `0x180074160`)
```assembly
   18001b8cd:	41 80 c8 3c          	or     $0x3c,%r8b
   18001b8d1:	48 8b cb             	mov    %rbx,%rcx
   18001b8d4:	e8 d7 2b 00 00       	call   0x18001e4b0
   18001b8d9:	4c 8d 45 c0          	lea    -0x40(%rbp),%r8
   18001b8dd:	b2 b1                	mov    $0xb1,%dl
   18001b8df:	48 8b cb             	mov    %rbx,%rcx
   18001b8e2:	e8 69 29 00 00       	call   0x18001e250
   18001b8e7:	44 0f b6 45 c0       	movzbl -0x40(%rbp),%r8d
   18001b8ec:	b2 b1                	mov    $0xb1,%dl
   18001b8ee:	41 80 c8 3c          	or     $0x3c,%r8b
   18001b8f2:	48 8b cb             	mov    %rbx,%rcx
   18001b8f5:	e8 b6 2b 00 00       	call   0x18001e4b0
   18001b8fa:	ba 01 00 00 00       	mov    $0x1,%edx
   18001b8ff:	48 8b cb             	mov    %rbx,%rcx
   18001b902:	e8 a9 1e 00 00       	call   0x18001d7b0
   18001b907:	ff 15 53 88 05 00    	call   *0x58853(%rip)        # 0x180074160
   18001b90d:	48 8b cb             	mov    %rbx,%rcx
   18001b910:	89 83 7c 05 00 00    	mov    %eax,0x57c(%rbx)
   18001b916:	e8 45 00 00 00       	call   0x18001b960
   18001b91b:	84 c0                	test   %al,%al
```

### Line 32036 (Address `0x180074160`)
```assembly
   18001d32a:	cc                   	int3
   18001d32b:	cc                   	int3
   18001d32c:	cc                   	int3
   18001d32d:	cc                   	int3
   18001d32e:	cc                   	int3
   18001d32f:	cc                   	int3
   18001d330:	40 53                	rex push %rbx
   18001d332:	48 83 ec 20          	sub    $0x20,%rsp
   18001d336:	0f b6 41 15          	movzbl 0x15(%rcx),%eax
   18001d33a:	48 8b d9             	mov    %rcx,%rbx
   18001d33d:	84 c0                	test   %al,%al
   18001d33f:	0f 85 cc 01 00 00    	jne    0x18001d511
   18001d345:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
   18001d34a:	33 f6                	xor    %esi,%esi
   18001d34c:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   18001d351:	ff 15 09 6e 05 00    	call   *0x56e09(%rip)        # 0x180074160
   18001d357:	8b f8                	mov    %eax,%edi
   18001d359:	40 38 73 14          	cmp    %sil,0x14(%rbx)
   18001d35d:	75 10                	jne    0x18001d36f
   18001d35f:	b9 e8 03 00 00       	mov    $0x3e8,%ecx
```

### Line 32398 (Address `0x180074160`)
```assembly
   18001d82f:	e9 ab 04 00 00       	jmp    0x18001dcdf
   18001d834:	80 b9 96 05 00 00 00 	cmpb   $0x0,0x596(%rcx)
   18001d83b:	75 15                	jne    0x18001d852
   18001d83d:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001d842:	ff 15 38 68 05 00    	call   *0x56838(%rip)        # 0x180074080
   18001d848:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001d84d:	e9 8d 04 00 00       	jmp    0x18001dcdf
   18001d852:	48 8b 3d c7 ad 08 00 	mov    0x8adc7(%rip),%rdi        # 0x1800a8620
   18001d859:	48 89 6c 24 78       	mov    %rbp,0x78(%rsp)
   18001d85e:	48 89 b4 24 80 00 00 	mov    %rsi,0x80(%rsp)
   18001d865:	00 
   18001d866:	4c 89 6c 24 50       	mov    %r13,0x50(%rsp)
   18001d86b:	48 63 87 68 20 00 00 	movslq 0x2068(%rdi),%rax
   18001d872:	c7 44 c7 68 46 00 00 	movl   $0x46,0x68(%rdi,%rax,8)
   18001d879:	00 
   18001d87a:	ff 15 e0 68 05 00    	call   *0x568e0(%rip)        # 0x180074160
   18001d880:	44 8b c0             	mov    %eax,%r8d
   18001d883:	33 ed                	xor    %ebp,%ebp
   18001d885:	b8 1f 85 eb 51       	mov    $0x51eb851f,%eax
   18001d88a:	41 f7 e0             	mul    %r8d
```

### Line 32461 (Address `0x180074160`)
```assembly
   18001d957:	e8 e4 28 00 00       	call   0x180020240
   18001d95c:	33 d2                	xor    %edx,%edx
   18001d95e:	48 8b cb             	mov    %rbx,%rcx
   18001d961:	e8 7a 2d 00 00       	call   0x1800206e0
   18001d966:	33 d2                	xor    %edx,%edx
   18001d968:	40 88 ab a8 01 00 00 	mov    %bpl,0x1a8(%rbx)
   18001d96f:	48 8b cb             	mov    %rbx,%rcx
   18001d972:	e8 79 1e 00 00       	call   0x18001f7f0
   18001d977:	ba 01 00 00 00       	mov    $0x1,%edx
   18001d97c:	40 88 ab 96 05 00 00 	mov    %bpl,0x596(%rbx)
   18001d983:	48 8b cb             	mov    %rbx,%rcx
   18001d986:	e8 b5 e0 ff ff       	call   0x18001ba40
   18001d98b:	b8 fc ff ff ff       	mov    $0xfffffffc,%eax
   18001d990:	40 88 ab a0 05 00 00 	mov    %bpl,0x5a0(%rbx)
   18001d997:	e9 31 03 00 00       	jmp    0x18001dccd
   18001d99c:	ff 15 be 67 05 00    	call   *0x567be(%rip)        # 0x180074160
   18001d9a2:	8b 8b 98 05 00 00    	mov    0x598(%rbx),%ecx
   18001d9a8:	81 c1 c4 09 00 00    	add    $0x9c4,%ecx
   18001d9ae:	3b c1                	cmp    %ecx,%eax
   18001d9b0:	0f 86 83 00 00 00    	jbe    0x18001da39
```

### Line 32596 (Address `0x180074160`)
```assembly
   18001dbd0:	41 8d 45 01          	lea    0x1(%r13),%eax
   18001dbd4:	4c 8b 74 24 48       	mov    0x48(%rsp),%r14
   18001dbd9:	89 ae c8 01 00 00    	mov    %ebp,0x1c8(%rsi)
   18001dbdf:	87 83 b0 01 00 00    	xchg   %eax,0x1b0(%rbx)
   18001dbe5:	85 ff                	test   %edi,%edi
   18001dbe7:	79 29                	jns    0x18001dc12
   18001dbe9:	48 8b 0d 30 aa 08 00 	mov    0x8aa30(%rip),%rcx        # 0x1800a8620
   18001dbf0:	ff 41 08             	incl   0x8(%rcx)
   18001dbf3:	83 ff 8c             	cmp    $0xffffff8c,%edi
   18001dbf6:	75 13                	jne    0x18001dc0b
   18001dbf8:	48 8b 0d 09 aa 08 00 	mov    0x8aa09(%rip),%rcx        # 0x1800a8608
   18001dbff:	48 8d 15 3a fa 07 00 	lea    0x7fa3a(%rip),%rdx        # 0x18009d640
   18001dc06:	e8 85 86 ff ff       	call   0x180016290
   18001dc0b:	8b c7                	mov    %edi,%eax
   18001dc0d:	e9 bb 00 00 00       	jmp    0x18001dccd
   18001dc12:	ff 15 48 65 05 00    	call   *0x56548(%rip)        # 0x180074160
   18001dc18:	48 8b 3d 01 aa 08 00 	mov    0x8aa01(%rip),%rdi        # 0x1800a8620
   18001dc1f:	89 83 98 05 00 00    	mov    %eax,0x598(%rbx)
   18001dc25:	ff 47 40             	incl   0x40(%rdi)
   18001dc28:	8b 83 28 02 00 00    	mov    0x228(%rbx),%eax
```

### Line 32622 (Address `0x180074160`)
```assembly
   18001dc44:	44 8b 86 bc 01 00 00 	mov    0x1bc(%rsi),%r8d
   18001dc4b:	48 8d 15 3e fa 07 00 	lea    0x7fa3e(%rip),%rdx        # 0x18009d690
   18001dc52:	48 8b 0d af a9 08 00 	mov    0x8a9af(%rip),%rcx        # 0x1800a8608
   18001dc59:	e8 32 86 ff ff       	call   0x180016290
   18001dc5e:	b2 01                	mov    $0x1,%dl
   18001dc60:	48 8b cb             	mov    %rbx,%rcx
   18001dc63:	e8 78 2a 00 00       	call   0x1800206e0
   18001dc68:	b2 01                	mov    $0x1,%dl
   18001dc6a:	48 8b cb             	mov    %rbx,%rcx
   18001dc6d:	e8 ce 25 00 00       	call   0x180020240
   18001dc72:	48 8b 3d a7 a9 08 00 	mov    0x8a9a7(%rip),%rdi        # 0x1800a8620
   18001dc79:	c6 83 a8 01 00 00 01 	movb   $0x1,0x1a8(%rbx)
   18001dc80:	48 63 8f 68 20 00 00 	movslq 0x2068(%rdi),%rcx
   18001dc87:	c7 44 cf 68 47 00 00 	movl   $0x47,0x68(%rdi,%rcx,8)
   18001dc8e:	00 
   18001dc8f:	ff 15 cb 64 05 00    	call   *0x564cb(%rip)        # 0x180074160
   18001dc95:	44 8b c0             	mov    %eax,%r8d
   18001dc98:	b8 1f 85 eb 51       	mov    $0x51eb851f,%eax
   18001dc9d:	41 f7 e0             	mul    %r8d
   18001dca0:	c1 ea 05             	shr    $0x5,%edx
```

## `KERNEL32.dll!HeapAlloc` (3 Call Sites)

### Line 29458 (Address `0x180074128`)
```assembly
   18001ac3d:	ff 15 c5 94 05 00    	call   *0x594c5(%rip)        # 0x180074108
   18001ac43:	48 8b 0d be d9 08 00 	mov    0x8d9be(%rip),%rcx        # 0x1800a8608
   18001ac4a:	48 8d 15 9f 17 08 00 	lea    0x8179f(%rip),%rdx        # 0x18009c3f0
   18001ac51:	44 8b c0             	mov    %eax,%r8d
   18001ac54:	e8 37 b6 ff ff       	call   0x180016290
   18001ac59:	e9 2d 01 00 00       	jmp    0x18001ad8b
   18001ac5e:	48 89 9c 24 80 00 00 	mov    %rbx,0x80(%rsp)
   18001ac65:	00 
   18001ac66:	4c 89 b4 24 90 00 00 	mov    %r14,0x90(%rsp)
   18001ac6d:	00 
   18001ac6e:	44 8b 74 24 30       	mov    0x30(%rsp),%r14d
   18001ac73:	ff 15 b7 94 05 00    	call   *0x594b7(%rip)        # 0x180074130
   18001ac79:	45 8b c6             	mov    %r14d,%r8d
   18001ac7c:	ba 08 00 00 00       	mov    $0x8,%edx
   18001ac81:	48 8b c8             	mov    %rax,%rcx
   18001ac84:	ff 15 9e 94 05 00    	call   *0x5949e(%rip)        # 0x180074128
   18001ac8a:	48 8b d8             	mov    %rax,%rbx
   18001ac8d:	48 85 c0             	test   %rax,%rax
   18001ac90:	0f 84 c9 00 00 00    	je     0x18001ad5f
   18001ac96:	c7 00 08 00 00 00    	movl   $0x8,(%rax)
```

### Line 117973 (Address `0x180074128`)
```assembly
   180066909:	77 3c                	ja     0x180066947
   18006690b:	48 85 c9             	test   %rcx,%rcx
   18006690e:	b8 01 00 00 00       	mov    $0x1,%eax
   180066913:	48 0f 44 d8          	cmove  %rax,%rbx
   180066917:	eb 15                	jmp    0x18006692e
   180066919:	e8 ba 6f 00 00       	call   0x18006d8d8
   18006691e:	85 c0                	test   %eax,%eax
   180066920:	74 25                	je     0x180066947
   180066922:	48 8b cb             	mov    %rbx,%rcx
   180066925:	e8 f2 ec ff ff       	call   0x18006561c
   18006692a:	85 c0                	test   %eax,%eax
   18006692c:	74 19                	je     0x180066947
   18006692e:	48 8b 0d 6b 1c 04 00 	mov    0x41c6b(%rip),%rcx        # 0x1800a85a0
   180066935:	4c 8b c3             	mov    %rbx,%r8
   180066938:	33 d2                	xor    %edx,%edx
   18006693a:	ff 15 e8 d7 00 00    	call   *0xd7e8(%rip)        # 0x180074128
   180066940:	48 85 c0             	test   %rax,%rax
   180066943:	74 d4                	je     0x180066919
   180066945:	eb 0d                	jmp    0x180066954
   180066947:	e8 18 8c ff ff       	call   0x18005f564
```

### Line 121353 (Address `0x180074128`)
```assembly
   18006964b:	49 0f af d8          	imul   %r8,%rbx
   18006964f:	b8 01 00 00 00       	mov    $0x1,%eax
   180069654:	48 85 db             	test   %rbx,%rbx
   180069657:	48 0f 44 d8          	cmove  %rax,%rbx
   18006965b:	eb 15                	jmp    0x180069672
   18006965d:	e8 76 42 00 00       	call   0x18006d8d8
   180069662:	85 c0                	test   %eax,%eax
   180069664:	74 28                	je     0x18006968e
   180069666:	48 8b cb             	mov    %rbx,%rcx
   180069669:	e8 ae bf ff ff       	call   0x18006561c
   18006966e:	85 c0                	test   %eax,%eax
   180069670:	74 1c                	je     0x18006968e
   180069672:	48 8b 0d 27 ef 03 00 	mov    0x3ef27(%rip),%rcx        # 0x1800a85a0
   180069679:	4c 8b c3             	mov    %rbx,%r8
   18006967c:	ba 08 00 00 00       	mov    $0x8,%edx
   180069681:	ff 15 a1 aa 00 00    	call   *0xaaa1(%rip)        # 0x180074128
   180069687:	48 85 c0             	test   %rax,%rax
   18006968a:	74 d1                	je     0x18006965d
   18006968c:	eb 0d                	jmp    0x18006969b
   18006968e:	e8 d1 5e ff ff       	call   0x18005f564
```

## `KERNEL32.dll!HeapFree` (2 Call Sites)

### Line 29510 (Address `0x180074118`)
```assembly
   18001ad1a:	41 b8 7a 00 07 80    	mov    $0x8007007a,%r8d
   18001ad20:	48 0f 45 c7          	cmovne %rdi,%rax
   18001ad24:	45 0f 45 c7          	cmovne %r15d,%r8d
   18001ad28:	66 44 89 38          	mov    %r15w,(%rax)
   18001ad2c:	75 18                	jne    0x18001ad46
   18001ad2e:	48 8b 0d d3 d8 08 00 	mov    0x8d8d3(%rip),%rcx        # 0x1800a8608
   18001ad35:	48 8d 15 b4 17 08 00 	lea    0x817b4(%rip),%rdx        # 0x18009c4f0
   18001ad3c:	e8 4f b5 ff ff       	call   0x180016290
   18001ad41:	40 32 f6             	xor    %sil,%sil
   18001ad44:	eb 03                	jmp    0x18001ad49
   18001ad46:	40 b6 01             	mov    $0x1,%sil
   18001ad49:	ff 15 e1 93 05 00    	call   *0x593e1(%rip)        # 0x180074130
   18001ad4f:	4c 8b c3             	mov    %rbx,%r8
   18001ad52:	33 d2                	xor    %edx,%edx
   18001ad54:	48 8b c8             	mov    %rax,%rcx
   18001ad57:	ff 15 bb 93 05 00    	call   *0x593bb(%rip)        # 0x180074118
   18001ad5d:	eb 1c                	jmp    0x18001ad7b
   18001ad5f:	ff 15 a3 93 05 00    	call   *0x593a3(%rip)        # 0x180074108
   18001ad65:	48 8b 0d 9c d8 08 00 	mov    0x8d89c(%rip),%rcx        # 0x1800a8608
   18001ad6c:	48 8d 15 0d 17 08 00 	lea    0x8170d(%rip),%rdx        # 0x18009c480
```

### Line 117939 (Address `0x180074118`)
```assembly
   1800668ab:	83 f8 19             	cmp    $0x19,%eax
   1800668ae:	77 03                	ja     0x1800668b3
   1800668b0:	83 c1 20             	add    $0x20,%ecx
   1800668b3:	8b c1                	mov    %ecx,%eax
   1800668b5:	48 83 c4 28          	add    $0x28,%rsp
   1800668b9:	c3                   	ret
   1800668ba:	cc                   	int3
   1800668bb:	cc                   	int3
   1800668bc:	48 85 c9             	test   %rcx,%rcx
   1800668bf:	74 37                	je     0x1800668f8
   1800668c1:	53                   	push   %rbx
   1800668c2:	48 83 ec 20          	sub    $0x20,%rsp
   1800668c6:	4c 8b c1             	mov    %rcx,%r8
   1800668c9:	33 d2                	xor    %edx,%edx
   1800668cb:	48 8b 0d ce 1c 04 00 	mov    0x41cce(%rip),%rcx        # 0x1800a85a0
   1800668d2:	ff 15 40 d8 00 00    	call   *0xd840(%rip)        # 0x180074118
   1800668d8:	85 c0                	test   %eax,%eax
   1800668da:	75 17                	jne    0x1800668f3
   1800668dc:	e8 83 8c ff ff       	call   0x18005f564
   1800668e1:	48 8b d8             	mov    %rax,%rbx
```

## `KERNEL32.dll!HeapReAlloc` (1 Call Sites)

### Line 125925 (Address `0x180074148`)
```assembly
   18006d4ea:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18006d4ef:	48 83 c4 20          	add    $0x20,%rsp
   18006d4f3:	5f                   	pop    %rdi
   18006d4f4:	c3                   	ret
   18006d4f5:	e8 de 03 00 00       	call   0x18006d8d8
   18006d4fa:	85 c0                	test   %eax,%eax
   18006d4fc:	74 df                	je     0x18006d4dd
   18006d4fe:	48 8b cb             	mov    %rbx,%rcx
   18006d501:	e8 16 81 ff ff       	call   0x18006561c
   18006d506:	85 c0                	test   %eax,%eax
   18006d508:	74 d3                	je     0x18006d4dd
   18006d50a:	48 8b 0d 8f b0 03 00 	mov    0x3b08f(%rip),%rcx        # 0x1800a85a0
   18006d511:	4c 8b cb             	mov    %rbx,%r9
   18006d514:	4c 8b c7             	mov    %rdi,%r8
   18006d517:	33 d2                	xor    %edx,%edx
   18006d519:	ff 15 29 6c 00 00    	call   *0x6c29(%rip)        # 0x180074148
   18006d51f:	48 85 c0             	test   %rax,%rax
   18006d522:	74 d1                	je     0x18006d4f5
   18006d524:	eb c4                	jmp    0x18006d4ea
   18006d526:	cc                   	int3
```

## `KERNEL32.dll!HeapSize` (1 Call Sites)

### Line 125887 (Address `0x180074140`)
```assembly
   18006d46e:	cc                   	int3
   18006d46f:	cc                   	int3
   18006d470:	48 83 ec 28          	sub    $0x28,%rsp
   18006d474:	48 85 c9             	test   %rcx,%rcx
   18006d477:	75 19                	jne    0x18006d492
   18006d479:	e8 e6 20 ff ff       	call   0x18005f564
   18006d47e:	c7 00 16 00 00 00    	movl   $0x16,(%rax)
   18006d484:	e8 5b 09 ff ff       	call   0x18005dde4
   18006d489:	48 83 c8 ff          	or     $0xffffffffffffffff,%rax
   18006d48d:	48 83 c4 28          	add    $0x28,%rsp
   18006d491:	c3                   	ret
   18006d492:	4c 8b c1             	mov    %rcx,%r8
   18006d495:	33 d2                	xor    %edx,%edx
   18006d497:	48 8b 0d 02 b1 03 00 	mov    0x3b102(%rip),%rcx        # 0x1800a85a0
   18006d49e:	48 83 c4 28          	add    $0x28,%rsp
   18006d4a2:	48 ff 25 97 6c 00 00 	rex.W jmp *0x6c97(%rip)        # 0x180074140
   18006d4a9:	cc                   	int3
   18006d4aa:	cc                   	int3
   18006d4ab:	cc                   	int3
   18006d4ac:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
```

## `KERNEL32.dll!InitializeCriticalSection` (7 Call Sites)

### Line 23240 (Address `0x1800740c8`)
```assembly
   180015598:	85 c0                	test   %eax,%eax
   18001559a:	0f 85 10 01 00 00    	jne    0x1800156b0
   1800155a0:	8d 48 70             	lea    0x70(%rax),%ecx
   1800155a3:	e8 0c fa 03 00       	call   0x180054fb4
   1800155a8:	48 8b f8             	mov    %rax,%rdi
   1800155ab:	45 8d 46 58          	lea    0x58(%r14),%r8d
   1800155af:	33 c0                	xor    %eax,%eax
   1800155b1:	33 d2                	xor    %edx,%edx
   1800155b3:	48 8d 4f 18          	lea    0x18(%rdi),%rcx
   1800155b7:	48 89 47 08          	mov    %rax,0x8(%rdi)
   1800155bb:	e8 70 18 04 00       	call   0x180056e30
   1800155c0:	48 8d 05 c1 54 08 00 	lea    0x854c1(%rip),%rax        # 0x18009aa88
   1800155c7:	48 89 07             	mov    %rax,(%rdi)
   1800155ca:	48 8d 4f 18          	lea    0x18(%rdi),%rcx
   1800155ce:	4c 89 7f 10          	mov    %r15,0x10(%rdi)
   1800155d2:	ff 15 f0 ea 05 00    	call   *0x5eaf0(%rip)        # 0x1800740c8
   1800155d8:	48 8d 4f 40          	lea    0x40(%rdi),%rcx
   1800155dc:	e8 6f 48 00 00       	call   0x180019e50
   1800155e1:	48 8b cf             	mov    %rdi,%rcx
   1800155e4:	4c 89 77 60          	mov    %r14,0x60(%rdi)
```

### Line 23258 (Address `0x1800740c8`)
```assembly
   1800155e1:	48 8b cf             	mov    %rdi,%rcx
   1800155e4:	4c 89 77 60          	mov    %r14,0x60(%rdi)
   1800155e8:	89 5f 0c             	mov    %ebx,0xc(%rdi)
   1800155eb:	e8 f0 07 00 00       	call   0x180015de0
   1800155f0:	48 8b cf             	mov    %rdi,%rcx
   1800155f3:	e8 b8 09 00 00       	call   0x180015fb0
   1800155f8:	41 8d 4e 70          	lea    0x70(%r14),%ecx
   1800155fc:	e8 b3 f9 03 00       	call   0x180054fb4
   180015601:	33 d2                	xor    %edx,%edx
   180015603:	45 8d 46 68          	lea    0x68(%r14),%r8d
   180015607:	48 8b d8             	mov    %rax,%rbx
   18001560a:	48 8d 48 08          	lea    0x8(%rax),%rcx
   18001560e:	e8 1d 18 04 00       	call   0x180056e30
   180015613:	48 8d 4b 08          	lea    0x8(%rbx),%rcx
   180015617:	4c 89 3b             	mov    %r15,(%rbx)
   18001561a:	ff 15 a8 ea 05 00    	call   *0x5eaa8(%rip)        # 0x1800740c8
   180015620:	4c 89 73 30          	mov    %r14,0x30(%rbx)
   180015624:	4c 89 73 38          	mov    %r14,0x38(%rbx)
   180015628:	e8 83 16 00 00       	call   0x180016cb0
   18001562d:	48 89 43 30          	mov    %rax,0x30(%rbx)
```

### Line 23454 (Address `0x1800740c8`)
```assembly
   18001594b:	41 c6 46 15 00       	movb   $0x0,0x15(%r14)
   180015950:	33 d2                	xor    %edx,%edx
   180015952:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   180015959:	00 
   18001595a:	ff 15 30 e7 05 00    	call   *0x5e730(%rip)        # 0x180074090
   180015960:	41 89 5e 1c          	mov    %ebx,0x1c(%r14)
   180015964:	49 8d 8e 18 02 00 00 	lea    0x218(%r14),%rcx
   18001596b:	49 89 46 08          	mov    %rax,0x8(%r14)
   18001596f:	48 8d 1d d2 57 08 00 	lea    0x857d2(%rip),%rbx        # 0x18009b148
   180015976:	48 8d 05 6b 52 08 00 	lea    0x8526b(%rip),%rax        # 0x18009abe8
   18001597d:	41 89 7e 18          	mov    %edi,0x18(%r14)
   180015981:	49 89 06             	mov    %rax,(%r14)
   180015984:	66 41 c7 46 20 00 00 	movw   $0x0,0x20(%r14)
   18001598b:	41 89 b6 0c 02 00 00 	mov    %esi,0x20c(%r14)
   180015992:	49 89 9e 10 02 00 00 	mov    %rbx,0x210(%r14)
   180015999:	ff 15 29 e7 05 00    	call   *0x5e729(%rip)        # 0x1800740c8
   18001599f:	49 8d 8e 48 02 00 00 	lea    0x248(%r14),%rcx
   1800159a6:	49 89 9e 40 02 00 00 	mov    %rbx,0x240(%r14)
   1800159ad:	ff 15 15 e7 05 00    	call   *0x5e715(%rip)        # 0x1800740c8
   1800159b3:	49 8d 4e 24          	lea    0x24(%r14),%rcx
```

### Line 23457 (Address `0x1800740c8`)
```assembly
   180015959:	00 
   18001595a:	ff 15 30 e7 05 00    	call   *0x5e730(%rip)        # 0x180074090
   180015960:	41 89 5e 1c          	mov    %ebx,0x1c(%r14)
   180015964:	49 8d 8e 18 02 00 00 	lea    0x218(%r14),%rcx
   18001596b:	49 89 46 08          	mov    %rax,0x8(%r14)
   18001596f:	48 8d 1d d2 57 08 00 	lea    0x857d2(%rip),%rbx        # 0x18009b148
   180015976:	48 8d 05 6b 52 08 00 	lea    0x8526b(%rip),%rax        # 0x18009abe8
   18001597d:	41 89 7e 18          	mov    %edi,0x18(%r14)
   180015981:	49 89 06             	mov    %rax,(%r14)
   180015984:	66 41 c7 46 20 00 00 	movw   $0x0,0x20(%r14)
   18001598b:	41 89 b6 0c 02 00 00 	mov    %esi,0x20c(%r14)
   180015992:	49 89 9e 10 02 00 00 	mov    %rbx,0x210(%r14)
   180015999:	ff 15 29 e7 05 00    	call   *0x5e729(%rip)        # 0x1800740c8
   18001599f:	49 8d 8e 48 02 00 00 	lea    0x248(%r14),%rcx
   1800159a6:	49 89 9e 40 02 00 00 	mov    %rbx,0x240(%r14)
   1800159ad:	ff 15 15 e7 05 00    	call   *0x5e715(%rip)        # 0x1800740c8
   1800159b3:	49 8d 4e 24          	lea    0x24(%r14),%rcx
   1800159b7:	41 c7 86 70 02 00 00 	movl   $0x0,0x270(%r14)
   1800159be:	00 00 00 00 
   1800159c2:	48 8d 44 24 6c       	lea    0x6c(%rsp),%rax
```

### Line 23987 (Address `0x1800740c8`)
```assembly
   180016157:	90                   	nop
   180016158:	48 8d 05 a9 81 08 00 	lea    0x881a9(%rip),%rax        # 0x18009e308
   18001615f:	48 89 06             	mov    %rax,(%rsi)
   180016162:	48 8d 4e 48          	lea    0x48(%rsi),%rcx
   180016166:	e8 e5 3c 00 00       	call   0x180019e50
   18001616b:	90                   	nop
   18001616c:	48 8d 4e 68          	lea    0x68(%rsi),%rcx
   180016170:	e8 db 3c 00 00       	call   0x180019e50
   180016175:	66 c7 86 88 00 00 00 	movw   $0x100,0x88(%rsi)
   18001617c:	00 01 
   18001617e:	48 c7 86 90 00 00 00 	movq   $0x0,0x90(%rsi)
   180016185:	00 00 00 00 
   180016189:	48 8d 05 b8 4f 08 00 	lea    0x84fb8(%rip),%rax        # 0x18009b148
   180016190:	48 89 86 98 00 00 00 	mov    %rax,0x98(%rsi)
   180016197:	48 8d 8e a0 00 00 00 	lea    0xa0(%rsi),%rcx
   18001619e:	ff 15 24 df 05 00    	call   *0x5df24(%rip)        # 0x1800740c8
   1800161a4:	90                   	nop
   1800161a5:	49 89 5f 60          	mov    %rbx,0x60(%r15)
   1800161a9:	49 8b 5f 48          	mov    0x48(%r15),%rbx
   1800161ad:	48 8d 4e 68          	lea    0x68(%rsi),%rcx
```

### Line 29589 (Address `0x1800740c8`)
```assembly
   18001ae1c:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   18001ae23:	00 
   18001ae24:	4c 8b c9             	mov    %rcx,%r9
   18001ae27:	4c 8d 05 b2 ef ff ff 	lea    -0x104e(%rip),%r8        # 0x180019de0
   18001ae2e:	33 d2                	xor    %edx,%edx
   18001ae30:	33 c9                	xor    %ecx,%ecx
   18001ae32:	ff 15 58 92 05 00    	call   *0x59258(%rip)        # 0x180074090
   18001ae38:	48 89 46 08          	mov    %rax,0x8(%rsi)
   18001ae3c:	48 8d 05 ed 1a 08 00 	lea    0x81aed(%rip),%rax        # 0x18009c930
   18001ae43:	48 89 06             	mov    %rax,(%rsi)
   18001ae46:	45 33 ff             	xor    %r15d,%r15d
   18001ae49:	4c 89 7e 28          	mov    %r15,0x28(%rsi)
   18001ae4d:	48 8d 2d f4 02 08 00 	lea    0x802f4(%rip),%rbp        # 0x18009b148
   18001ae54:	48 89 6e 50          	mov    %rbp,0x50(%rsi)
   18001ae58:	48 8d 4e 58          	lea    0x58(%rsi),%rcx
   18001ae5c:	ff 15 66 92 05 00    	call   *0x59266(%rip)        # 0x1800740c8
   18001ae62:	90                   	nop
   18001ae63:	c7 86 80 00 00 00 ff 	movl   $0xffffffff,0x80(%rsi)
   18001ae6a:	ff ff ff 
   18001ae6d:	89 9e 84 00 00 00    	mov    %ebx,0x84(%rsi)
```

### Line 29597 (Address `0x1800740c8`)
```assembly
   18001ae3c:	48 8d 05 ed 1a 08 00 	lea    0x81aed(%rip),%rax        # 0x18009c930
   18001ae43:	48 89 06             	mov    %rax,(%rsi)
   18001ae46:	45 33 ff             	xor    %r15d,%r15d
   18001ae49:	4c 89 7e 28          	mov    %r15,0x28(%rsi)
   18001ae4d:	48 8d 2d f4 02 08 00 	lea    0x802f4(%rip),%rbp        # 0x18009b148
   18001ae54:	48 89 6e 50          	mov    %rbp,0x50(%rsi)
   18001ae58:	48 8d 4e 58          	lea    0x58(%rsi),%rcx
   18001ae5c:	ff 15 66 92 05 00    	call   *0x59266(%rip)        # 0x1800740c8
   18001ae62:	90                   	nop
   18001ae63:	c7 86 80 00 00 00 ff 	movl   $0xffffffff,0x80(%rsi)
   18001ae6a:	ff ff ff 
   18001ae6d:	89 9e 84 00 00 00    	mov    %ebx,0x84(%rsi)
   18001ae73:	4c 89 b6 98 01 00 00 	mov    %r14,0x198(%rsi)
   18001ae7a:	48 89 ae f8 01 00 00 	mov    %rbp,0x1f8(%rsi)
   18001ae81:	48 8d 8e 00 02 00 00 	lea    0x200(%rsi),%rcx
   18001ae88:	ff 15 3a 92 05 00    	call   *0x5923a(%rip)        # 0x1800740c8
   18001ae8e:	90                   	nop
   18001ae8f:	44 89 be 2c 02 00 00 	mov    %r15d,0x22c(%rsi)
   18001ae96:	44 88 be 3c 02 00 00 	mov    %r15b,0x23c(%rsi)
   18001ae9d:	8b 84 24 80 00 00 00 	mov    0x80(%rsp),%eax
```

## `KERNEL32.dll!InitializeCriticalSectionAndSpinCount` (3 Call Sites)

### Line 96899 (Address `0x1800741b8`)
```assembly
   180055021:	5b                   	pop    %rbx
   180055022:	c3                   	ret
   180055023:	cc                   	int3
   180055024:	e9 1b 9c 00 00       	jmp    0x18005ec44
   180055029:	cc                   	int3
   18005502a:	cc                   	int3
   18005502b:	cc                   	int3
   18005502c:	40 57                	rex push %rdi
   18005502e:	48 83 ec 30          	sub    $0x30,%rsp
   180055032:	48 c7 44 24 20 fe ff 	movq   $0xfffffffffffffffe,0x20(%rsp)
   180055039:	ff ff 
   18005503b:	48 89 5c 24 40       	mov    %rbx,0x40(%rsp)
   180055040:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180055045:	ba a0 0f 00 00       	mov    $0xfa0,%edx
   18005504a:	48 8d 0d 07 23 05 00 	lea    0x52307(%rip),%rcx        # 0x1800a7358
   180055051:	ff 15 61 f1 01 00    	call   *0x1f161(%rip)        # 0x1800741b8
   180055057:	90                   	nop
   180055058:	48 8d 0d b1 d1 03 00 	lea    0x3d1b1(%rip),%rcx        # 0x180092210
   18005505f:	ff 15 f3 ef 01 00    	call   *0x1eff3(%rip)        # 0x180074058
   180055065:	90                   	nop
```

### Line 101736 (Address `0x1800741b8`)
```assembly
   180059077:	41 8b f0             	mov    %r8d,%esi
   18005907a:	4c 8d 0d f7 95 03 00 	lea    0x395f7(%rip),%r9        # 0x180092678
   180059081:	8b da                	mov    %edx,%ebx
   180059083:	4c 8d 05 e6 95 03 00 	lea    0x395e6(%rip),%r8        # 0x180092670
   18005908a:	48 8b f9             	mov    %rcx,%rdi
   18005908d:	48 8d 15 e4 95 03 00 	lea    0x395e4(%rip),%rdx        # 0x180092678
   180059094:	b9 04 00 00 00       	mov    $0x4,%ecx
   180059099:	e8 c6 fc ff ff       	call   0x180058d64
   18005909e:	8b d3                	mov    %ebx,%edx
   1800590a0:	48 8b cf             	mov    %rdi,%rcx
   1800590a3:	48 85 c0             	test   %rax,%rax
   1800590a6:	74 0b                	je     0x1800590b3
   1800590a8:	44 8b c6             	mov    %esi,%r8d
   1800590ab:	ff 15 bf b2 01 00    	call   *0x1b2bf(%rip)        # 0x180074370
   1800590b1:	eb 06                	jmp    0x1800590b9
   1800590b3:	ff 15 ff b0 01 00    	call   *0x1b0ff(%rip)        # 0x1800741b8
   1800590b9:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   1800590be:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   1800590c3:	48 83 c4 20          	add    $0x20,%rsp
   1800590c7:	5f                   	pop    %rdi
```

### Line 122500 (Address `0x1800741b8`)
```assembly
   18006a5e7:	41 8b f0             	mov    %r8d,%esi
   18006a5ea:	4c 8d 0d 47 b3 02 00 	lea    0x2b347(%rip),%r9        # 0x180095938
   18006a5f1:	8b da                	mov    %edx,%ebx
   18006a5f3:	4c 8d 05 36 b3 02 00 	lea    0x2b336(%rip),%r8        # 0x180095930
   18006a5fa:	48 8b f9             	mov    %rcx,%rdi
   18006a5fd:	48 8d 15 34 b3 02 00 	lea    0x2b334(%rip),%rdx        # 0x180095938
   18006a604:	b9 12 00 00 00       	mov    $0x12,%ecx
   18006a609:	e8 be fa ff ff       	call   0x18006a0cc
   18006a60e:	8b d3                	mov    %ebx,%edx
   18006a610:	48 8b cf             	mov    %rdi,%rcx
   18006a613:	48 85 c0             	test   %rax,%rax
   18006a616:	74 0b                	je     0x18006a623
   18006a618:	44 8b c6             	mov    %esi,%r8d
   18006a61b:	ff 15 4f 9d 00 00    	call   *0x9d4f(%rip)        # 0x180074370
   18006a621:	eb 06                	jmp    0x18006a629
   18006a623:	ff 15 8f 9b 00 00    	call   *0x9b8f(%rip)        # 0x1800741b8
   18006a629:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18006a62e:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   18006a633:	48 83 c4 20          	add    $0x20,%rsp
   18006a637:	5f                   	pop    %rdi
```

## `KERNEL32.dll!InitializeCriticalSectionEx` (1 Call Sites)

### Line 29544 (Address `0x180074138`)
```assembly
   18001adad:	48 83 c4 60          	add    $0x60,%rsp
   18001adb1:	41 5f                	pop    %r15
   18001adb3:	5f                   	pop    %rdi
   18001adb4:	5e                   	pop    %rsi
   18001adb5:	c3                   	ret
   18001adb6:	cc                   	int3
   18001adb7:	cc                   	int3
   18001adb8:	cc                   	int3
   18001adb9:	cc                   	int3
   18001adba:	cc                   	int3
   18001adbb:	cc                   	int3
   18001adbc:	cc                   	int3
   18001adbd:	cc                   	int3
   18001adbe:	cc                   	int3
   18001adbf:	cc                   	int3
   18001adc0:	48 ff 25 71 93 05 00 	rex.W jmp *0x59371(%rip)        # 0x180074138
   18001adc7:	cc                   	int3
   18001adc8:	cc                   	int3
   18001adc9:	cc                   	int3
   18001adca:	cc                   	int3
```

## `KERNEL32.dll!InitializeSListHead` (1 Call Sites)

### Line 97695 (Address `0x180074218`)
```assembly
   180055b1a:	2b 00 00 
   180055b1d:	48 3b c3             	cmp    %rbx,%rax
   180055b20:	48 0f 44 c1          	cmove  %rcx,%rax
   180055b24:	48 89 05 35 08 05 00 	mov    %rax,0x50835(%rip)        # 0x1800a6360
   180055b2b:	48 8b 5c 24 48       	mov    0x48(%rsp),%rbx
   180055b30:	48 f7 d0             	not    %rax
   180055b33:	48 89 05 1e 08 05 00 	mov    %rax,0x5081e(%rip)        # 0x1800a6358
   180055b3a:	48 83 c4 20          	add    $0x20,%rsp
   180055b3e:	5d                   	pop    %rbp
   180055b3f:	c3                   	ret
   180055b40:	b8 01 00 00 00       	mov    $0x1,%eax
   180055b45:	c3                   	ret
   180055b46:	cc                   	int3
   180055b47:	cc                   	int3
   180055b48:	48 8d 0d 11 1e 05 00 	lea    0x51e11(%rip),%rcx        # 0x1800a7960
   180055b4f:	48 ff 25 c2 e6 01 00 	rex.W jmp *0x1e6c2(%rip)        # 0x180074218
   180055b56:	cc                   	int3
   180055b57:	cc                   	int3
   180055b58:	48 8d 0d 01 1e 05 00 	lea    0x51e01(%rip),%rcx        # 0x1800a7960
   180055b5f:	e9 f4 17 00 00       	jmp    0x180057358
```

## `KERNEL32.dll!InterlockedFlushSList` (1 Call Sites)

### Line 99551 (Address `0x180074238`)
```assembly
   18005733d:	48 2b d0             	sub    %rax,%rdx
   180057340:	8a 08                	mov    (%rax),%cl
   180057342:	3a 0c 10             	cmp    (%rax,%rdx,1),%cl
   180057345:	75 0a                	jne    0x180057351
   180057347:	48 ff c0             	inc    %rax
   18005734a:	84 c9                	test   %cl,%cl
   18005734c:	75 f2                	jne    0x180057340
   18005734e:	33 c0                	xor    %eax,%eax
   180057350:	c3                   	ret
   180057351:	1b c0                	sbb    %eax,%eax
   180057353:	83 c8 01             	or     $0x1,%eax
   180057356:	c3                   	ret
   180057357:	cc                   	int3
   180057358:	40 53                	rex push %rbx
   18005735a:	48 83 ec 20          	sub    $0x20,%rsp
   18005735e:	ff 15 d4 ce 01 00    	call   *0x1ced4(%rip)        # 0x180074238
   180057364:	48 85 c0             	test   %rax,%rax
   180057367:	74 13                	je     0x18005737c
   180057369:	48 8b 18             	mov    (%rax),%rbx
   18005736c:	48 8b c8             	mov    %rax,%rcx
```

## `KERNEL32.dll!IsDebuggerPresent` (4 Call Sites)

### Line 97766 (Address `0x180074220`)
```assembly
   180055c39:	48 8b 85 c8 04 00 00 	mov    0x4c8(%rbp),%rax
   180055c40:	48 8d 4c 24 50       	lea    0x50(%rsp),%rcx
   180055c45:	48 89 85 e8 00 00 00 	mov    %rax,0xe8(%rbp)
   180055c4c:	33 d2                	xor    %edx,%edx
   180055c4e:	48 8d 85 c8 04 00 00 	lea    0x4c8(%rbp),%rax
   180055c55:	41 b8 98 00 00 00    	mov    $0x98,%r8d
   180055c5b:	48 83 c0 08          	add    $0x8,%rax
   180055c5f:	48 89 85 88 00 00 00 	mov    %rax,0x88(%rbp)
   180055c66:	e8 c5 11 00 00       	call   0x180056e30
   180055c6b:	48 8b 85 c8 04 00 00 	mov    0x4c8(%rbp),%rax
   180055c72:	48 89 44 24 60       	mov    %rax,0x60(%rsp)
   180055c77:	c7 44 24 50 15 00 00 	movl   $0x40000015,0x50(%rsp)
   180055c7e:	40 
   180055c7f:	c7 44 24 54 01 00 00 	movl   $0x1,0x54(%rsp)
   180055c86:	00 
   180055c87:	ff 15 93 e5 01 00    	call   *0x1e593(%rip)        # 0x180074220
   180055c8d:	83 f8 01             	cmp    $0x1,%eax
   180055c90:	48 8d 44 24 50       	lea    0x50(%rsp),%rax
   180055c95:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   180055c9a:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
```

### Line 98061 (Address `0x180074220`)
```assembly
   18005603c:	48 89 47 08          	mov    %rax,0x8(%rdi)
   180056040:	48 8d 05 59 c3 03 00 	lea    0x3c359(%rip),%rax        # 0x1800923a0
   180056047:	48 89 47 20          	mov    %rax,0x20(%rdi)
   18005604b:	c7 07 60 00 00 00    	movl   $0x60,(%rdi)
   180056051:	c7 47 18 00 0e 00 00 	movl   $0xe00,0x18(%rdi)
   180056058:	e8 63 4d fc ff       	call   0x18001adc0
   18005605d:	85 c0                	test   %eax,%eax
   18005605f:	75 36                	jne    0x180056097
   180056061:	ff 15 a1 e0 01 00    	call   *0x1e0a1(%rip)        # 0x180074108
   180056067:	0f b7 c8             	movzwl %ax,%ecx
   18005606a:	81 c9 00 00 07 80    	or     $0x80070000,%ecx
   180056070:	85 c0                	test   %eax,%eax
   180056072:	0f 4e c8             	cmovle %eax,%ecx
   180056075:	85 c9                	test   %ecx,%ecx
   180056077:	79 1e                	jns    0x180056097
   180056079:	ff 15 a1 e1 01 00    	call   *0x1e1a1(%rip)        # 0x180074220
   18005607f:	85 c0                	test   %eax,%eax
   180056081:	74 0d                	je     0x180056090
   180056083:	48 8d 0d 26 c3 03 00 	lea    0x3c326(%rip),%rcx        # 0x1800923b0
   18005608a:	ff 15 d0 df 01 00    	call   *0x1dfd0(%rip)        # 0x180074060
```

### Line 107423 (Address `0x180074220`)
```assembly
   18005dc87:	48 8d 4c 24 60       	lea    0x60(%rsp),%rcx
   18005dc8c:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   18005dc91:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc95:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   18005dc9a:	33 c9                	xor    %ecx,%ecx
   18005dc9c:	ff 15 3e 65 01 00    	call   *0x1653e(%rip)        # 0x1800741e0
   18005dca2:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dca9:	48 89 85 08 01 00 00 	mov    %rax,0x108(%rbp)
   18005dcb0:	48 8d 85 08 05 00 00 	lea    0x508(%rbp),%rax
   18005dcb7:	48 83 c0 08          	add    $0x8,%rax
   18005dcbb:	89 74 24 70          	mov    %esi,0x70(%rsp)
   18005dcbf:	48 89 85 a8 00 00 00 	mov    %rax,0xa8(%rbp)
   18005dcc6:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dccd:	48 89 45 80          	mov    %rax,-0x80(%rbp)
   18005dcd1:	89 7c 24 74          	mov    %edi,0x74(%rsp)
   18005dcd5:	ff 15 45 65 01 00    	call   *0x16545(%rip)        # 0x180074220
   18005dcdb:	33 c9                	xor    %ecx,%ecx
   18005dcdd:	8b f8                	mov    %eax,%edi
   18005dcdf:	ff 15 0b 65 01 00    	call   *0x1650b(%rip)        # 0x1800741f0
   18005dce5:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
```

### Line 120935 (Address `0x180074220`)
```assembly
   1800690b9:	49 8b 5b 18          	mov    0x18(%r11),%rbx
   1800690bd:	49 8b 7b 20          	mov    0x20(%r11),%rdi
   1800690c1:	49 8b e3             	mov    %r11,%rsp
   1800690c4:	5d                   	pop    %rbp
   1800690c5:	c3                   	ret
   1800690c6:	cc                   	int3
   1800690c7:	cc                   	int3
   1800690c8:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   1800690cd:	48 89 6c 24 10       	mov    %rbp,0x10(%rsp)
   1800690d2:	48 89 74 24 18       	mov    %rsi,0x18(%rsp)
   1800690d7:	57                   	push   %rdi
   1800690d8:	48 83 ec 20          	sub    $0x20,%rsp
   1800690dc:	41 8b f8             	mov    %r8d,%edi
   1800690df:	48 8b ea             	mov    %rdx,%rbp
   1800690e2:	48 8b d9             	mov    %rcx,%rbx
   1800690e5:	ff 15 35 b1 00 00    	call   *0xb135(%rip)        # 0x180074220
   1800690eb:	85 c0                	test   %eax,%eax
   1800690ed:	40 0f 95 c6          	setne  %sil
   1800690f1:	85 c0                	test   %eax,%eax
   1800690f3:	74 1f                	je     0x180069114
```

## `KERNEL32.dll!IsProcessorFeaturePresent` (3 Call Sites)

### Line 107529 (Address `0x180074200`)
```assembly
   18005de0e:	45 33 c9             	xor    %r9d,%r9d
   18005de11:	45 33 c0             	xor    %r8d,%r8d
   18005de14:	33 d2                	xor    %edx,%edx
   18005de16:	33 c9                	xor    %ecx,%ecx
   18005de18:	e8 17 ff ff ff       	call   0x18005dd34
   18005de1d:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   18005de23:	45 33 c9             	xor    %r9d,%r9d
   18005de26:	45 33 c0             	xor    %r8d,%r8d
   18005de29:	33 d2                	xor    %edx,%edx
   18005de2b:	33 c9                	xor    %ecx,%ecx
   18005de2d:	e8 02 00 00 00       	call   0x18005de34
   18005de32:	cc                   	int3
   18005de33:	cc                   	int3
   18005de34:	48 83 ec 28          	sub    $0x28,%rsp
   18005de38:	b9 17 00 00 00       	mov    $0x17,%ecx
   18005de3d:	ff 15 bd 63 01 00    	call   *0x163bd(%rip)        # 0x180074200
   18005de43:	85 c0                	test   %eax,%eax
   18005de45:	74 07                	je     0x18005de4e
   18005de47:	b9 05 00 00 00       	mov    $0x5,%ecx
   18005de4c:	cd 29                	int    $0x29
```

### Line 117667 (Address `0x180074200`)
```assembly
   18006655f:	48 83 c4 20          	add    $0x20,%rsp
   180066563:	5f                   	pop    %rdi
   180066564:	c3                   	ret
   180066565:	cc                   	int3
   180066566:	cc                   	int3
   180066567:	cc                   	int3
   180066568:	48 83 ec 28          	sub    $0x28,%rsp
   18006656c:	e8 ff 2d 00 00       	call   0x180069370
   180066571:	48 85 c0             	test   %rax,%rax
   180066574:	74 0a                	je     0x180066580
   180066576:	b9 16 00 00 00       	mov    $0x16,%ecx
   18006657b:	e8 40 2e 00 00       	call   0x1800693c0
   180066580:	f6 05 21 ff 03 00 02 	testb  $0x2,0x3ff21(%rip)        # 0x1800a64a8
   180066587:	74 2a                	je     0x1800665b3
   180066589:	b9 17 00 00 00       	mov    $0x17,%ecx
   18006658e:	ff 15 6c dc 00 00    	call   *0xdc6c(%rip)        # 0x180074200
   180066594:	85 c0                	test   %eax,%eax
   180066596:	74 07                	je     0x18006659f
   180066598:	b9 07 00 00 00       	mov    $0x7,%ecx
   18006659d:	cd 29                	int    $0x29
```

### Line 131615 (Address `0x180074200`)
```assembly
   180072356:	48 83 ec 20          	sub    $0x20,%rsp
   18007235a:	48 8b d9             	mov    %rcx,%rbx
   18007235d:	e8 9e fb ff ff       	call   0x180071f00
   180072362:	83 e3 3f             	and    $0x3f,%ebx
   180072365:	0b c3                	or     %ebx,%eax
   180072367:	8b c8                	mov    %eax,%ecx
   180072369:	48 83 c4 20          	add    $0x20,%rsp
   18007236d:	5b                   	pop    %rbx
   18007236e:	e9 9d fb ff ff       	jmp    0x180071f10
   180072373:	cc                   	int3
   180072374:	48 83 ec 28          	sub    $0x28,%rsp
   180072378:	e8 83 fb ff ff       	call   0x180071f00
   18007237d:	83 e0 3f             	and    $0x3f,%eax
   180072380:	48 83 c4 28          	add    $0x28,%rsp
   180072384:	c3                   	ret
   180072385:	ff 25 75 1e 00 00    	jmp    *0x1e75(%rip)        # 0x180074200
   18007238b:	ff 25 9f 1e 00 00    	jmp    *0x1e9f(%rip)        # 0x180074230
   180072391:	cc                   	int3
   180072392:	cc                   	int3
   180072393:	cc                   	int3
```

## `KERNEL32.dll!IsValidCodePage` (1 Call Sites)

### Line 125473 (Address `0x1800741a0`)
```assembly
   18006ceef:	85 c0                	test   %eax,%eax
   18006cef1:	0f 84 53 02 00 00    	je     0x18006d14a
   18006cef7:	4c 8d 2d a2 9a 03 00 	lea    0x39aa2(%rip),%r13        # 0x1800a69a0
   18006cefe:	44 8b f3             	mov    %ebx,%r14d
   18006cf01:	49 8b c5             	mov    %r13,%rax
   18006cf04:	8d 6b 01             	lea    0x1(%rbx),%ebp
   18006cf07:	39 38                	cmp    %edi,(%rax)
   18006cf09:	0f 84 4e 01 00 00    	je     0x18006d05d
   18006cf0f:	44 03 f5             	add    %ebp,%r14d
   18006cf12:	48 83 c0 30          	add    $0x30,%rax
   18006cf16:	41 83 fe 05          	cmp    $0x5,%r14d
   18006cf1a:	72 eb                	jb     0x18006cf07
   18006cf1c:	81 ff e8 fd 00 00    	cmp    $0xfde8,%edi
   18006cf22:	0f 84 2d 01 00 00    	je     0x18006d055
   18006cf28:	0f b7 cf             	movzwl %di,%ecx
   18006cf2b:	ff 15 6f 72 00 00    	call   *0x726f(%rip)        # 0x1800741a0
   18006cf31:	85 c0                	test   %eax,%eax
   18006cf33:	0f 84 1c 01 00 00    	je     0x18006d055
   18006cf39:	b8 e9 fd 00 00       	mov    $0xfde9,%eax
   18006cf3e:	3b f8                	cmp    %eax,%edi
```

## `KERNEL32.dll!LCMapStringW` (1 Call Sites)

### Line 122557 (Address `0x1800741b0`)
```assembly
   18006a6c6:	48 8b cd             	mov    %rbp,%rcx
   18006a6c9:	ff 15 a1 9c 00 00    	call   *0x9ca1(%rip)        # 0x180074370
   18006a6cf:	eb 32                	jmp    0x18006a703
   18006a6d1:	33 d2                	xor    %edx,%edx
   18006a6d3:	48 8b cd             	mov    %rbp,%rcx
   18006a6d6:	e8 3d 00 00 00       	call   0x18006a718
   18006a6db:	8b c8                	mov    %eax,%ecx
   18006a6dd:	44 8b cb             	mov    %ebx,%r9d
   18006a6e0:	8b 84 24 88 00 00 00 	mov    0x88(%rsp),%eax
   18006a6e7:	4c 8b c7             	mov    %rdi,%r8
   18006a6ea:	89 44 24 28          	mov    %eax,0x28(%rsp)
   18006a6ee:	8b d6                	mov    %esi,%edx
   18006a6f0:	48 8b 84 24 80 00 00 	mov    0x80(%rsp),%rax
   18006a6f7:	00 
   18006a6f8:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18006a6fd:	ff 15 ad 9a 00 00    	call   *0x9aad(%rip)        # 0x1800741b0
   18006a703:	48 8b 5c 24 60       	mov    0x60(%rsp),%rbx
   18006a708:	48 8b 6c 24 68       	mov    0x68(%rsp),%rbp
   18006a70d:	48 8b 74 24 70       	mov    0x70(%rsp),%rsi
   18006a712:	48 83 c4 50          	add    $0x50,%rsp
```

## `KERNEL32.dll!LeaveCriticalSection` (4 Call Sites)

### Line 28951 (Address `0x1800740c0`)
```assembly
   18001a594:	48 89 03             	mov    %rax,(%rbx)
   18001a597:	48 83 c4 20          	add    $0x20,%rsp
   18001a59b:	5b                   	pop    %rbx
   18001a59c:	c3                   	ret
   18001a59d:	cc                   	int3
   18001a59e:	cc                   	int3
   18001a59f:	cc                   	int3
   18001a5a0:	48 83 c1 08          	add    $0x8,%rcx
   18001a5a4:	48 ff 25 0d 9b 05 00 	rex.W jmp *0x59b0d(%rip)        # 0x1800740b8
   18001a5ab:	cc                   	int3
   18001a5ac:	cc                   	int3
   18001a5ad:	cc                   	int3
   18001a5ae:	cc                   	int3
   18001a5af:	cc                   	int3
   18001a5b0:	48 83 c1 08          	add    $0x8,%rcx
   18001a5b4:	48 ff 25 05 9b 05 00 	rex.W jmp *0x59b05(%rip)        # 0x1800740c0
   18001a5bb:	cc                   	int3
   18001a5bc:	cc                   	int3
   18001a5bd:	cc                   	int3
   18001a5be:	cc                   	int3
```

### Line 109674 (Address `0x1800740c0`)
```assembly
   18005faf7:	48 83 c3 08          	add    $0x8,%rbx
   18005fafb:	48 83 fb 18          	cmp    $0x18,%rbx
   18005faff:	75 d1                	jne    0x18005fad2
   18005fb01:	48 8b 0d 80 80 04 00 	mov    0x48080(%rip),%rcx        # 0x1800a7b88
   18005fb08:	e8 af 6d 00 00       	call   0x1800668bc
   18005fb0d:	48 83 25 73 80 04 00 	andq   $0x0,0x48073(%rip)        # 0x1800a7b88
   18005fb14:	00 
   18005fb15:	48 83 c4 20          	add    $0x20,%rsp
   18005fb19:	5b                   	pop    %rbx
   18005fb1a:	c3                   	ret
   18005fb1b:	cc                   	int3
   18005fb1c:	48 83 c1 30          	add    $0x30,%rcx
   18005fb20:	48 ff 25 91 45 01 00 	rex.W jmp *0x14591(%rip)        # 0x1800740b8
   18005fb27:	cc                   	int3
   18005fb28:	48 83 c1 30          	add    $0x30,%rcx
   18005fb2c:	48 ff 25 8d 45 01 00 	rex.W jmp *0x1458d(%rip)        # 0x1800740c0
   18005fb33:	cc                   	int3
   18005fb34:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18005fb39:	57                   	push   %rdi
   18005fb3a:	48 83 ec 40          	sub    $0x40,%rsp
```

### Line 121485 (Address `0x1800740c0`)
```assembly
   180069813:	48 8d 0c 9b          	lea    (%rbx,%rbx,4),%rcx
   180069817:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   18006981b:	ff 15 af a8 00 00    	call   *0xa8af(%rip)        # 0x1800740d0
   180069821:	ff 0d 69 eb 03 00    	decl   0x3eb69(%rip)        # 0x1800a8390
   180069827:	85 db                	test   %ebx,%ebx
   180069829:	75 df                	jne    0x18006980a
   18006982b:	b0 01                	mov    $0x1,%al
   18006982d:	48 83 c4 20          	add    $0x20,%rsp
   180069831:	5b                   	pop    %rbx
   180069832:	c3                   	ret
   180069833:	cc                   	int3
   180069834:	48 63 c1             	movslq %ecx,%rax
   180069837:	48 8d 0c 80          	lea    (%rax,%rax,4),%rcx
   18006983b:	48 8d 05 1e e9 03 00 	lea    0x3e91e(%rip),%rax        # 0x1800a8160
   180069842:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   180069846:	48 ff 25 73 a8 00 00 	rex.W jmp *0xa873(%rip)        # 0x1800740c0
   18006984d:	cc                   	int3
   18006984e:	cc                   	int3
   18006984f:	cc                   	int3
   180069850:	48 89 5c 24 18       	mov    %rbx,0x18(%rsp)
```

### Line 128443 (Address `0x1800740c0`)
```assembly
   18006f8e5:	83 e2 3f             	and    $0x3f,%edx
   18006f8e8:	48 c1 f8 06          	sar    $0x6,%rax
   18006f8ec:	48 8d 0c d2          	lea    (%rdx,%rdx,8),%rcx
   18006f8f0:	49 8b 04 c0          	mov    (%r8,%rax,8),%rax
   18006f8f4:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   18006f8f8:	48 ff 25 b9 47 00 00 	rex.W jmp *0x47b9(%rip)        # 0x1800740b8
   18006f8ff:	cc                   	int3
   18006f900:	48 63 d1             	movslq %ecx,%rdx
   18006f903:	4c 8d 05 26 84 03 00 	lea    0x38426(%rip),%r8        # 0x1800a7d30
   18006f90a:	48 8b c2             	mov    %rdx,%rax
   18006f90d:	83 e2 3f             	and    $0x3f,%edx
   18006f910:	48 c1 f8 06          	sar    $0x6,%rax
   18006f914:	48 8d 0c d2          	lea    (%rdx,%rdx,8),%rcx
   18006f918:	49 8b 04 c0          	mov    (%r8,%rax,8),%rax
   18006f91c:	48 8d 0c c8          	lea    (%rax,%rcx,8),%rcx
   18006f920:	48 ff 25 99 47 00 00 	rex.W jmp *0x4799(%rip)        # 0x1800740c0
   18006f927:	cc                   	int3
   18006f928:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18006f92d:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
   18006f932:	48 89 7c 24 18       	mov    %rdi,0x18(%rsp)
```

## `KERNEL32.dll!LoadLibraryExW` (4 Call Sites)

### Line 101544 (Address `0x180074280`)
```assembly
   180058dcd:	4d 3b c4             	cmp    %r12,%r8
   180058dd0:	0f 84 d9 00 00 00    	je     0x180058eaf
   180058dd6:	8b 75 00             	mov    0x0(%rbp),%esi
   180058dd9:	49 8b 9c f6 b8 7a 0a 	mov    0xa7ab8(%r14,%rsi,8),%rbx
   180058de0:	00 
   180058de1:	48 85 db             	test   %rbx,%rbx
   180058de4:	74 0e                	je     0x180058df4
   180058de6:	48 3b df             	cmp    %rdi,%rbx
   180058de9:	0f 84 ac 00 00 00    	je     0x180058e9b
   180058def:	e9 a2 00 00 00       	jmp    0x180058e96
   180058df4:	4d 8b b4 f6 48 25 09 	mov    0x92548(%r14,%rsi,8),%r14
   180058dfb:	00 
   180058dfc:	33 d2                	xor    %edx,%edx
   180058dfe:	49 8b ce             	mov    %r14,%rcx
   180058e01:	41 b8 00 08 00 00    	mov    $0x800,%r8d
   180058e07:	ff 15 73 b4 01 00    	call   *0x1b473(%rip)        # 0x180074280
   180058e0d:	48 8b d8             	mov    %rax,%rbx
   180058e10:	48 85 c0             	test   %rax,%rax
   180058e13:	75 4f                	jne    0x180058e64
   180058e15:	ff 15 ed b2 01 00    	call   *0x1b2ed(%rip)        # 0x180074108
```

### Line 101567 (Address `0x180074280`)
```assembly
   180058e23:	49 8b ce             	mov    %r14,%rcx
   180058e26:	44 8b c3             	mov    %ebx,%r8d
   180058e29:	48 8d 15 c8 97 03 00 	lea    0x397c8(%rip),%rdx        # 0x1800925f8
   180058e30:	e8 f3 d7 00 00       	call   0x180066628
   180058e35:	85 c0                	test   %eax,%eax
   180058e37:	74 29                	je     0x180058e62
   180058e39:	44 8b c3             	mov    %ebx,%r8d
   180058e3c:	48 8d 15 c5 97 03 00 	lea    0x397c5(%rip),%rdx        # 0x180092608
   180058e43:	49 8b ce             	mov    %r14,%rcx
   180058e46:	e8 dd d7 00 00       	call   0x180066628
   180058e4b:	85 c0                	test   %eax,%eax
   180058e4d:	74 13                	je     0x180058e62
   180058e4f:	45 33 c0             	xor    %r8d,%r8d
   180058e52:	33 d2                	xor    %edx,%edx
   180058e54:	49 8b ce             	mov    %r14,%rcx
   180058e57:	ff 15 23 b4 01 00    	call   *0x1b423(%rip)        # 0x180074280
   180058e5d:	48 8b d8             	mov    %rax,%rbx
   180058e60:	eb 02                	jmp    0x180058e64
   180058e62:	33 db                	xor    %ebx,%ebx
   180058e64:	4c 8d 35 95 71 fa ff 	lea    -0x58e6b(%rip),%r14        # 0x180000000
```

### Line 122178 (Address `0x180074280`)
```assembly
   18006a135:	4d 3b c4             	cmp    %r12,%r8
   18006a138:	0f 84 d9 00 00 00    	je     0x18006a217
   18006a13e:	8b 75 00             	mov    0x0(%rbp),%esi
   18006a141:	49 8b 9c f6 a0 83 0a 	mov    0xa83a0(%r14,%rsi,8),%rbx
   18006a148:	00 
   18006a149:	48 85 db             	test   %rbx,%rbx
   18006a14c:	74 0e                	je     0x18006a15c
   18006a14e:	48 3b df             	cmp    %rdi,%rbx
   18006a151:	0f 84 ac 00 00 00    	je     0x18006a203
   18006a157:	e9 a2 00 00 00       	jmp    0x18006a1fe
   18006a15c:	4d 8b b4 f6 80 52 09 	mov    0x95280(%r14,%rsi,8),%r14
   18006a163:	00 
   18006a164:	33 d2                	xor    %edx,%edx
   18006a166:	49 8b ce             	mov    %r14,%rcx
   18006a169:	41 b8 00 08 00 00    	mov    $0x800,%r8d
   18006a16f:	ff 15 0b a1 00 00    	call   *0xa10b(%rip)        # 0x180074280
   18006a175:	48 8b d8             	mov    %rax,%rbx
   18006a178:	48 85 c0             	test   %rax,%rax
   18006a17b:	75 4f                	jne    0x18006a1cc
   18006a17d:	ff 15 85 9f 00 00    	call   *0x9f85(%rip)        # 0x180074108
```

### Line 122201 (Address `0x180074280`)
```assembly
   18006a18b:	49 8b ce             	mov    %r14,%rcx
   18006a18e:	44 8b c3             	mov    %ebx,%r8d
   18006a191:	48 8d 15 70 b6 02 00 	lea    0x2b670(%rip),%rdx        # 0x180095808
   18006a198:	e8 8b c4 ff ff       	call   0x180066628
   18006a19d:	85 c0                	test   %eax,%eax
   18006a19f:	74 29                	je     0x18006a1ca
   18006a1a1:	44 8b c3             	mov    %ebx,%r8d
   18006a1a4:	48 8d 15 6d b6 02 00 	lea    0x2b66d(%rip),%rdx        # 0x180095818
   18006a1ab:	49 8b ce             	mov    %r14,%rcx
   18006a1ae:	e8 75 c4 ff ff       	call   0x180066628
   18006a1b3:	85 c0                	test   %eax,%eax
   18006a1b5:	74 13                	je     0x18006a1ca
   18006a1b7:	45 33 c0             	xor    %r8d,%r8d
   18006a1ba:	33 d2                	xor    %edx,%edx
   18006a1bc:	49 8b ce             	mov    %r14,%rcx
   18006a1bf:	ff 15 bb a0 00 00    	call   *0xa0bb(%rip)        # 0x180074280
   18006a1c5:	48 8b d8             	mov    %rax,%rbx
   18006a1c8:	eb 02                	jmp    0x18006a1cc
   18006a1ca:	33 db                	xor    %ebx,%ebx
   18006a1cc:	4c 8d 35 2d 5e f9 ff 	lea    -0x6a1d3(%rip),%r14        # 0x180000000
```

## `KERNEL32.dll!MultiByteToWideChar` (3 Call Sites)

### Line 36681 (Address `0x180074158`)
```assembly
   18002177b:	0f b7 05 3e c9 07 00 	movzwl 0x7c93e(%rip),%eax        # 0x18009e0c0
   180021782:	66 89 01             	mov    %ax,(%rcx)
   180021785:	83 fb 0f             	cmp    $0xf,%ebx
   180021788:	0f 85 9e 00 00 00    	jne    0x18002182c
   18002178e:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   180021793:	49 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%r9
   18002179a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
   1800217a0:	49 ff c1             	inc    %r9
   1800217a3:	46 38 34 08          	cmp    %r14b,(%rax,%r9,1)
   1800217a7:	75 f7                	jne    0x1800217a0
   1800217a9:	44 89 74 24 28       	mov    %r14d,0x28(%rsp)
   1800217ae:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
   1800217b3:	33 d2                	xor    %edx,%edx
   1800217b5:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
   1800217ba:	33 c9                	xor    %ecx,%ecx
   1800217bc:	ff 15 96 29 05 00    	call   *0x52996(%rip)        # 0x180074158
   1800217c2:	48 63 d8             	movslq %eax,%rbx
   1800217c5:	49 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%r9
   1800217cc:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   1800217d1:	49 ff c1             	inc    %r9
```

### Line 36695 (Address `0x180074158`)
```assembly
   1800217ba:	33 c9                	xor    %ecx,%ecx
   1800217bc:	ff 15 96 29 05 00    	call   *0x52996(%rip)        # 0x180074158
   1800217c2:	48 63 d8             	movslq %eax,%rbx
   1800217c5:	49 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%r9
   1800217cc:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   1800217d1:	49 ff c1             	inc    %r9
   1800217d4:	46 38 34 08          	cmp    %r14b,(%rax,%r9,1)
   1800217d8:	75 f7                	jne    0x1800217d1
   1800217da:	48 8d 84 24 30 01 00 	lea    0x130(%rsp),%rax
   1800217e1:	00 
   1800217e2:	89 5c 24 28          	mov    %ebx,0x28(%rsp)
   1800217e6:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
   1800217eb:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800217f0:	33 d2                	xor    %edx,%edx
   1800217f2:	33 c9                	xor    %ecx,%ecx
   1800217f4:	ff 15 5e 29 05 00    	call   *0x5295e(%rip)        # 0x180074158
   1800217fa:	48 8b c3             	mov    %rbx,%rax
   1800217fd:	48 03 c0             	add    %rax,%rax
   180021800:	48 3d 00 02 00 00    	cmp    $0x200,%rax
   180021806:	73 5e                	jae    0x180021866
```

### Line 121389 (Address `0x180074158`)
```assembly
   1800696c3:	83 f9 2a             	cmp    $0x2a,%ecx
   1800696c6:	75 2f                	jne    0x1800696f7
   1800696c8:	33 d2                	xor    %edx,%edx
   1800696ca:	eb 2b                	jmp    0x1800696f7
   1800696cc:	81 f9 98 d6 00 00    	cmp    $0xd698,%ecx
   1800696d2:	74 20                	je     0x1800696f4
   1800696d4:	81 f9 a9 de 00 00    	cmp    $0xdea9,%ecx
   1800696da:	76 1b                	jbe    0x1800696f7
   1800696dc:	81 f9 b3 de 00 00    	cmp    $0xdeb3,%ecx
   1800696e2:	76 e4                	jbe    0x1800696c8
   1800696e4:	81 f9 e8 fd 00 00    	cmp    $0xfde8,%ecx
   1800696ea:	74 dc                	je     0x1800696c8
   1800696ec:	81 f9 e9 fd 00 00    	cmp    $0xfde9,%ecx
   1800696f2:	75 03                	jne    0x1800696f7
   1800696f4:	83 e2 08             	and    $0x8,%edx
   1800696f7:	48 ff 25 5a aa 00 00 	rex.W jmp *0xaa5a(%rip)        # 0x180074158
   1800696fe:	cc                   	int3
   1800696ff:	cc                   	int3
   180069700:	40 53                	rex push %rbx
   180069702:	8d 81 18 02 ff ff    	lea    -0xfde8(%rcx),%eax
```

## `KERNEL32.dll!OutputDebugStringW` (3 Call Sites)

### Line 26847 (Address `0x180074060`)
```assembly
   180018828:	41 54                	push   %r12
   18001882a:	41 55                	push   %r13
   18001882c:	41 56                	push   %r14
   18001882e:	41 57                	push   %r15
   180018830:	48 81 ec 80 01 00 00 	sub    $0x180,%rsp
   180018837:	48 8b 05 22 db 08 00 	mov    0x8db22(%rip),%rax        # 0x1800a6360
   18001883e:	48 33 c4             	xor    %rsp,%rax
   180018841:	48 89 84 24 70 01 00 	mov    %rax,0x170(%rsp)
   180018848:	00 
   180018849:	48 8b f1             	mov    %rcx,%rsi
   18001884c:	8b fa                	mov    %edx,%edi
   18001884e:	48 8d 0d 6b 25 08 00 	lea    0x8256b(%rip),%rcx        # 0x18009adc0
   180018855:	45 8b e1             	mov    %r9d,%r12d
   180018858:	4d 8b e8             	mov    %r8,%r13
   18001885b:	bb fa ff ff ff       	mov    $0xfffffffa,%ebx
   180018860:	ff 15 fa b7 05 00    	call   *0x5b7fa(%rip)        # 0x180074060
   180018866:	8b c7                	mov    %edi,%eax
   180018868:	25 00 ff ff ff       	and    $0xffffff00,%eax
   18001886d:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   180018872:	0f 85 4f 01 00 00    	jne    0x1800189c7
```

### Line 98065 (Address `0x180074060`)
```assembly
   180056051:	c7 47 18 00 0e 00 00 	movl   $0xe00,0x18(%rdi)
   180056058:	e8 63 4d fc ff       	call   0x18001adc0
   18005605d:	85 c0                	test   %eax,%eax
   18005605f:	75 36                	jne    0x180056097
   180056061:	ff 15 a1 e0 01 00    	call   *0x1e0a1(%rip)        # 0x180074108
   180056067:	0f b7 c8             	movzwl %ax,%ecx
   18005606a:	81 c9 00 00 07 80    	or     $0x80070000,%ecx
   180056070:	85 c0                	test   %eax,%eax
   180056072:	0f 4e c8             	cmovle %eax,%ecx
   180056075:	85 c9                	test   %ecx,%ecx
   180056077:	79 1e                	jns    0x180056097
   180056079:	ff 15 a1 e1 01 00    	call   *0x1e1a1(%rip)        # 0x180074220
   18005607f:	85 c0                	test   %eax,%eax
   180056081:	74 0d                	je     0x180056090
   180056083:	48 8d 0d 26 c3 03 00 	lea    0x3c326(%rip),%rcx        # 0x1800923b0
   18005608a:	ff 15 d0 df 01 00    	call   *0x1dfd0(%rip)        # 0x180074060
   180056090:	c6 05 c9 26 05 00 01 	movb   $0x1,0x526c9(%rip)        # 0x1800a8760
   180056097:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18005609c:	48 8b c7             	mov    %rdi,%rax
   18005609f:	48 83 c4 20          	add    $0x20,%rsp
```

### Line 120943 (Address `0x180074060`)
```assembly
   1800690cd:	48 89 6c 24 10       	mov    %rbp,0x10(%rsp)
   1800690d2:	48 89 74 24 18       	mov    %rsi,0x18(%rsp)
   1800690d7:	57                   	push   %rdi
   1800690d8:	48 83 ec 20          	sub    $0x20,%rsp
   1800690dc:	41 8b f8             	mov    %r8d,%edi
   1800690df:	48 8b ea             	mov    %rdx,%rbp
   1800690e2:	48 8b d9             	mov    %rcx,%rbx
   1800690e5:	ff 15 35 b1 00 00    	call   *0xb135(%rip)        # 0x180074220
   1800690eb:	85 c0                	test   %eax,%eax
   1800690ed:	40 0f 95 c6          	setne  %sil
   1800690f1:	85 c0                	test   %eax,%eax
   1800690f3:	74 1f                	je     0x180069114
   1800690f5:	48 85 db             	test   %rbx,%rbx
   1800690f8:	74 09                	je     0x180069103
   1800690fa:	48 8b cb             	mov    %rbx,%rcx
   1800690fd:	ff 15 5d af 00 00    	call   *0xaf5d(%rip)        # 0x180074060
   180069103:	e8 58 0f 00 00       	call   0x18006a060
   180069108:	83 f8 01             	cmp    $0x1,%eax
   18006910b:	74 07                	je     0x180069114
   18006910d:	b8 04 00 00 00       	mov    $0x4,%eax
```

## `KERNEL32.dll!QueryPerformanceCounter` (1 Call Sites)

### Line 97669 (Address `0x180074208`)
```assembly
   180055aaf:	2b 00 00 
   180055ab2:	48 3b c3             	cmp    %rbx,%rax
   180055ab5:	75 74                	jne    0x180055b2b
   180055ab7:	48 83 65 18 00       	andq   $0x0,0x18(%rbp)
   180055abc:	48 8d 4d 18          	lea    0x18(%rbp),%rcx
   180055ac0:	ff 15 4a e7 01 00    	call   *0x1e74a(%rip)        # 0x180074210
   180055ac6:	48 8b 45 18          	mov    0x18(%rbp),%rax
   180055aca:	48 89 45 10          	mov    %rax,0x10(%rbp)
   180055ace:	ff 15 04 e6 01 00    	call   *0x1e604(%rip)        # 0x1800740d8
   180055ad4:	8b c0                	mov    %eax,%eax
   180055ad6:	48 31 45 10          	xor    %rax,0x10(%rbp)
   180055ada:	ff 15 00 e6 01 00    	call   *0x1e600(%rip)        # 0x1800740e0
   180055ae0:	8b c0                	mov    %eax,%eax
   180055ae2:	48 8d 4d 20          	lea    0x20(%rbp),%rcx
   180055ae6:	48 31 45 10          	xor    %rax,0x10(%rbp)
   180055aea:	ff 15 18 e7 01 00    	call   *0x1e718(%rip)        # 0x180074208
   180055af0:	8b 45 20             	mov    0x20(%rbp),%eax
   180055af3:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   180055af7:	48 c1 e0 20          	shl    $0x20,%rax
   180055afb:	48 33 45 20          	xor    0x20(%rbp),%rax
```

## `KERNEL32.dll!RaiseException` (3 Call Sites)

### Line 99667 (Address `0x180074150`)
```assembly
   1800574ad:	48 89 5d f0          	mov    %rbx,-0x10(%rbp)
   1800574b1:	ff 15 89 cd 01 00    	call   *0x1cd89(%rip)        # 0x180074240
   1800574b7:	48 89 45 10          	mov    %rax,0x10(%rbp)
   1800574bb:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
   1800574bf:	48 85 db             	test   %rbx,%rbx
   1800574c2:	74 11                	je     0x1800574d5
   1800574c4:	f6 03 08             	testb  $0x8,(%rbx)
   1800574c7:	75 05                	jne    0x1800574ce
   1800574c9:	48 85 c0             	test   %rax,%rax
   1800574cc:	75 07                	jne    0x1800574d5
   1800574ce:	c7 45 e0 00 40 99 01 	movl   $0x1994000,-0x20(%rbp)
   1800574d5:	44 8b 45 d8          	mov    -0x28(%rbp),%r8d
   1800574d9:	4c 8d 4d e0          	lea    -0x20(%rbp),%r9
   1800574dd:	8b 55 c4             	mov    -0x3c(%rbp),%edx
   1800574e0:	8b 4d c0             	mov    -0x40(%rbp),%ecx
   1800574e3:	ff 15 67 cc 01 00    	call   *0x1cc67(%rip)        # 0x180074150
   1800574e9:	4c 8d 5c 24 60       	lea    0x60(%rsp),%r11
   1800574ee:	49 8b 5b 18          	mov    0x18(%r11),%rbx
   1800574f2:	49 8b 7b 20          	mov    0x20(%r11),%rdi
   1800574f6:	49 8b e3             	mov    %r11,%rsp
```

### Line 100997 (Address `0x180074150`)
```assembly
   180058703:	74 21                	je     0x180058726
   180058705:	b2 01                	mov    $0x1,%dl
   180058707:	48 8b ce             	mov    %rsi,%rcx
   18005870a:	e8 bd df ff ff       	call   0x1800566cc
   18005870f:	48 8b 84 24 c8 00 00 	mov    0xc8(%rsp),%rax
   180058716:	00 
   180058717:	4c 8d 48 20          	lea    0x20(%rax),%r9
   18005871b:	44 8b 40 18          	mov    0x18(%rax),%r8d
   18005871f:	8b 50 04             	mov    0x4(%rax),%edx
   180058722:	8b 08                	mov    (%rax),%ecx
   180058724:	eb 0d                	jmp    0x180058733
   180058726:	4c 8d 4e 20          	lea    0x20(%rsi),%r9
   18005872a:	44 8b 46 18          	mov    0x18(%rsi),%r8d
   18005872e:	8b 56 04             	mov    0x4(%rsi),%edx
   180058731:	8b 0e                	mov    (%rsi),%ecx
   180058733:	ff 15 17 ba 01 00    	call   *0x1ba17(%rip)        # 0x180074150
   180058739:	44 8b 7c 24 20       	mov    0x20(%rsp),%r15d
   18005873e:	48 8b 5c 24 28       	mov    0x28(%rsp),%rbx
   180058743:	4c 8b 6c 24 40       	mov    0x40(%rsp),%r13
   180058748:	48 8b bc 24 c0 00 00 	mov    0xc0(%rsp),%rdi
```

### Line 131479 (Address `0x180074150`)
```assembly
   1800721a4:	48 8b 45 10          	mov    0x10(%rbp),%rax
   1800721a8:	83 48 60 01          	orl    $0x1,0x60(%rax)
   1800721ac:	48 8b 55 10          	mov    0x10(%rbp),%rdx
   1800721b0:	8b 42 60             	mov    0x60(%rdx),%eax
   1800721b3:	41 23 c0             	and    %r8d,%eax
   1800721b6:	83 c8 02             	or     $0x2,%eax
   1800721b9:	89 42 60             	mov    %eax,0x60(%rdx)
   1800721bc:	48 8b 45 10          	mov    0x10(%rbp),%rax
   1800721c0:	48 8b 16             	mov    (%rsi),%rdx
   1800721c3:	48 89 50 50          	mov    %rdx,0x50(%rax)
   1800721c7:	e8 ec 00 00 00       	call   0x1800722b8
   1800721cc:	33 d2                	xor    %edx,%edx
   1800721ce:	4c 8d 4d 10          	lea    0x10(%rbp),%r9
   1800721d2:	8b cf                	mov    %edi,%ecx
   1800721d4:	44 8d 42 01          	lea    0x1(%rdx),%r8d
   1800721d8:	ff 15 72 1f 00 00    	call   *0x1f72(%rip)        # 0x180074150
   1800721de:	48 8b 4d 10          	mov    0x10(%rbp),%rcx
   1800721e2:	8b 41 08             	mov    0x8(%rcx),%eax
   1800721e5:	a8 10                	test   $0x10,%al
   1800721e7:	74 08                	je     0x1800721f1
```

## `KERNEL32.dll!ReadFile` (1 Call Sites)

### Line 29230 (Address `0x1800740e8`)
```assembly
   18001a8ed:	cc                   	int3
   18001a8ee:	cc                   	int3
   18001a8ef:	cc                   	int3
   18001a8f0:	4c 8b dc             	mov    %rsp,%r11
   18001a8f3:	48 81 ec 98 00 00 00 	sub    $0x98,%rsp
   18001a8fa:	49 c7 43 98 fe ff ff 	movq   $0xfffffffffffffffe,-0x68(%r11)
   18001a901:	ff 
   18001a902:	41 8b c0             	mov    %r8d,%eax
   18001a905:	4c 3b c0             	cmp    %rax,%r8
   18001a908:	75 74                	jne    0x18001a97e
   18001a90a:	33 c0                	xor    %eax,%eax
   18001a90c:	41 89 43 18          	mov    %eax,0x18(%r11)
   18001a910:	49 89 43 88          	mov    %rax,-0x78(%r11)
   18001a914:	4d 8d 4b 18          	lea    0x18(%r11),%r9
   18001a918:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   18001a91c:	ff 15 c6 97 05 00    	call   *0x597c6(%rip)        # 0x1800740e8
   18001a922:	85 c0                	test   %eax,%eax
   18001a924:	75 0d                	jne    0x18001a933
   18001a926:	ff 15 dc 97 05 00    	call   *0x597dc(%rip)        # 0x180074108
   18001a92c:	83 f8 26             	cmp    $0x26,%eax
```

## `KERNEL32.dll!ResumeThread` (3 Call Sites)

### Line 23097 (Address `0x180074078`)
```assembly
   1800153d4:	49 8b 06             	mov    (%r14),%rax
   1800153d7:	49 8b ce             	mov    %r14,%rcx
   1800153da:	ff 50 08             	call   *0x8(%rax)
   1800153dd:	48 81 c3 7c 02 00 00 	add    $0x27c,%rbx
   1800153e4:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
   1800153e9:	be 10 00 00 00       	mov    $0x10,%esi
   1800153ee:	66 90                	xchg   %ax,%ax
   1800153f0:	80 7b fc 00          	cmpb   $0x0,-0x4(%rbx)
   1800153f4:	74 2d                	je     0x180015423
   1800153f6:	44 8b 03             	mov    (%rbx),%r8d
   1800153f9:	48 8d 15 18 5a 08 00 	lea    0x85a18(%rip),%rdx        # 0x18009ae18
   180015400:	48 8b 0d 01 32 09 00 	mov    0x93201(%rip),%rcx        # 0x1800a8608
   180015407:	e8 84 0e 00 00       	call   0x180016290
   18001540c:	48 8b 7b 04          	mov    0x4(%rbx),%rdi
   180015410:	48 8b 4f 08          	mov    0x8(%rdi),%rcx
   180015414:	ff 15 5e ec 05 00    	call   *0x5ec5e(%rip)        # 0x180074078
   18001541a:	83 f8 ff             	cmp    $0xffffffff,%eax
   18001541d:	0f 95 c0             	setne  %al
   180015420:	88 47 14             	mov    %al,0x14(%rdi)
   180015423:	48 83 c3 18          	add    $0x18,%rbx
```

### Line 23526 (Address `0x180074078`)
```assembly
   180015aa1:	45 88 a6 d8 02 00 00 	mov    %r12b,0x2d8(%r14)
   180015aa8:	45 88 a6 f0 02 00 00 	mov    %r12b,0x2f0(%r14)
   180015aaf:	45 88 a6 08 03 00 00 	mov    %r12b,0x308(%r14)
   180015ab6:	45 88 a6 20 03 00 00 	mov    %r12b,0x320(%r14)
   180015abd:	45 88 a6 38 03 00 00 	mov    %r12b,0x338(%r14)
   180015ac4:	45 88 a6 50 03 00 00 	mov    %r12b,0x350(%r14)
   180015acb:	45 88 a6 68 03 00 00 	mov    %r12b,0x368(%r14)
   180015ad2:	45 88 a6 80 03 00 00 	mov    %r12b,0x380(%r14)
   180015ad9:	45 88 a6 98 03 00 00 	mov    %r12b,0x398(%r14)
   180015ae0:	45 88 a6 b0 03 00 00 	mov    %r12b,0x3b0(%r14)
   180015ae7:	45 88 a6 c8 03 00 00 	mov    %r12b,0x3c8(%r14)
   180015aee:	45 88 a6 e0 03 00 00 	mov    %r12b,0x3e0(%r14)
   180015af5:	49 8b 4e 08          	mov    0x8(%r14),%rcx
   180015af9:	48 89 05 18 2b 09 00 	mov    %rax,0x92b18(%rip)        # 0x1800a8618
   180015b00:	4c 89 35 e1 2a 09 00 	mov    %r14,0x92ae1(%rip)        # 0x1800a85e8
   180015b07:	ff 15 6b e5 05 00    	call   *0x5e56b(%rip)        # 0x180074078
   180015b0d:	48 8b 0d f4 2a 09 00 	mov    0x92af4(%rip),%rcx        # 0x1800a8608
   180015b14:	48 8d 15 b5 4d 08 00 	lea    0x84db5(%rip),%rdx        # 0x18009a8d0
   180015b1b:	83 f8 ff             	cmp    $0xffffffff,%eax
   180015b1e:	c7 05 d8 2a 09 00 01 	movl   $0x1,0x92ad8(%rip)        # 0x1800a8600
```

### Line 27354 (Address `0x180074078`)
```assembly
   180018f9b:	48 8b cb             	mov    %rbx,%rcx
   180018f9e:	e8 2d 1e 00 00       	call   0x18001add0
   180018fa3:	90                   	nop
   180018fa4:	4b 8d 0c 76          	lea    (%r14,%r14,2),%rcx
   180018fa8:	49 89 84 cd 80 02 00 	mov    %rax,0x280(%r13,%rcx,8)
   180018faf:	00 
   180018fb0:	41 8b 85 70 02 00 00 	mov    0x270(%r13),%eax
   180018fb7:	41 89 84 cd 7c 02 00 	mov    %eax,0x27c(%r13,%rcx,8)
   180018fbe:	00 
   180018fbf:	41 ff 85 70 02 00 00 	incl   0x270(%r13)
   180018fc6:	41 c6 84 cd 78 02 00 	movb   $0x1,0x278(%r13,%rcx,8)
   180018fcd:	00 01 
   180018fcf:	49 8b 9c cd 80 02 00 	mov    0x280(%r13,%rcx,8),%rbx
   180018fd6:	00 
   180018fd7:	48 8b 4b 08          	mov    0x8(%rbx),%rcx
   180018fdb:	ff 15 97 b0 05 00    	call   *0x5b097(%rip)        # 0x180074078
   180018fe1:	83 f8 ff             	cmp    $0xffffffff,%eax
   180018fe4:	0f 95 c0             	setne  %al
   180018fe7:	88 43 14             	mov    %al,0x14(%rbx)
   180018fea:	49 8b 85 10 02 00 00 	mov    0x210(%r13),%rax
```

## `KERNEL32.dll!RtlCaptureContext` (4 Call Sites)

### Line 97099 (Address `0x1800741d0`)
```assembly
   18005533f:	00 00 00 
   180055342:	b8 08 00 00 00       	mov    $0x8,%eax
   180055347:	48 6b c0 00          	imul   $0x0,%rax,%rax
   18005534b:	48 8d 0d 6e 20 05 00 	lea    0x5206e(%rip),%rcx        # 0x1800a73c0
   180055352:	8b 54 24 30          	mov    0x30(%rsp),%edx
   180055356:	48 89 14 01          	mov    %rdx,(%rcx,%rax,1)
   18005535a:	48 8d 0d 77 cf 03 00 	lea    0x3cf77(%rip),%rcx        # 0x1800922d8
   180055361:	e8 4e fe ff ff       	call   0x1800551b4
   180055366:	48 83 c4 28          	add    $0x28,%rsp
   18005536a:	c3                   	ret
   18005536b:	cc                   	int3
   18005536c:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180055371:	57                   	push   %rdi
   180055372:	48 83 ec 40          	sub    $0x40,%rsp
   180055376:	48 8b d9             	mov    %rcx,%rbx
   180055379:	ff 15 51 ee 01 00    	call   *0x1ee51(%rip)        # 0x1800741d0
   18005537f:	48 8b bb f8 00 00 00 	mov    0xf8(%rbx),%rdi
   180055386:	48 8d 54 24 50       	lea    0x50(%rsp),%rdx
   18005538b:	48 8b cf             	mov    %rdi,%rcx
   18005538e:	45 33 c0             	xor    %r8d,%r8d
```

### Line 97130 (Address `0x1800741d0`)
```assembly
   1800553c1:	33 c9                	xor    %ecx,%ecx
   1800553c3:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   1800553c8:	ff 15 12 ee 01 00    	call   *0x1ee12(%rip)        # 0x1800741e0
   1800553ce:	48 8b 5c 24 68       	mov    0x68(%rsp),%rbx
   1800553d3:	48 83 c4 40          	add    $0x40,%rsp
   1800553d7:	5f                   	pop    %rdi
   1800553d8:	c3                   	ret
   1800553d9:	cc                   	int3
   1800553da:	cc                   	int3
   1800553db:	cc                   	int3
   1800553dc:	40 53                	rex push %rbx
   1800553de:	56                   	push   %rsi
   1800553df:	57                   	push   %rdi
   1800553e0:	48 83 ec 40          	sub    $0x40,%rsp
   1800553e4:	48 8b d9             	mov    %rcx,%rbx
   1800553e7:	ff 15 e3 ed 01 00    	call   *0x1ede3(%rip)        # 0x1800741d0
   1800553ed:	48 8b b3 f8 00 00 00 	mov    0xf8(%rbx),%rsi
   1800553f4:	33 ff                	xor    %edi,%edi
   1800553f6:	45 33 c0             	xor    %r8d,%r8d
   1800553f9:	48 8d 54 24 60       	lea    0x60(%rsp),%rdx
```

### Line 97731 (Address `0x1800741d0`)
```assembly
   180055b9e:	48 81 ec c0 05 00 00 	sub    $0x5c0,%rsp
   180055ba5:	8b d9                	mov    %ecx,%ebx
   180055ba7:	b9 17 00 00 00       	mov    $0x17,%ecx
   180055bac:	e8 d4 c7 01 00       	call   0x180072385
   180055bb1:	85 c0                	test   %eax,%eax
   180055bb3:	74 04                	je     0x180055bb9
   180055bb5:	8b cb                	mov    %ebx,%ecx
   180055bb7:	cd 29                	int    $0x29
   180055bb9:	b9 03 00 00 00       	mov    $0x3,%ecx
   180055bbe:	e8 c5 ff ff ff       	call   0x180055b88
   180055bc3:	33 d2                	xor    %edx,%edx
   180055bc5:	48 8d 4d f0          	lea    -0x10(%rbp),%rcx
   180055bc9:	41 b8 d0 04 00 00    	mov    $0x4d0,%r8d
   180055bcf:	e8 5c 12 00 00       	call   0x180056e30
   180055bd4:	48 8d 4d f0          	lea    -0x10(%rbp),%rcx
   180055bd8:	ff 15 f2 e5 01 00    	call   *0x1e5f2(%rip)        # 0x1800741d0
   180055bde:	48 8b 9d e8 00 00 00 	mov    0xe8(%rbp),%rbx
   180055be5:	48 8d 95 d8 04 00 00 	lea    0x4d8(%rbp),%rdx
   180055bec:	48 8b cb             	mov    %rbx,%rcx
   180055bef:	45 33 c0             	xor    %r8d,%r8d
```

### Line 107394 (Address `0x1800741d0`)
```assembly
   18005dc08:	74 05                	je     0x18005dc0f
   18005dc0a:	e8 79 7f ff ff       	call   0x180055b88
   18005dc0f:	33 d2                	xor    %edx,%edx
   18005dc11:	48 8d 4c 24 70       	lea    0x70(%rsp),%rcx
   18005dc16:	41 b8 98 00 00 00    	mov    $0x98,%r8d
   18005dc1c:	e8 0f 92 ff ff       	call   0x180056e30
   18005dc21:	33 d2                	xor    %edx,%edx
   18005dc23:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc27:	41 b8 d0 04 00 00    	mov    $0x4d0,%r8d
   18005dc2d:	e8 fe 91 ff ff       	call   0x180056e30
   18005dc32:	48 8d 44 24 70       	lea    0x70(%rsp),%rax
   18005dc37:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18005dc3c:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc40:	48 8d 45 10          	lea    0x10(%rbp),%rax
   18005dc44:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   18005dc49:	ff 15 81 65 01 00    	call   *0x16581(%rip)        # 0x1800741d0
   18005dc4f:	4c 8b b5 08 01 00 00 	mov    0x108(%rbp),%r14
   18005dc56:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18005dc5b:	49 8b ce             	mov    %r14,%rcx
   18005dc5e:	45 33 c0             	xor    %r8d,%r8d
```

## `KERNEL32.dll!RtlLookupFunctionEntry` (5 Call Sites)

### Line 97104 (Address `0x1800741d8`)
```assembly
   180055356:	48 89 14 01          	mov    %rdx,(%rcx,%rax,1)
   18005535a:	48 8d 0d 77 cf 03 00 	lea    0x3cf77(%rip),%rcx        # 0x1800922d8
   180055361:	e8 4e fe ff ff       	call   0x1800551b4
   180055366:	48 83 c4 28          	add    $0x28,%rsp
   18005536a:	c3                   	ret
   18005536b:	cc                   	int3
   18005536c:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180055371:	57                   	push   %rdi
   180055372:	48 83 ec 40          	sub    $0x40,%rsp
   180055376:	48 8b d9             	mov    %rcx,%rbx
   180055379:	ff 15 51 ee 01 00    	call   *0x1ee51(%rip)        # 0x1800741d0
   18005537f:	48 8b bb f8 00 00 00 	mov    0xf8(%rbx),%rdi
   180055386:	48 8d 54 24 50       	lea    0x50(%rsp),%rdx
   18005538b:	48 8b cf             	mov    %rdi,%rcx
   18005538e:	45 33 c0             	xor    %r8d,%r8d
   180055391:	ff 15 41 ee 01 00    	call   *0x1ee41(%rip)        # 0x1800741d8
   180055397:	48 85 c0             	test   %rax,%rax
   18005539a:	74 32                	je     0x1800553ce
   18005539c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   1800553a2:	48 8d 4c 24 58       	lea    0x58(%rsp),%rcx
```

### Line 97136 (Address `0x1800741d8`)
```assembly
   1800553d8:	c3                   	ret
   1800553d9:	cc                   	int3
   1800553da:	cc                   	int3
   1800553db:	cc                   	int3
   1800553dc:	40 53                	rex push %rbx
   1800553de:	56                   	push   %rsi
   1800553df:	57                   	push   %rdi
   1800553e0:	48 83 ec 40          	sub    $0x40,%rsp
   1800553e4:	48 8b d9             	mov    %rcx,%rbx
   1800553e7:	ff 15 e3 ed 01 00    	call   *0x1ede3(%rip)        # 0x1800741d0
   1800553ed:	48 8b b3 f8 00 00 00 	mov    0xf8(%rbx),%rsi
   1800553f4:	33 ff                	xor    %edi,%edi
   1800553f6:	45 33 c0             	xor    %r8d,%r8d
   1800553f9:	48 8d 54 24 60       	lea    0x60(%rsp),%rdx
   1800553fe:	48 8b ce             	mov    %rsi,%rcx
   180055401:	ff 15 d1 ed 01 00    	call   *0x1edd1(%rip)        # 0x1800741d8
   180055407:	48 85 c0             	test   %rax,%rax
   18005540a:	74 39                	je     0x180055445
   18005540c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   180055412:	48 8d 4c 24 68       	lea    0x68(%rsp),%rcx
```

### Line 97736 (Address `0x1800741d8`)
```assembly
   180055bb3:	74 04                	je     0x180055bb9
   180055bb5:	8b cb                	mov    %ebx,%ecx
   180055bb7:	cd 29                	int    $0x29
   180055bb9:	b9 03 00 00 00       	mov    $0x3,%ecx
   180055bbe:	e8 c5 ff ff ff       	call   0x180055b88
   180055bc3:	33 d2                	xor    %edx,%edx
   180055bc5:	48 8d 4d f0          	lea    -0x10(%rbp),%rcx
   180055bc9:	41 b8 d0 04 00 00    	mov    $0x4d0,%r8d
   180055bcf:	e8 5c 12 00 00       	call   0x180056e30
   180055bd4:	48 8d 4d f0          	lea    -0x10(%rbp),%rcx
   180055bd8:	ff 15 f2 e5 01 00    	call   *0x1e5f2(%rip)        # 0x1800741d0
   180055bde:	48 8b 9d e8 00 00 00 	mov    0xe8(%rbp),%rbx
   180055be5:	48 8d 95 d8 04 00 00 	lea    0x4d8(%rbp),%rdx
   180055bec:	48 8b cb             	mov    %rbx,%rcx
   180055bef:	45 33 c0             	xor    %r8d,%r8d
   180055bf2:	ff 15 e0 e5 01 00    	call   *0x1e5e0(%rip)        # 0x1800741d8
   180055bf8:	48 85 c0             	test   %rax,%rax
   180055bfb:	74 3c                	je     0x180055c39
   180055bfd:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   180055c03:	48 8d 8d e0 04 00 00 	lea    0x4e0(%rbp),%rcx
```

### Line 98223 (Address `0x1800741d8`)
```assembly
   18005624c:	4c 89 16             	mov    %r10,(%rsi)
   18005624f:	85 ff                	test   %edi,%edi
   180056251:	74 74                	je     0x1800562c7
   180056253:	49 63 46 10          	movslq 0x10(%r14),%rax
   180056257:	ff cf                	dec    %edi
   180056259:	48 8d 14 bf          	lea    (%rdi,%rdi,4),%rdx
   18005625d:	48 8d 1c 90          	lea    (%rax,%rdx,4),%rbx
   180056261:	49 03 5f 08          	add    0x8(%r15),%rbx
   180056265:	3b 6b 04             	cmp    0x4(%rbx),%ebp
   180056268:	7e e5                	jle    0x18005624f
   18005626a:	3b 6b 08             	cmp    0x8(%rbx),%ebp
   18005626d:	7f e0                	jg     0x18005624f
   18005626f:	49 8b 0f             	mov    (%r15),%rcx
   180056272:	48 8d 54 24 50       	lea    0x50(%rsp),%rdx
   180056277:	45 33 c0             	xor    %r8d,%r8d
   18005627a:	ff 15 58 df 01 00    	call   *0x1df58(%rip)        # 0x1800741d8
   180056280:	4c 63 43 10          	movslq 0x10(%rbx),%r8
   180056284:	33 c9                	xor    %ecx,%ecx
   180056286:	4c 03 44 24 50       	add    0x50(%rsp),%r8
   18005628b:	44 8b 4b 0c          	mov    0xc(%rbx),%r9d
```

### Line 107399 (Address `0x1800741d8`)
```assembly
   18005dc1c:	e8 0f 92 ff ff       	call   0x180056e30
   18005dc21:	33 d2                	xor    %edx,%edx
   18005dc23:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc27:	41 b8 d0 04 00 00    	mov    $0x4d0,%r8d
   18005dc2d:	e8 fe 91 ff ff       	call   0x180056e30
   18005dc32:	48 8d 44 24 70       	lea    0x70(%rsp),%rax
   18005dc37:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18005dc3c:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc40:	48 8d 45 10          	lea    0x10(%rbp),%rax
   18005dc44:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   18005dc49:	ff 15 81 65 01 00    	call   *0x16581(%rip)        # 0x1800741d0
   18005dc4f:	4c 8b b5 08 01 00 00 	mov    0x108(%rbp),%r14
   18005dc56:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18005dc5b:	49 8b ce             	mov    %r14,%rcx
   18005dc5e:	45 33 c0             	xor    %r8d,%r8d
   18005dc61:	ff 15 71 65 01 00    	call   *0x16571(%rip)        # 0x1800741d8
   18005dc67:	48 85 c0             	test   %rax,%rax
   18005dc6a:	74 36                	je     0x18005dca2
   18005dc6c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   18005dc72:	48 8d 4c 24 58       	lea    0x58(%rsp),%rcx
```

## `KERNEL32.dll!RtlPcToFileHeader` (1 Call Sites)

### Line 99653 (Address `0x180074240`)
```assembly
   18005747c:	0f 29 4d f0          	movaps %xmm1,-0x10(%rbp)
   180057480:	48 85 d2             	test   %rdx,%rdx
   180057483:	74 1d                	je     0x1800574a2
   180057485:	f6 02 10             	testb  $0x10,(%rdx)
   180057488:	74 18                	je     0x1800574a2
   18005748a:	48 8b 09             	mov    (%rcx),%rcx
   18005748d:	48 83 e9 08          	sub    $0x8,%rcx
   180057491:	48 8b 01             	mov    (%rcx),%rax
   180057494:	48 8b 58 30          	mov    0x30(%rax),%rbx
   180057498:	48 8b 40 40          	mov    0x40(%rax),%rax
   18005749c:	ff 15 ce ce 01 00    	call   *0x1cece(%rip)        # 0x180074370
   1800574a2:	48 8d 55 10          	lea    0x10(%rbp),%rdx
   1800574a6:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
   1800574aa:	48 8b cb             	mov    %rbx,%rcx
   1800574ad:	48 89 5d f0          	mov    %rbx,-0x10(%rbp)
   1800574b1:	ff 15 89 cd 01 00    	call   *0x1cd89(%rip)        # 0x180074240
   1800574b7:	48 89 45 10          	mov    %rax,0x10(%rbp)
   1800574bb:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
   1800574bf:	48 85 db             	test   %rbx,%rbx
   1800574c2:	74 11                	je     0x1800574d5
```

## `KERNEL32.dll!RtlUnwindEx` (3 Call Sites)

### Line 98423 (Address `0x180074230`)
```assembly
   180056500:	48 89 44 24 78       	mov    %rax,0x78(%rsp)
   180056505:	0f b6 85 10 05 00 00 	movzbl 0x510(%rbp),%eax
   18005650c:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   180056510:	49 8b 42 40          	mov    0x40(%r10),%rax
   180056514:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   180056519:	48 8d 45 d0          	lea    -0x30(%rbp),%rax
   18005651d:	4c 89 4c 24 58       	mov    %r9,0x58(%rsp)
   180056522:	45 33 c9             	xor    %r9d,%r9d
   180056525:	4c 89 44 24 70       	mov    %r8,0x70(%rsp)
   18005652a:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
   18005652f:	48 89 55 80          	mov    %rdx,-0x80(%rbp)
   180056533:	49 8b 12             	mov    (%r10),%rdx
   180056536:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18005653b:	48 c7 45 90 20 05 93 	movq   $0x19930520,-0x70(%rbp)
   180056542:	19 
   180056543:	ff 15 e7 dc 01 00    	call   *0x1dce7(%rip)        # 0x180074230
   180056549:	48 8b 8d a0 04 00 00 	mov    0x4a0(%rbp),%rcx
   180056550:	48 33 cc             	xor    %rsp,%rcx
   180056553:	e8 c8 e6 ff ff       	call   0x180054c20
   180056558:	48 81 c4 b0 05 00 00 	add    $0x5b0,%rsp
```

### Line 99404 (Address `0x180074230`)
```assembly
   180057169:	ff 15 69 b3 03 00    	call   *0x3b369(%rip)        # 0x1800924d8
   18005716f:	8b 4c fb 10          	mov    0x10(%rbx,%rdi,8),%ecx
   180057173:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   180057179:	49 03 cc             	add    %r12,%rcx
   18005717c:	49 8b d5             	mov    %r13,%rdx
   18005717f:	e8 2c 1b 00 00       	call   0x180058cb0
   180057184:	49 8b 47 40          	mov    0x40(%r15),%rax
   180057188:	4c 8b c5             	mov    %rbp,%r8
   18005718b:	8b 54 fb 10          	mov    0x10(%rbx,%rdi,8),%edx
   18005718f:	49 8b cd             	mov    %r13,%rcx
   180057192:	44 8b 4d 00          	mov    0x0(%rbp),%r9d
   180057196:	49 03 d4             	add    %r12,%rdx
   180057199:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18005719e:	49 8b 47 28          	mov    0x28(%r15),%rax
   1800571a2:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   1800571a7:	ff 15 83 d0 01 00    	call   *0x1d083(%rip)        # 0x180074230
   1800571ad:	e8 2e 1b 00 00       	call   0x180058ce0
   1800571b2:	ff c6                	inc    %esi
   1800571b4:	e9 35 ff ff ff       	jmp    0x1800570ee
   1800571b9:	33 c0                	xor    %eax,%eax
```

### Line 131616 (Address `0x180074230`)
```assembly
   18007235a:	48 8b d9             	mov    %rcx,%rbx
   18007235d:	e8 9e fb ff ff       	call   0x180071f00
   180072362:	83 e3 3f             	and    $0x3f,%ebx
   180072365:	0b c3                	or     %ebx,%eax
   180072367:	8b c8                	mov    %eax,%ecx
   180072369:	48 83 c4 20          	add    $0x20,%rsp
   18007236d:	5b                   	pop    %rbx
   18007236e:	e9 9d fb ff ff       	jmp    0x180071f10
   180072373:	cc                   	int3
   180072374:	48 83 ec 28          	sub    $0x28,%rsp
   180072378:	e8 83 fb ff ff       	call   0x180071f00
   18007237d:	83 e0 3f             	and    $0x3f,%eax
   180072380:	48 83 c4 28          	add    $0x28,%rsp
   180072384:	c3                   	ret
   180072385:	ff 25 75 1e 00 00    	jmp    *0x1e75(%rip)        # 0x180074200
   18007238b:	ff 25 9f 1e 00 00    	jmp    *0x1e9f(%rip)        # 0x180074230
   180072391:	cc                   	int3
   180072392:	cc                   	int3
   180072393:	cc                   	int3
   180072394:	cc                   	int3
```

## `KERNEL32.dll!RtlVirtualUnwind` (4 Call Sites)

### Line 97117 (Address `0x1800741e0`)
```assembly
   18005538b:	48 8b cf             	mov    %rdi,%rcx
   18005538e:	45 33 c0             	xor    %r8d,%r8d
   180055391:	ff 15 41 ee 01 00    	call   *0x1ee41(%rip)        # 0x1800741d8
   180055397:	48 85 c0             	test   %rax,%rax
   18005539a:	74 32                	je     0x1800553ce
   18005539c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   1800553a2:	48 8d 4c 24 58       	lea    0x58(%rsp),%rcx
   1800553a7:	48 8b 54 24 50       	mov    0x50(%rsp),%rdx
   1800553ac:	4c 8b c8             	mov    %rax,%r9
   1800553af:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   1800553b4:	4c 8b c7             	mov    %rdi,%r8
   1800553b7:	48 8d 4c 24 60       	lea    0x60(%rsp),%rcx
   1800553bc:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   1800553c1:	33 c9                	xor    %ecx,%ecx
   1800553c3:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   1800553c8:	ff 15 12 ee 01 00    	call   *0x1ee12(%rip)        # 0x1800741e0
   1800553ce:	48 8b 5c 24 68       	mov    0x68(%rsp),%rbx
   1800553d3:	48 83 c4 40          	add    $0x40,%rsp
   1800553d7:	5f                   	pop    %rdi
   1800553d8:	c3                   	ret
```

### Line 97149 (Address `0x1800741e0`)
```assembly
   1800553f9:	48 8d 54 24 60       	lea    0x60(%rsp),%rdx
   1800553fe:	48 8b ce             	mov    %rsi,%rcx
   180055401:	ff 15 d1 ed 01 00    	call   *0x1edd1(%rip)        # 0x1800741d8
   180055407:	48 85 c0             	test   %rax,%rax
   18005540a:	74 39                	je     0x180055445
   18005540c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   180055412:	48 8d 4c 24 68       	lea    0x68(%rsp),%rcx
   180055417:	48 8b 54 24 60       	mov    0x60(%rsp),%rdx
   18005541c:	4c 8b c8             	mov    %rax,%r9
   18005541f:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   180055424:	4c 8b c6             	mov    %rsi,%r8
   180055427:	48 8d 4c 24 70       	lea    0x70(%rsp),%rcx
   18005542c:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   180055431:	33 c9                	xor    %ecx,%ecx
   180055433:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180055438:	ff 15 a2 ed 01 00    	call   *0x1eda2(%rip)        # 0x1800741e0
   18005543e:	ff c7                	inc    %edi
   180055440:	83 ff 02             	cmp    $0x2,%edi
   180055443:	7c b1                	jl     0x1800553f6
   180055445:	48 83 c4 40          	add    $0x40,%rsp
```

### Line 97750 (Address `0x1800741e0`)
```assembly
   180055bef:	45 33 c0             	xor    %r8d,%r8d
   180055bf2:	ff 15 e0 e5 01 00    	call   *0x1e5e0(%rip)        # 0x1800741d8
   180055bf8:	48 85 c0             	test   %rax,%rax
   180055bfb:	74 3c                	je     0x180055c39
   180055bfd:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   180055c03:	48 8d 8d e0 04 00 00 	lea    0x4e0(%rbp),%rcx
   180055c0a:	48 8b 95 d8 04 00 00 	mov    0x4d8(%rbp),%rdx
   180055c11:	4c 8b c8             	mov    %rax,%r9
   180055c14:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   180055c19:	4c 8b c3             	mov    %rbx,%r8
   180055c1c:	48 8d 8d e8 04 00 00 	lea    0x4e8(%rbp),%rcx
   180055c23:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   180055c28:	48 8d 4d f0          	lea    -0x10(%rbp),%rcx
   180055c2c:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   180055c31:	33 c9                	xor    %ecx,%ecx
   180055c33:	ff 15 a7 e5 01 00    	call   *0x1e5a7(%rip)        # 0x1800741e0
   180055c39:	48 8b 85 c8 04 00 00 	mov    0x4c8(%rbp),%rax
   180055c40:	48 8d 4c 24 50       	lea    0x50(%rsp),%rcx
   180055c45:	48 89 85 e8 00 00 00 	mov    %rax,0xe8(%rbp)
   180055c4c:	33 d2                	xor    %edx,%edx
```

### Line 107413 (Address `0x1800741e0`)
```assembly
   18005dc5e:	45 33 c0             	xor    %r8d,%r8d
   18005dc61:	ff 15 71 65 01 00    	call   *0x16571(%rip)        # 0x1800741d8
   18005dc67:	48 85 c0             	test   %rax,%rax
   18005dc6a:	74 36                	je     0x18005dca2
   18005dc6c:	48 83 64 24 38 00    	andq   $0x0,0x38(%rsp)
   18005dc72:	48 8d 4c 24 58       	lea    0x58(%rsp),%rcx
   18005dc77:	48 8b 54 24 40       	mov    0x40(%rsp),%rdx
   18005dc7c:	4c 8b c8             	mov    %rax,%r9
   18005dc7f:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
   18005dc84:	4d 8b c6             	mov    %r14,%r8
   18005dc87:	48 8d 4c 24 60       	lea    0x60(%rsp),%rcx
   18005dc8c:	48 89 4c 24 28       	mov    %rcx,0x28(%rsp)
   18005dc91:	48 8d 4d 10          	lea    0x10(%rbp),%rcx
   18005dc95:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   18005dc9a:	33 c9                	xor    %ecx,%ecx
   18005dc9c:	ff 15 3e 65 01 00    	call   *0x1653e(%rip)        # 0x1800741e0
   18005dca2:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dca9:	48 89 85 08 01 00 00 	mov    %rax,0x108(%rbp)
   18005dcb0:	48 8d 85 08 05 00 00 	lea    0x508(%rbp),%rax
   18005dcb7:	48 83 c0 08          	add    $0x8,%rax
```

## `KERNEL32.dll!SetEnvironmentVariableW` (1 Call Sites)

### Line 128626 (Address `0x1800742b8`)
```assembly
   18006fb7e:	eb 14                	jmp    0x18006fb94
   18006fb80:	44 38 7d df          	cmp    %r15b,-0x21(%rbp)
   18006fb84:	74 0b                	je     0x18006fb91
   18006fb86:	48 8b 45 c7          	mov    -0x39(%rbp),%rax
   18006fb8a:	83 a0 a8 03 00 00 fd 	andl   $0xfffffffd,0x3a8(%rax)
   18006fb91:	41 8b df             	mov    %r15d,%ebx
   18006fb94:	44 8b c3             	mov    %ebx,%r8d
   18006fb97:	48 8d 55 e7          	lea    -0x19(%rbp),%rdx
   18006fb9b:	49 8b ce             	mov    %r14,%rcx
   18006fb9e:	e8 c5 c1 ff ff       	call   0x18006bd68
   18006fba3:	48 8b 7d f7          	mov    -0x9(%rbp),%rdi
   18006fba7:	85 c0                	test   %eax,%eax
   18006fba9:	75 11                	jne    0x18006fbbc
   18006fbab:	48 8b 4d 27          	mov    0x27(%rbp),%rcx
   18006fbaf:	48 8b d7             	mov    %rdi,%rdx
   18006fbb2:	ff 15 00 47 00 00    	call   *0x4700(%rip)        # 0x1800742b8
   18006fbb8:	8b d8                	mov    %eax,%ebx
   18006fbba:	eb 03                	jmp    0x18006fbbf
   18006fbbc:	41 8b df             	mov    %r15d,%ebx
   18006fbbf:	44 38 7d 0f          	cmp    %r15b,0xf(%rbp)
```

## `KERNEL32.dll!SetFilePointer` (2 Call Sites)

### Line 37877 (Address `0x1800740f8`)
```assembly
   1800227e3:	00 
   1800227e4:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   1800227eb:	00 
   1800227ec:	45 33 c9             	xor    %r9d,%r9d
   1800227ef:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   1800227f4:	45 8d 41 01          	lea    0x1(%r9),%r8d
   1800227f8:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   1800227fc:	ff 15 fe 18 05 00    	call   *0x518fe(%rip)        # 0x180074100
   180022802:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022806:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18002280a:	0f 84 78 03 00 00    	je     0x180022b88
   180022810:	41 b9 02 00 00 00    	mov    $0x2,%r9d
   180022816:	45 33 c0             	xor    %r8d,%r8d
   180022819:	33 d2                	xor    %edx,%edx
   18002281b:	48 8b c8             	mov    %rax,%rcx
   18002281e:	ff 15 d4 18 05 00    	call   *0x518d4(%rip)        # 0x1800740f8
   180022824:	8b d8                	mov    %eax,%ebx
   180022826:	ff 15 dc 18 05 00    	call   *0x518dc(%rip)        # 0x180074108
   18002282c:	83 fb ff             	cmp    $0xffffffff,%ebx
   18002282f:	75 08                	jne    0x180022839
```

### Line 38061 (Address `0x1800740f8`)
```assembly
   180022aa8:	00 
   180022aa9:	c7 44 24 20 04 00 00 	movl   $0x4,0x20(%rsp)
   180022ab0:	00 
   180022ab1:	45 33 c9             	xor    %r9d,%r9d
   180022ab4:	ba 00 00 00 c0       	mov    $0xc0000000,%edx
   180022ab9:	45 8d 41 01          	lea    0x1(%r9),%r8d
   180022abd:	49 8b 4f 18          	mov    0x18(%r15),%rcx
   180022ac1:	ff 15 39 16 05 00    	call   *0x51639(%rip)        # 0x180074100
   180022ac7:	49 89 47 08          	mov    %rax,0x8(%r15)
   180022acb:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   180022acf:	0f 84 15 01 00 00    	je     0x180022bea
   180022ad5:	41 b9 02 00 00 00    	mov    $0x2,%r9d
   180022adb:	45 33 c0             	xor    %r8d,%r8d
   180022ade:	33 d2                	xor    %edx,%edx
   180022ae0:	48 8b c8             	mov    %rax,%rcx
   180022ae3:	ff 15 0f 16 05 00    	call   *0x5160f(%rip)        # 0x1800740f8
   180022ae9:	8b d8                	mov    %eax,%ebx
   180022aeb:	ff 15 17 16 05 00    	call   *0x51617(%rip)        # 0x180074108
   180022af1:	83 fb ff             	cmp    $0xffffffff,%ebx
   180022af4:	75 08                	jne    0x180022afe
```

## `KERNEL32.dll!SetFilePointerEx` (2 Call Sites)

### Line 123939 (Address `0x180074190`)
```assembly
   18006b9ed:	8b 41 14             	mov    0x14(%rcx),%eax
   18006b9f0:	a8 c0                	test   $0xc0,%al
   18006b9f2:	74 09                	je     0x18006b9fd
   18006b9f4:	48 8b 41 08          	mov    0x8(%rcx),%rax
   18006b9f8:	48 39 01             	cmp    %rax,(%rcx)
   18006b9fb:	74 4a                	je     0x18006ba47
   18006b9fd:	8b 49 18             	mov    0x18(%rcx),%ecx
   18006ba00:	e8 df 3f 00 00       	call   0x18006f9e4
   18006ba05:	48 8b d8             	mov    %rax,%rbx
   18006ba08:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18006ba0c:	74 39                	je     0x18006ba47
   18006ba0e:	33 d2                	xor    %edx,%edx
   18006ba10:	4c 8d 44 24 38       	lea    0x38(%rsp),%r8
   18006ba15:	48 8b c8             	mov    %rax,%rcx
   18006ba18:	44 8d 4a 01          	lea    0x1(%rdx),%r9d
   18006ba1c:	ff 15 6e 87 00 00    	call   *0x876e(%rip)        # 0x180074190
   18006ba22:	85 c0                	test   %eax,%eax
   18006ba24:	74 21                	je     0x18006ba47
   18006ba26:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   18006ba2b:	48 8b cb             	mov    %rbx,%rcx
```

### Line 128939 (Address `0x180074190`)
```assembly
   18006ff9f:	48 63 d9             	movslq %ecx,%rbx
   18006ffa2:	41 8b f8             	mov    %r8d,%edi
   18006ffa5:	8b cb                	mov    %ebx,%ecx
   18006ffa7:	48 8b f2             	mov    %rdx,%rsi
   18006ffaa:	e8 35 fa ff ff       	call   0x18006f9e4
   18006ffaf:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18006ffb3:	75 11                	jne    0x18006ffc6
   18006ffb5:	e8 aa f5 fe ff       	call   0x18005f564
   18006ffba:	c7 00 09 00 00 00    	movl   $0x9,(%rax)
   18006ffc0:	48 83 c8 ff          	or     $0xffffffffffffffff,%rax
   18006ffc4:	eb 53                	jmp    0x180070019
   18006ffc6:	44 8b cf             	mov    %edi,%r9d
   18006ffc9:	4c 8d 44 24 48       	lea    0x48(%rsp),%r8
   18006ffce:	48 8b d6             	mov    %rsi,%rdx
   18006ffd1:	48 8b c8             	mov    %rax,%rcx
   18006ffd4:	ff 15 b6 41 00 00    	call   *0x41b6(%rip)        # 0x180074190
   18006ffda:	85 c0                	test   %eax,%eax
   18006ffdc:	75 0f                	jne    0x18006ffed
   18006ffde:	ff 15 24 41 00 00    	call   *0x4124(%rip)        # 0x180074108
   18006ffe4:	8b c8                	mov    %eax,%ecx
```

## `KERNEL32.dll!SetLastError` (3 Call Sites)

### Line 99770 (Address `0x180074248`)
```assembly
   180057603:	85 c0                	test   %eax,%eax
   180057605:	74 1c                	je     0x180057623
   180057607:	48 c7 c0 fe ff ff ff 	mov    $0xfffffffffffffffe,%rax
   18005760e:	89 43 78             	mov    %eax,0x78(%rbx)
   180057611:	48 89 83 80 00 00 00 	mov    %rax,0x80(%rbx)
   180057618:	48 8b c3             	mov    %rbx,%rax
   18005761b:	48 8b de             	mov    %rsi,%rbx
   18005761e:	48 8b f0             	mov    %rax,%rsi
   180057621:	eb 0d                	jmp    0x180057630
   180057623:	8b 0d 57 ed 04 00    	mov    0x4ed57(%rip),%ecx        # 0x1800a6380
   180057629:	33 d2                	xor    %edx,%edx
   18005762b:	e8 e4 19 00 00       	call   0x180059014
   180057630:	48 8b cb             	mov    %rbx,%rcx
   180057633:	e8 0c 76 00 00       	call   0x18005ec44
   180057638:	8b cf                	mov    %edi,%ecx
   18005763a:	ff 15 08 cc 01 00    	call   *0x1cc08(%rip)        # 0x180074248
   180057640:	48 8b c6             	mov    %rsi,%rax
   180057643:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   180057648:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   18005764d:	48 83 c4 20          	add    $0x20,%rsp
```

### Line 118842 (Address `0x180074248`)
```assembly
   180067477:	48 8b d7             	mov    %rdi,%rdx
   18006747a:	e8 05 31 00 00       	call   0x18006a584
   18006747f:	85 c0                	test   %eax,%eax
   180067481:	75 12                	jne    0x180067495
   180067483:	8b 0d 27 f0 03 00    	mov    0x3f027(%rip),%ecx        # 0x1800a64b0
   180067489:	33 d2                	xor    %edx,%edx
   18006748b:	e8 f4 30 00 00       	call   0x18006a584
   180067490:	48 8b cf             	mov    %rdi,%rcx
   180067493:	eb db                	jmp    0x180067470
   180067495:	48 8b cf             	mov    %rdi,%rcx
   180067498:	e8 cb fc ff ff       	call   0x180067168
   18006749d:	33 c9                	xor    %ecx,%ecx
   18006749f:	e8 18 f4 ff ff       	call   0x1800668bc
   1800674a4:	48 8b f7             	mov    %rdi,%rsi
   1800674a7:	8b cb                	mov    %ebx,%ecx
   1800674a9:	ff 15 99 cd 00 00    	call   *0xcd99(%rip)        # 0x180074248
   1800674af:	48 f7 df             	neg    %rdi
   1800674b2:	48 1b c0             	sbb    %rax,%rax
   1800674b5:	48 23 c6             	and    %rsi,%rax
   1800674b8:	74 10                	je     0x1800674ca
```

### Line 118955 (Address `0x180074248`)
```assembly
   1800675f3:	48 8b d7             	mov    %rdi,%rdx
   1800675f6:	e8 89 2f 00 00       	call   0x18006a584
   1800675fb:	85 c0                	test   %eax,%eax
   1800675fd:	75 12                	jne    0x180067611
   1800675ff:	8b 0d ab ee 03 00    	mov    0x3eeab(%rip),%ecx        # 0x1800a64b0
   180067605:	33 d2                	xor    %edx,%edx
   180067607:	e8 78 2f 00 00       	call   0x18006a584
   18006760c:	48 8b cf             	mov    %rdi,%rcx
   18006760f:	eb db                	jmp    0x1800675ec
   180067611:	48 8b cf             	mov    %rdi,%rcx
   180067614:	e8 4f fb ff ff       	call   0x180067168
   180067619:	33 c9                	xor    %ecx,%ecx
   18006761b:	e8 9c f2 ff ff       	call   0x1800668bc
   180067620:	48 8b f7             	mov    %rdi,%rsi
   180067623:	8b cb                	mov    %ebx,%ecx
   180067625:	ff 15 1d cc 00 00    	call   *0xcc1d(%rip)        # 0x180074248
   18006762b:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   180067630:	48 f7 df             	neg    %rdi
   180067633:	48 1b c0             	sbb    %rax,%rax
   180067636:	48 23 c6             	and    %rsi,%rax
```

## `KERNEL32.dll!SetStdHandle` (1 Call Sites)

### Line 128481 (Address `0x180074000`)
```assembly
   18006f977:	e8 f0 91 ff ff       	call   0x180068b6c
   18006f97c:	83 f8 01             	cmp    $0x1,%eax
   18006f97f:	75 27                	jne    0x18006f9a8
   18006f981:	85 db                	test   %ebx,%ebx
   18006f983:	74 16                	je     0x18006f99b
   18006f985:	2b d8                	sub    %eax,%ebx
   18006f987:	74 0b                	je     0x18006f994
   18006f989:	3b d8                	cmp    %eax,%ebx
   18006f98b:	75 1b                	jne    0x18006f9a8
   18006f98d:	b9 f4 ff ff ff       	mov    $0xfffffff4,%ecx
   18006f992:	eb 0c                	jmp    0x18006f9a0
   18006f994:	b9 f5 ff ff ff       	mov    $0xfffffff5,%ecx
   18006f999:	eb 05                	jmp    0x18006f9a0
   18006f99b:	b9 f6 ff ff ff       	mov    $0xfffffff6,%ecx
   18006f9a0:	33 d2                	xor    %edx,%edx
   18006f9a2:	ff 15 58 46 00 00    	call   *0x4658(%rip)        # 0x180074000
   18006f9a8:	49 8b 04 f6          	mov    (%r14,%rsi,8),%rax
   18006f9ac:	48 83 4c f8 28 ff    	orq    $0xffffffffffffffff,0x28(%rax,%rdi,8)
   18006f9b2:	33 c0                	xor    %eax,%eax
   18006f9b4:	eb 16                	jmp    0x18006f9cc
```

## `KERNEL32.dll!SetUnhandledExceptionFilter` (3 Call Sites)

### Line 97001 (Address `0x1800741f0`)
```assembly
   18005518a:	cc                   	int3
   18005518b:	cc                   	int3
   18005518c:	48 83 ec 28          	sub    $0x28,%rsp
   180055190:	48 8d 0d c1 21 05 00 	lea    0x521c1(%rip),%rcx        # 0x1800a7358
   180055197:	ff 15 33 ef 01 00    	call   *0x1ef33(%rip)        # 0x1800740d0
   18005519d:	48 8b 0d e4 21 05 00 	mov    0x521e4(%rip),%rcx        # 0x1800a7388
   1800551a4:	48 85 c9             	test   %rcx,%rcx
   1800551a7:	74 06                	je     0x1800551af
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
   1800551af:	48 83 c4 28          	add    $0x28,%rsp
   1800551b3:	c3                   	ret
   1800551b4:	40 53                	rex push %rbx
   1800551b6:	48 83 ec 20          	sub    $0x20,%rsp
   1800551ba:	48 8b d9             	mov    %rcx,%rbx
   1800551bd:	33 c9                	xor    %ecx,%ecx
   1800551bf:	ff 15 2b f0 01 00    	call   *0x1f02b(%rip)        # 0x1800741f0
   1800551c5:	48 8b cb             	mov    %rbx,%rcx
   1800551c8:	ff 15 1a f0 01 00    	call   *0x1f01a(%rip)        # 0x1800741e8
   1800551ce:	ff 15 94 ef 01 00    	call   *0x1ef94(%rip)        # 0x180074168
   1800551d4:	48 8b c8             	mov    %rax,%rcx
```

### Line 97774 (Address `0x1800741f0`)
```assembly
   180055c66:	e8 c5 11 00 00       	call   0x180056e30
   180055c6b:	48 8b 85 c8 04 00 00 	mov    0x4c8(%rbp),%rax
   180055c72:	48 89 44 24 60       	mov    %rax,0x60(%rsp)
   180055c77:	c7 44 24 50 15 00 00 	movl   $0x40000015,0x50(%rsp)
   180055c7e:	40 
   180055c7f:	c7 44 24 54 01 00 00 	movl   $0x1,0x54(%rsp)
   180055c86:	00 
   180055c87:	ff 15 93 e5 01 00    	call   *0x1e593(%rip)        # 0x180074220
   180055c8d:	83 f8 01             	cmp    $0x1,%eax
   180055c90:	48 8d 44 24 50       	lea    0x50(%rsp),%rax
   180055c95:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   180055c9a:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
   180055c9e:	0f 94 c3             	sete   %bl
   180055ca1:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   180055ca6:	33 c9                	xor    %ecx,%ecx
   180055ca8:	ff 15 42 e5 01 00    	call   *0x1e542(%rip)        # 0x1800741f0
   180055cae:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180055cb3:	ff 15 2f e5 01 00    	call   *0x1e52f(%rip)        # 0x1800741e8
   180055cb9:	85 c0                	test   %eax,%eax
   180055cbb:	75 0c                	jne    0x180055cc9
```

### Line 107426 (Address `0x1800741f0`)
```assembly
   18005dc95:	48 89 4c 24 20       	mov    %rcx,0x20(%rsp)
   18005dc9a:	33 c9                	xor    %ecx,%ecx
   18005dc9c:	ff 15 3e 65 01 00    	call   *0x1653e(%rip)        # 0x1800741e0
   18005dca2:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dca9:	48 89 85 08 01 00 00 	mov    %rax,0x108(%rbp)
   18005dcb0:	48 8d 85 08 05 00 00 	lea    0x508(%rbp),%rax
   18005dcb7:	48 83 c0 08          	add    $0x8,%rax
   18005dcbb:	89 74 24 70          	mov    %esi,0x70(%rsp)
   18005dcbf:	48 89 85 a8 00 00 00 	mov    %rax,0xa8(%rbp)
   18005dcc6:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dccd:	48 89 45 80          	mov    %rax,-0x80(%rbp)
   18005dcd1:	89 7c 24 74          	mov    %edi,0x74(%rsp)
   18005dcd5:	ff 15 45 65 01 00    	call   *0x16545(%rip)        # 0x180074220
   18005dcdb:	33 c9                	xor    %ecx,%ecx
   18005dcdd:	8b f8                	mov    %eax,%edi
   18005dcdf:	ff 15 0b 65 01 00    	call   *0x1650b(%rip)        # 0x1800741f0
   18005dce5:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18005dcea:	ff 15 f8 64 01 00    	call   *0x164f8(%rip)        # 0x1800741e8
   18005dcf0:	85 c0                	test   %eax,%eax
   18005dcf2:	75 10                	jne    0x18005dd04
```

## `KERNEL32.dll!Sleep` (34 Call Sites)

### Line 26804 (Address `0x180074080`)
```assembly
   180018789:	74 44                	je     0x1800187cf
   18001878b:	48 8b 0d fe e5 08 00 	mov    0x8e5fe(%rip),%rcx        # 0x1800a6d90
   180018792:	48 83 f9 ff          	cmp    $0xffffffffffffffff,%rcx
   180018796:	74 11                	je     0x1800187a9
   180018798:	ff 15 ea b8 05 00    	call   *0x5b8ea(%rip)        # 0x180074088
   18001879e:	48 c7 05 e7 e5 08 00 	movq   $0xffffffffffffffff,0x8e5e7(%rip)        # 0x1800a6d90
   1800187a5:	ff ff ff ff 
   1800187a9:	48 8b 0d 80 fe 08 00 	mov    0x8fe80(%rip),%rcx        # 0x1800a8630
   1800187b0:	48 85 c9             	test   %rcx,%rcx
   1800187b3:	74 13                	je     0x1800187c8
   1800187b5:	e8 8a 64 04 00       	call   0x18005ec44
   1800187ba:	4c 89 25 6f fe 08 00 	mov    %r12,0x8fe6f(%rip)        # 0x1800a8630
   1800187c1:	4c 89 25 60 fe 08 00 	mov    %r12,0x8fe60(%rip)        # 0x1800a8628
   1800187c8:	c6 85 f9 03 00 00 00 	movb   $0x0,0x3f9(%rbp)
   1800187cf:	b9 90 01 00 00       	mov    $0x190,%ecx
   1800187d4:	ff 15 a6 b8 05 00    	call   *0x5b8a6(%rip)        # 0x180074080
   1800187da:	0f b6 45 15          	movzbl 0x15(%rbp),%eax
   1800187de:	84 c0                	test   %al,%al
   1800187e0:	0f 84 1f fe ff ff    	je     0x180018605
   1800187e6:	48 8d 15 a3 25 08 00 	lea    0x825a3(%rip),%rdx        # 0x18009ad90
```

### Line 29657 (Address `0x180074080`)
```assembly
   18001af79:	e8 62 b3 ff ff       	call   0x1800162e0
   18001af7e:	bd 03 00 00 00       	mov    $0x3,%ebp
   18001af83:	8b dd                	mov    %ebp,%ebx
   18001af85:	ff cb                	dec    %ebx
   18001af87:	49 8b ce             	mov    %r14,%rcx
   18001af8a:	ff 15 a8 93 05 00    	call   *0x593a8(%rip)        # 0x180074338
   18001af90:	48 89 86 90 01 00 00 	mov    %rax,0x190(%rsi)
   18001af97:	48 85 c0             	test   %rax,%rax
   18001af9a:	75 24                	jne    0x18001afc0
   18001af9c:	48 8d 15 e5 19 08 00 	lea    0x819e5(%rip),%rdx        # 0x18009c988
   18001afa3:	48 8b 0d 5e d6 08 00 	mov    0x8d65e(%rip),%rcx        # 0x1800a8608
   18001afaa:	e8 e1 b2 ff ff       	call   0x180016290
   18001afaf:	85 db                	test   %ebx,%ebx
   18001afb1:	74 0d                	je     0x18001afc0
   18001afb3:	b9 f4 01 00 00       	mov    $0x1f4,%ecx
   18001afb8:	ff 15 c2 90 05 00    	call   *0x590c2(%rip)        # 0x180074080
   18001afbe:	eb c5                	jmp    0x18001af85
   18001afc0:	48 83 be 90 01 00 00 	cmpq   $0x0,0x190(%rsi)
   18001afc7:	00 
   18001afc8:	75 3c                	jne    0x18001b006
```

### Line 29875 (Address `0x180074080`)
```assembly
   18001b2af:	49 8b 07             	mov    (%r15),%rax
   18001b2b2:	49 8b cf             	mov    %r15,%rcx
   18001b2b5:	ff 50 08             	call   *0x8(%rax)
   18001b2b8:	90                   	nop
   18001b2b9:	49 8d be c0 01 00 00 	lea    0x1c0(%r14),%rdi
   18001b2c0:	8d 6e 02             	lea    0x2(%rsi),%ebp
   18001b2c3:	bb 64 00 00 00       	mov    $0x64,%ebx
   18001b2c8:	83 7f 08 01          	cmpl   $0x1,0x8(%rdi)
   18001b2cc:	75 1c                	jne    0x18001b2ea
   18001b2ce:	66 90                	xchg   %ax,%ax
   18001b2d0:	8b c3                	mov    %ebx,%eax
   18001b2d2:	ff cb                	dec    %ebx
   18001b2d4:	85 c0                	test   %eax,%eax
   18001b2d6:	74 12                	je     0x18001b2ea
   18001b2d8:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001b2dd:	ff 15 9d 8d 05 00    	call   *0x58d9d(%rip)        # 0x180074080
   18001b2e3:	90                   	nop
   18001b2e4:	83 7f 08 01          	cmpl   $0x1,0x8(%rdi)
   18001b2e8:	74 e6                	je     0x18001b2d0
   18001b2ea:	48 8b 0f             	mov    (%rdi),%rcx
```

### Line 29979 (Address `0x180074080`)
```assembly
   18001b438:	e8 53 ae ff ff       	call   0x180016290
   18001b43d:	c7 43 18 04 00 00 00 	movl   $0x4,0x18(%rbx)
   18001b444:	e9 03 05 00 00       	jmp    0x18001b94c
   18001b449:	c6 83 95 05 00 00 01 	movb   $0x1,0x595(%rbx)
   18001b450:	83 7b 28 00          	cmpl   $0x0,0x28(%rbx)
   18001b454:	75 55                	jne    0x18001b4ab
   18001b456:	48 8b cb             	mov    %rbx,%rcx
   18001b459:	e8 b2 53 00 00       	call   0x180020810
   18001b45e:	48 8b 0d a3 d1 08 00 	mov    0x8d1a3(%rip),%rcx        # 0x1800a8608
   18001b465:	85 c0                	test   %eax,%eax
   18001b467:	74 1f                	je     0x18001b488
   18001b469:	44 8b c0             	mov    %eax,%r8d
   18001b46c:	48 8d 15 6d 17 08 00 	lea    0x8176d(%rip),%rdx        # 0x18009cbe0
   18001b473:	e8 18 ae ff ff       	call   0x180016290
   18001b478:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001b47d:	ff 15 fd 8b 05 00    	call   *0x58bfd(%rip)        # 0x180074080
   18001b483:	e9 c4 04 00 00       	jmp    0x18001b94c
   18001b488:	0f b6 83 a1 05 00 00 	movzbl 0x5a1(%rbx),%eax
   18001b48f:	48 8d 15 7a 17 08 00 	lea    0x8177a(%rip),%rdx        # 0x18009cc10
   18001b496:	44 0f b6 8b a8 05 00 	movzbl 0x5a8(%rbx),%r9d
```

### Line 30035 (Address `0x180074080`)
```assembly
   18001b547:	75 4d                	jne    0x18001b596
   18001b549:	81 7b 28 32 91 00 00 	cmpl   $0x9132,0x28(%rbx)
   18001b550:	4c 8d 45 c0          	lea    -0x40(%rbp),%r8
   18001b554:	ba e9 f7 00 00       	mov    $0xf7e9,%edx
   18001b559:	c6 45 c0 00          	movb   $0x0,-0x40(%rbp)
   18001b55d:	b8 39 f4 00 00       	mov    $0xf439,%eax
   18001b562:	48 8b cb             	mov    %rbx,%rcx
   18001b565:	0f 45 d0             	cmovne %eax,%edx
   18001b568:	e8 83 35 00 00       	call   0x18001eaf0
   18001b56d:	f6 45 c0 01          	testb  $0x1,-0x40(%rbp)
   18001b571:	74 23                	je     0x18001b596
   18001b573:	48 8b 0d 8e d0 08 00 	mov    0x8d08e(%rip),%rcx        # 0x1800a8608
   18001b57a:	48 8d 15 87 17 08 00 	lea    0x81787(%rip),%rdx        # 0x18009cd08
   18001b581:	e8 0a ad ff ff       	call   0x180016290
   18001b586:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001b58b:	ff 15 ef 8a 05 00    	call   *0x58aef(%rip)        # 0x180074080
   18001b591:	e9 b6 03 00 00       	jmp    0x18001b94c
   18001b596:	4c 8d 4d c8          	lea    -0x38(%rbp),%r9
   18001b59a:	ba e0 1f 00 00       	mov    $0x1fe0,%edx
   18001b59f:	41 b8 20 00 00 00    	mov    $0x20,%r8d
```

### Line 30256 (Address `0x180074080`)
```assembly
   18001b8ee:	41 80 c8 3c          	or     $0x3c,%r8b
   18001b8f2:	48 8b cb             	mov    %rbx,%rcx
   18001b8f5:	e8 b6 2b 00 00       	call   0x18001e4b0
   18001b8fa:	ba 01 00 00 00       	mov    $0x1,%edx
   18001b8ff:	48 8b cb             	mov    %rbx,%rcx
   18001b902:	e8 a9 1e 00 00       	call   0x18001d7b0
   18001b907:	ff 15 53 88 05 00    	call   *0x58853(%rip)        # 0x180074160
   18001b90d:	48 8b cb             	mov    %rbx,%rcx
   18001b910:	89 83 7c 05 00 00    	mov    %eax,0x57c(%rbx)
   18001b916:	e8 45 00 00 00       	call   0x18001b960
   18001b91b:	84 c0                	test   %al,%al
   18001b91d:	74 1d                	je     0x18001b93c
   18001b91f:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001b924:	c7 83 90 05 00 00 00 	movl   $0x0,0x590(%rbx)
   18001b92b:	00 00 00 
   18001b92e:	ff 15 4c 87 05 00    	call   *0x5874c(%rip)        # 0x180074080
   18001b934:	48 8b cb             	mov    %rbx,%rcx
   18001b937:	e8 d4 08 00 00       	call   0x18001c210
   18001b93c:	48 8b b4 24 98 00 00 	mov    0x98(%rsp),%rsi
   18001b943:	00 
```

### Line 32041 (Address `0x180074080`)
```assembly
   18001d32f:	cc                   	int3
   18001d330:	40 53                	rex push %rbx
   18001d332:	48 83 ec 20          	sub    $0x20,%rsp
   18001d336:	0f b6 41 15          	movzbl 0x15(%rcx),%eax
   18001d33a:	48 8b d9             	mov    %rcx,%rbx
   18001d33d:	84 c0                	test   %al,%al
   18001d33f:	0f 85 cc 01 00 00    	jne    0x18001d511
   18001d345:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
   18001d34a:	33 f6                	xor    %esi,%esi
   18001d34c:	48 89 7c 24 38       	mov    %rdi,0x38(%rsp)
   18001d351:	ff 15 09 6e 05 00    	call   *0x56e09(%rip)        # 0x180074160
   18001d357:	8b f8                	mov    %eax,%edi
   18001d359:	40 38 73 14          	cmp    %sil,0x14(%rbx)
   18001d35d:	75 10                	jne    0x18001d36f
   18001d35f:	b9 e8 03 00 00       	mov    $0x3e8,%ecx
   18001d364:	ff 15 16 6d 05 00    	call   *0x56d16(%rip)        # 0x180074080
   18001d36a:	e9 8c 01 00 00       	jmp    0x18001d4fb
   18001d36f:	8b 4b 18             	mov    0x18(%rbx),%ecx
   18001d372:	85 c9                	test   %ecx,%ecx
   18001d374:	0f 84 6e 01 00 00    	je     0x18001d4e8
```

### Line 32056 (Address `0x180074080`)
```assembly
   18001d364:	ff 15 16 6d 05 00    	call   *0x56d16(%rip)        # 0x180074080
   18001d36a:	e9 8c 01 00 00       	jmp    0x18001d4fb
   18001d36f:	8b 4b 18             	mov    0x18(%rbx),%ecx
   18001d372:	85 c9                	test   %ecx,%ecx
   18001d374:	0f 84 6e 01 00 00    	je     0x18001d4e8
   18001d37a:	83 e9 01             	sub    $0x1,%ecx
   18001d37d:	0f 84 27 01 00 00    	je     0x18001d4aa
   18001d383:	83 e9 02             	sub    $0x2,%ecx
   18001d386:	74 29                	je     0x18001d3b1
   18001d388:	83 f9 01             	cmp    $0x1,%ecx
   18001d38b:	0f 85 6a 01 00 00    	jne    0x18001d4fb
   18001d391:	40 38 b3 a8 01 00 00 	cmp    %sil,0x1a8(%rbx)
   18001d398:	74 07                	je     0x18001d3a1
   18001d39a:	40 88 b3 a8 01 00 00 	mov    %sil,0x1a8(%rbx)
   18001d3a1:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001d3a6:	ff 15 d4 6c 05 00    	call   *0x56cd4(%rip)        # 0x180074080
   18001d3ac:	e9 4a 01 00 00       	jmp    0x18001d4fb
   18001d3b1:	8b 83 7c 05 00 00    	mov    0x57c(%rbx),%eax
   18001d3b7:	3b f8                	cmp    %eax,%edi
   18001d3b9:	72 09                	jb     0x18001d3c4
```

### Line 32129 (Address `0x180074080`)
```assembly
   18001d49c:	e8 4f 23 00 00       	call   0x18001f7f0
   18001d4a1:	40 88 b3 96 05 00 00 	mov    %sil,0x596(%rbx)
   18001d4a8:	eb 51                	jmp    0x18001d4fb
   18001d4aa:	8b 83 7c 05 00 00    	mov    0x57c(%rbx),%eax
   18001d4b0:	3b f8                	cmp    %eax,%edi
   18001d4b2:	72 07                	jb     0x18001d4bb
   18001d4b4:	83 c0 64             	add    $0x64,%eax
   18001d4b7:	3b f8                	cmp    %eax,%edi
   18001d4b9:	72 40                	jb     0x18001d4fb
   18001d4bb:	48 8b cb             	mov    %rbx,%rcx
   18001d4be:	e8 9d e4 ff ff       	call   0x18001b960
   18001d4c3:	84 c0                	test   %al,%al
   18001d4c5:	74 19                	je     0x18001d4e0
   18001d4c7:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001d4cc:	89 b3 90 05 00 00    	mov    %esi,0x590(%rbx)
   18001d4d2:	ff 15 a8 6b 05 00    	call   *0x56ba8(%rip)        # 0x180074080
   18001d4d8:	48 8b cb             	mov    %rbx,%rcx
   18001d4db:	e8 30 ed ff ff       	call   0x18001c210
   18001d4e0:	89 bb 7c 05 00 00    	mov    %edi,0x57c(%rbx)
   18001d4e6:	eb 13                	jmp    0x18001d4fb
```

### Line 32135 (Address `0x180074080`)
```assembly
   18001d4b4:	83 c0 64             	add    $0x64,%eax
   18001d4b7:	3b f8                	cmp    %eax,%edi
   18001d4b9:	72 40                	jb     0x18001d4fb
   18001d4bb:	48 8b cb             	mov    %rbx,%rcx
   18001d4be:	e8 9d e4 ff ff       	call   0x18001b960
   18001d4c3:	84 c0                	test   %al,%al
   18001d4c5:	74 19                	je     0x18001d4e0
   18001d4c7:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001d4cc:	89 b3 90 05 00 00    	mov    %esi,0x590(%rbx)
   18001d4d2:	ff 15 a8 6b 05 00    	call   *0x56ba8(%rip)        # 0x180074080
   18001d4d8:	48 8b cb             	mov    %rbx,%rcx
   18001d4db:	e8 30 ed ff ff       	call   0x18001c210
   18001d4e0:	89 bb 7c 05 00 00    	mov    %edi,0x57c(%rbx)
   18001d4e6:	eb 13                	jmp    0x18001d4fb
   18001d4e8:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001d4ed:	ff 15 8d 6b 05 00    	call   *0x56b8d(%rip)        # 0x180074080
   18001d4f3:	48 8b cb             	mov    %rbx,%rcx
   18001d4f6:	e8 a5 de ff ff       	call   0x18001b3a0
   18001d4fb:	0f b6 43 15          	movzbl 0x15(%rbx),%eax
   18001d4ff:	84 c0                	test   %al,%al
```

### Line 32381 (Address `0x180074080`)
```assembly
   18001d7fb:	cc                   	int3
   18001d7fc:	cc                   	int3
   18001d7fd:	cc                   	int3
   18001d7fe:	cc                   	int3
   18001d7ff:	cc                   	int3
   18001d800:	40 53                	rex push %rbx
   18001d802:	57                   	push   %rdi
   18001d803:	48 83 ec 58          	sub    $0x58,%rsp
   18001d807:	48 8b 05 52 8b 08 00 	mov    0x88b52(%rip),%rax        # 0x1800a6360
   18001d80e:	48 33 c4             	xor    %rsp,%rax
   18001d811:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
   18001d816:	83 79 18 03          	cmpl   $0x3,0x18(%rcx)
   18001d81a:	48 8b d9             	mov    %rcx,%rbx
   18001d81d:	74 15                	je     0x18001d834
   18001d81f:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001d824:	ff 15 56 68 05 00    	call   *0x56856(%rip)        # 0x180074080
   18001d82a:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
   18001d82f:	e9 ab 04 00 00       	jmp    0x18001dcdf
   18001d834:	80 b9 96 05 00 00 00 	cmpb   $0x0,0x596(%rcx)
   18001d83b:	75 15                	jne    0x18001d852
```

### Line 32387 (Address `0x180074080`)
```assembly
   18001d802:	57                   	push   %rdi
   18001d803:	48 83 ec 58          	sub    $0x58,%rsp
   18001d807:	48 8b 05 52 8b 08 00 	mov    0x88b52(%rip),%rax        # 0x1800a6360
   18001d80e:	48 33 c4             	xor    %rsp,%rax
   18001d811:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
   18001d816:	83 79 18 03          	cmpl   $0x3,0x18(%rcx)
   18001d81a:	48 8b d9             	mov    %rcx,%rbx
   18001d81d:	74 15                	je     0x18001d834
   18001d81f:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001d824:	ff 15 56 68 05 00    	call   *0x56856(%rip)        # 0x180074080
   18001d82a:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
   18001d82f:	e9 ab 04 00 00       	jmp    0x18001dcdf
   18001d834:	80 b9 96 05 00 00 00 	cmpb   $0x0,0x596(%rcx)
   18001d83b:	75 15                	jne    0x18001d852
   18001d83d:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001d842:	ff 15 38 68 05 00    	call   *0x56838(%rip)        # 0x180074080
   18001d848:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001d84d:	e9 8d 04 00 00       	jmp    0x18001dcdf
   18001d852:	48 8b 3d c7 ad 08 00 	mov    0x8adc7(%rip),%rdi        # 0x1800a8620
   18001d859:	48 89 6c 24 78       	mov    %rbp,0x78(%rsp)
```

### Line 32423 (Address `0x180074080`)
```assembly
   18001d8a2:	8b 87 68 20 00 00    	mov    0x2068(%rdi),%eax
   18001d8a8:	3d ff 03 00 00       	cmp    $0x3ff,%eax
   18001d8ad:	7c 04                	jl     0x18001d8b3
   18001d8af:	8b c5                	mov    %ebp,%eax
   18001d8b1:	eb 02                	jmp    0x18001d8b5
   18001d8b3:	ff c0                	inc    %eax
   18001d8b5:	89 87 68 20 00 00    	mov    %eax,0x2068(%rdi)
   18001d8bb:	44 8b ab b0 01 00 00 	mov    0x1b0(%rbx),%r13d
   18001d8c2:	41 8b f5             	mov    %r13d,%esi
   18001d8c5:	83 e6 01             	and    $0x1,%esi
   18001d8c8:	48 c1 e6 05          	shl    $0x5,%rsi
   18001d8cc:	48 03 f3             	add    %rbx,%rsi
   18001d8cf:	83 be c8 01 00 00 02 	cmpl   $0x2,0x1c8(%rsi)
   18001d8d6:	74 15                	je     0x18001d8ed
   18001d8d8:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001d8dd:	ff 15 9d 67 05 00    	call   *0x5679d(%rip)        # 0x180074080
   18001d8e3:	b8 fd ff ff ff       	mov    $0xfffffffd,%eax
   18001d8e8:	e9 e0 03 00 00       	jmp    0x18001dccd
   18001d8ed:	40 38 ab a1 05 00 00 	cmp    %bpl,0x5a1(%rbx)
   18001d8f4:	0f 85 3f 01 00 00    	jne    0x18001da39
```

### Line 32502 (Address `0x180074080`)
```assembly
   18001da1c:	74 5d                	je     0x18001da7b
   18001da1e:	48 8d 15 2b f0 07 00 	lea    0x7f02b(%rip),%rdx        # 0x18009ca50
   18001da25:	e8 66 88 ff ff       	call   0x180016290
   18001da2a:	48 8b cb             	mov    %rbx,%rcx
   18001da2d:	c6 83 a0 05 00 00 01 	movb   $0x1,0x5a0(%rbx)
   18001da34:	e8 c7 02 00 00       	call   0x18001dd00
   18001da39:	4c 89 74 24 48       	mov    %r14,0x48(%rsp)
   18001da3e:	4c 89 7c 24 40       	mov    %r15,0x40(%rsp)
   18001da43:	40 38 ab a0 05 00 00 	cmp    %bpl,0x5a0(%rbx)
   18001da4a:	74 7e                	je     0x18001daca
   18001da4c:	44 8b 83 84 00 00 00 	mov    0x84(%rbx),%r8d
   18001da53:	48 8d 15 56 fb 07 00 	lea    0x7fb56(%rip),%rdx        # 0x18009d5b0
   18001da5a:	48 8b 0d a7 ab 08 00 	mov    0x8aba7(%rip),%rcx        # 0x1800a8608
   18001da61:	e8 2a 88 ff ff       	call   0x180016290
   18001da66:	b9 64 00 00 00       	mov    $0x64,%ecx
   18001da6b:	ff 15 0f 66 05 00    	call   *0x5660f(%rip)        # 0x180074080
   18001da71:	bf 9d ff ff ff       	mov    $0xffffff9d,%edi
   18001da76:	e9 50 01 00 00       	jmp    0x18001dbcb
   18001da7b:	48 8d 15 4e f0 07 00 	lea    0x7f04e(%rip),%rdx        # 0x18009cad0
   18001da82:	e8 09 88 ff ff       	call   0x180016290
```

### Line 32692 (Address `0x180074080`)
```assembly
   18001dd48:	bd 02 00 00 00       	mov    $0x2,%ebp
   18001dd4d:	0f 1f 00             	nopl   (%rax)
   18001dd50:	83 3f 01             	cmpl   $0x1,(%rdi)
   18001dd53:	8b de                	mov    %esi,%ebx
   18001dd55:	75 37                	jne    0x18001dd8e
   18001dd57:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
   18001dd5e:	00 00 
   18001dd60:	8b c3                	mov    %ebx,%eax
   18001dd62:	ff c3                	inc    %ebx
   18001dd64:	3d e8 03 00 00       	cmp    $0x3e8,%eax
   18001dd69:	7d 23                	jge    0x18001dd8e
   18001dd6b:	48 8b 0d 96 a8 08 00 	mov    0x8a896(%rip),%rcx        # 0x1800a8608
   18001dd72:	48 8d 15 a7 f9 07 00 	lea    0x7f9a7(%rip),%rdx        # 0x18009d720
   18001dd79:	e8 12 85 ff ff       	call   0x180016290
   18001dd7e:	b9 01 00 00 00       	mov    $0x1,%ecx
   18001dd83:	ff 15 f7 62 05 00    	call   *0x562f7(%rip)        # 0x180074080
   18001dd89:	83 3f 01             	cmpl   $0x1,(%rdi)
   18001dd8c:	74 d2                	je     0x18001dd60
   18001dd8e:	89 77 f4             	mov    %esi,-0xc(%rdi)
   18001dd91:	89 37                	mov    %esi,(%rdi)
```

### Line 34607 (Address `0x180074080`)
```assembly
   18001f937:	e8 74 de ff ff       	call   0x18001d7b0
   18001f93c:	8d 83 18 fc ff ff    	lea    -0x3e8(%rbx),%eax
   18001f942:	eb 3e                	jmp    0x18001f982
   18001f944:	8b 86 70 05 00 00    	mov    0x570(%rsi),%eax
   18001f94a:	85 c0                	test   %eax,%eax
   18001f94c:	7e 08                	jle    0x18001f956
   18001f94e:	ff c8                	dec    %eax
   18001f950:	89 86 70 05 00 00    	mov    %eax,0x570(%rsi)
   18001f956:	48 8b 0d ab 8c 08 00 	mov    0x88cab(%rip),%rcx        # 0x1800a8608
   18001f95d:	48 8d 15 fc df 07 00 	lea    0x7dffc(%rip),%rdx        # 0x18009d960
   18001f964:	40 84 ed             	test   %bpl,%bpl
   18001f967:	75 07                	jne    0x18001f970
   18001f969:	48 8d 15 18 e0 07 00 	lea    0x7e018(%rip),%rdx        # 0x18009d988
   18001f970:	e8 1b 69 ff ff       	call   0x180016290
   18001f975:	b9 0a 00 00 00       	mov    $0xa,%ecx
   18001f97a:	ff 15 00 47 05 00    	call   *0x54700(%rip)        # 0x180074080
   18001f980:	33 c0                	xor    %eax,%eax
   18001f982:	48 8b 4c 24 50       	mov    0x50(%rsp),%rcx
   18001f987:	48 33 cc             	xor    %rsp,%rcx
   18001f98a:	e8 91 52 03 00       	call   0x180054c20
```

### Line 34722 (Address `0x180074080`)
```assembly
   18001faec:	7c 20                	jl     0x18001fb0e
   18001faee:	48 8b 0d 13 8b 08 00 	mov    0x88b13(%rip),%rcx        # 0x1800a8608
   18001faf5:	48 8d 15 fc dc 07 00 	lea    0x7dcfc(%rip),%rdx        # 0x18009d7f8
   18001fafc:	e8 8f 67 ff ff       	call   0x180016290
   18001fb01:	ba 04 00 00 00       	mov    $0x4,%edx
   18001fb06:	48 8b ce             	mov    %rsi,%rcx
   18001fb09:	e8 a2 dc ff ff       	call   0x18001d7b0
   18001fb0e:	8d 83 18 fc ff ff    	lea    -0x3e8(%rbx),%eax
   18001fb14:	e9 18 01 00 00       	jmp    0x18001fc31
   18001fb19:	8b 86 70 05 00 00    	mov    0x570(%rsi),%eax
   18001fb1f:	85 c0                	test   %eax,%eax
   18001fb21:	7e 08                	jle    0x18001fb2b
   18001fb23:	ff c8                	dec    %eax
   18001fb25:	89 86 70 05 00 00    	mov    %eax,0x570(%rsi)
   18001fb2b:	b9 0a 00 00 00       	mov    $0xa,%ecx
   18001fb30:	ff 15 4a 45 05 00    	call   *0x5454a(%rip)        # 0x180074080
   18001fb36:	8b 46 28             	mov    0x28(%rsi),%eax
   18001fb39:	bb 64 00 00 00       	mov    $0x64,%ebx
   18001fb3e:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18001fb43:	75 4f                	jne    0x18001fb94
```

### Line 34739 (Address `0x180074080`)
```assembly
   18001fb39:	bb 64 00 00 00       	mov    $0x64,%ebx
   18001fb3e:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18001fb43:	75 4f                	jne    0x18001fb94
   18001fb45:	66 66 66 0f 1f 84 00 	data16 data16 nopw 0x0(%rax,%rax,1)
   18001fb4c:	00 00 00 00 
   18001fb50:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fb55:	ba 26 10 00 00       	mov    $0x1026,%edx
   18001fb5a:	48 8b ce             	mov    %rsi,%rcx
   18001fb5d:	ff cb                	dec    %ebx
   18001fb5f:	e8 8c ef ff ff       	call   0x18001eaf0
   18001fb64:	85 c0                	test   %eax,%eax
   18001fb66:	0f 85 ad 00 00 00    	jne    0x18001fc19
   18001fb6c:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001fb70:	0f 84 b9 00 00 00    	je     0x18001fc2f
   18001fb76:	8b cd                	mov    %ebp,%ecx
   18001fb78:	ff 15 02 45 05 00    	call   *0x54502(%rip)        # 0x180074080
   18001fb7e:	85 db                	test   %ebx,%ebx
   18001fb80:	75 ce                	jne    0x18001fb50
   18001fb82:	41 b8 26 10 00 00    	mov    $0x1026,%r8d
   18001fb88:	48 8d 15 51 e0 07 00 	lea    0x7e051(%rip),%rdx        # 0x18009dbe0
```

### Line 34758 (Address `0x180074080`)
```assembly
   18001fb88:	48 8d 15 51 e0 07 00 	lea    0x7e051(%rip),%rdx        # 0x18009dbe0
   18001fb8f:	e9 8f 00 00 00       	jmp    0x18001fc23
   18001fb94:	3d 20 51 00 00       	cmp    $0x5120,%eax
   18001fb99:	75 45                	jne    0x18001fbe0
   18001fb9b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   18001fba0:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fba5:	ba 18 c5 00 00       	mov    $0xc518,%edx
   18001fbaa:	48 8b ce             	mov    %rsi,%rcx
   18001fbad:	ff cb                	dec    %ebx
   18001fbaf:	e8 3c ef ff ff       	call   0x18001eaf0
   18001fbb4:	85 c0                	test   %eax,%eax
   18001fbb6:	75 61                	jne    0x18001fc19
   18001fbb8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001fbbc:	74 71                	je     0x18001fc2f
   18001fbbe:	8b cd                	mov    %ebp,%ecx
   18001fbc0:	ff 15 ba 44 05 00    	call   *0x544ba(%rip)        # 0x180074080
   18001fbc6:	85 db                	test   %ebx,%ebx
   18001fbc8:	75 d6                	jne    0x18001fba0
   18001fbca:	41 b8 18 c5 00 00    	mov    $0xc518,%r8d
   18001fbd0:	48 8d 15 09 e0 07 00 	lea    0x7e009(%rip),%rdx        # 0x18009dbe0
```

### Line 34775 (Address `0x180074080`)
```assembly
   18001fbc8:	75 d6                	jne    0x18001fba0
   18001fbca:	41 b8 18 c5 00 00    	mov    $0xc518,%r8d
   18001fbd0:	48 8d 15 09 e0 07 00 	lea    0x7e009(%rip),%rdx        # 0x18009dbe0
   18001fbd7:	eb 4a                	jmp    0x18001fc23
   18001fbd9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   18001fbe0:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fbe5:	ba 58 c5 00 00       	mov    $0xc558,%edx
   18001fbea:	48 8b ce             	mov    %rsi,%rcx
   18001fbed:	ff cb                	dec    %ebx
   18001fbef:	e8 fc ee ff ff       	call   0x18001eaf0
   18001fbf4:	85 c0                	test   %eax,%eax
   18001fbf6:	75 21                	jne    0x18001fc19
   18001fbf8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001fbfc:	74 31                	je     0x18001fc2f
   18001fbfe:	8b cd                	mov    %ebp,%ecx
   18001fc00:	ff 15 7a 44 05 00    	call   *0x5447a(%rip)        # 0x180074080
   18001fc06:	85 db                	test   %ebx,%ebx
   18001fc08:	75 d6                	jne    0x18001fbe0
   18001fc0a:	41 b8 58 c5 00 00    	mov    $0xc558,%r8d
   18001fc10:	48 8d 15 c9 df 07 00 	lea    0x7dfc9(%rip),%rdx        # 0x18009dbe0
```

### Line 34924 (Address `0x180074080`)
```assembly
   18001fdf9:	8b 86 70 05 00 00    	mov    0x570(%rsi),%eax
   18001fdff:	85 c0                	test   %eax,%eax
   18001fe01:	7e 08                	jle    0x18001fe0b
   18001fe03:	ff c8                	dec    %eax
   18001fe05:	89 86 70 05 00 00    	mov    %eax,0x570(%rsi)
   18001fe0b:	48 8b 0d f6 87 08 00 	mov    0x887f6(%rip),%rcx        # 0x1800a8608
   18001fe12:	48 8d 15 d7 db 07 00 	lea    0x7dbd7(%rip),%rdx        # 0x18009d9f0
   18001fe19:	41 0f b6 c7          	movzbl %r15b,%eax
   18001fe1d:	45 8b ce             	mov    %r14d,%r9d
   18001fe20:	c7 44 24 28 00 00 00 	movl   $0x0,0x28(%rsp)
   18001fe27:	00 
   18001fe28:	44 8b c5             	mov    %ebp,%r8d
   18001fe2b:	89 44 24 20          	mov    %eax,0x20(%rsp)
   18001fe2f:	e8 5c 64 ff ff       	call   0x180016290
   18001fe34:	b9 0a 00 00 00       	mov    $0xa,%ecx
   18001fe39:	ff 15 41 42 05 00    	call   *0x54241(%rip)        # 0x180074080
   18001fe3f:	8b 46 28             	mov    0x28(%rsi),%eax
   18001fe42:	bb 64 00 00 00       	mov    $0x64,%ebx
   18001fe47:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18001fe4c:	75 47                	jne    0x18001fe95
```

### Line 34940 (Address `0x180074080`)
```assembly
   18001fe3f:	8b 46 28             	mov    0x28(%rsi),%eax
   18001fe42:	bb 64 00 00 00       	mov    $0x64,%ebx
   18001fe47:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18001fe4c:	75 47                	jne    0x18001fe95
   18001fe4e:	66 90                	xchg   %ax,%ax
   18001fe50:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fe55:	ba 23 11 00 00       	mov    $0x1123,%edx
   18001fe5a:	48 8b ce             	mov    %rsi,%rcx
   18001fe5d:	ff cb                	dec    %ebx
   18001fe5f:	e8 8c ec ff ff       	call   0x18001eaf0
   18001fe64:	85 c0                	test   %eax,%eax
   18001fe66:	0f 85 ae 00 00 00    	jne    0x18001ff1a
   18001fe6c:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001fe70:	0f 84 ba 00 00 00    	je     0x18001ff30
   18001fe76:	41 8b cc             	mov    %r12d,%ecx
   18001fe79:	ff 15 01 42 05 00    	call   *0x54201(%rip)        # 0x180074080
   18001fe7f:	85 db                	test   %ebx,%ebx
   18001fe81:	75 cd                	jne    0x18001fe50
   18001fe83:	41 b8 23 11 00 00    	mov    $0x1123,%r8d
   18001fe89:	48 8d 15 50 dd 07 00 	lea    0x7dd50(%rip),%rdx        # 0x18009dbe0
```

### Line 34959 (Address `0x180074080`)
```assembly
   18001fe89:	48 8d 15 50 dd 07 00 	lea    0x7dd50(%rip),%rdx        # 0x18009dbe0
   18001fe90:	e9 8f 00 00 00       	jmp    0x18001ff24
   18001fe95:	3d 20 51 00 00       	cmp    $0x5120,%eax
   18001fe9a:	75 44                	jne    0x18001fee0
   18001fe9c:	0f 1f 40 00          	nopl   0x0(%rax)
   18001fea0:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fea5:	ba 16 c5 00 00       	mov    $0xc516,%edx
   18001feaa:	48 8b ce             	mov    %rsi,%rcx
   18001fead:	ff cb                	dec    %ebx
   18001feaf:	e8 3c ec ff ff       	call   0x18001eaf0
   18001feb4:	85 c0                	test   %eax,%eax
   18001feb6:	75 62                	jne    0x18001ff1a
   18001feb8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001febc:	74 72                	je     0x18001ff30
   18001febe:	41 8b cc             	mov    %r12d,%ecx
   18001fec1:	ff 15 b9 41 05 00    	call   *0x541b9(%rip)        # 0x180074080
   18001fec7:	85 db                	test   %ebx,%ebx
   18001fec9:	75 d5                	jne    0x18001fea0
   18001fecb:	41 b8 16 c5 00 00    	mov    $0xc516,%r8d
   18001fed1:	48 8d 15 08 dd 07 00 	lea    0x7dd08(%rip),%rdx        # 0x18009dbe0
```

### Line 34976 (Address `0x180074080`)
```assembly
   18001fec9:	75 d5                	jne    0x18001fea0
   18001fecb:	41 b8 16 c5 00 00    	mov    $0xc516,%r8d
   18001fed1:	48 8d 15 08 dd 07 00 	lea    0x7dd08(%rip),%rdx        # 0x18009dbe0
   18001fed8:	eb 4a                	jmp    0x18001ff24
   18001feda:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
   18001fee0:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   18001fee5:	ba 56 c5 00 00       	mov    $0xc556,%edx
   18001feea:	48 8b ce             	mov    %rsi,%rcx
   18001feed:	ff cb                	dec    %ebx
   18001feef:	e8 fc eb ff ff       	call   0x18001eaf0
   18001fef4:	85 c0                	test   %eax,%eax
   18001fef6:	75 22                	jne    0x18001ff1a
   18001fef8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18001fefc:	74 32                	je     0x18001ff30
   18001fefe:	41 8b cc             	mov    %r12d,%ecx
   18001ff01:	ff 15 79 41 05 00    	call   *0x54179(%rip)        # 0x180074080
   18001ff07:	85 db                	test   %ebx,%ebx
   18001ff09:	75 d5                	jne    0x18001fee0
   18001ff0b:	41 b8 56 c5 00 00    	mov    $0xc556,%r8d
   18001ff11:	48 8d 15 c8 dc 07 00 	lea    0x7dcc8(%rip),%rdx        # 0x18009dbe0
```

### Line 35116 (Address `0x180074080`)
```assembly
   1800200e3:	8d 83 18 fc ff ff    	lea    -0x3e8(%rbx),%eax
   1800200e9:	e9 34 01 00 00       	jmp    0x180020222
   1800200ee:	8b 86 70 05 00 00    	mov    0x570(%rsi),%eax
   1800200f4:	85 c0                	test   %eax,%eax
   1800200f6:	7e 08                	jle    0x180020100
   1800200f8:	ff c8                	dec    %eax
   1800200fa:	89 86 70 05 00 00    	mov    %eax,0x570(%rsi)
   180020100:	48 8b 0d 01 85 08 00 	mov    0x88501(%rip),%rcx        # 0x1800a8608
   180020107:	48 8d 15 52 d9 07 00 	lea    0x7d952(%rip),%rdx        # 0x18009da60
   18002010e:	45 0f b6 c7          	movzbl %r15b,%r8d
   180020112:	45 33 c9             	xor    %r9d,%r9d
   180020115:	44 89 74 24 28       	mov    %r14d,0x28(%rsp)
   18002011a:	89 6c 24 20          	mov    %ebp,0x20(%rsp)
   18002011e:	e8 6d 61 ff ff       	call   0x180016290
   180020123:	b9 14 00 00 00       	mov    $0x14,%ecx
   180020128:	ff 15 52 3f 05 00    	call   *0x53f52(%rip)        # 0x180074080
   18002012e:	8b 46 28             	mov    0x28(%rsi),%eax
   180020131:	bb 64 00 00 00       	mov    $0x64,%ebx
   180020136:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18002013b:	75 48                	jne    0x180020185
```

### Line 35132 (Address `0x180074080`)
```assembly
   18002012e:	8b 46 28             	mov    0x28(%rsi),%eax
   180020131:	bb 64 00 00 00       	mov    $0x64,%ebx
   180020136:	3d 32 91 00 00       	cmp    $0x9132,%eax
   18002013b:	75 48                	jne    0x180020185
   18002013d:	0f 1f 00             	nopl   (%rax)
   180020140:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020145:	ba 25 11 00 00       	mov    $0x1125,%edx
   18002014a:	48 8b ce             	mov    %rsi,%rcx
   18002014d:	ff cb                	dec    %ebx
   18002014f:	e8 9c e9 ff ff       	call   0x18001eaf0
   180020154:	85 c0                	test   %eax,%eax
   180020156:	0f 85 ae 00 00 00    	jne    0x18002020a
   18002015c:	38 44 24 40          	cmp    %al,0x40(%rsp)
   180020160:	0f 84 ba 00 00 00    	je     0x180020220
   180020166:	41 8b cc             	mov    %r12d,%ecx
   180020169:	ff 15 11 3f 05 00    	call   *0x53f11(%rip)        # 0x180074080
   18002016f:	85 db                	test   %ebx,%ebx
   180020171:	75 cd                	jne    0x180020140
   180020173:	41 b8 25 11 00 00    	mov    $0x1125,%r8d
   180020179:	48 8d 15 60 da 07 00 	lea    0x7da60(%rip),%rdx        # 0x18009dbe0
```

### Line 35151 (Address `0x180074080`)
```assembly
   180020179:	48 8d 15 60 da 07 00 	lea    0x7da60(%rip),%rdx        # 0x18009dbe0
   180020180:	e9 8f 00 00 00       	jmp    0x180020214
   180020185:	3d 20 51 00 00       	cmp    $0x5120,%eax
   18002018a:	75 44                	jne    0x1800201d0
   18002018c:	0f 1f 40 00          	nopl   0x0(%rax)
   180020190:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020195:	ba 17 c5 00 00       	mov    $0xc517,%edx
   18002019a:	48 8b ce             	mov    %rsi,%rcx
   18002019d:	ff cb                	dec    %ebx
   18002019f:	e8 4c e9 ff ff       	call   0x18001eaf0
   1800201a4:	85 c0                	test   %eax,%eax
   1800201a6:	75 62                	jne    0x18002020a
   1800201a8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   1800201ac:	74 72                	je     0x180020220
   1800201ae:	41 8b cc             	mov    %r12d,%ecx
   1800201b1:	ff 15 c9 3e 05 00    	call   *0x53ec9(%rip)        # 0x180074080
   1800201b7:	85 db                	test   %ebx,%ebx
   1800201b9:	75 d5                	jne    0x180020190
   1800201bb:	41 b8 17 c5 00 00    	mov    $0xc517,%r8d
   1800201c1:	48 8d 15 18 da 07 00 	lea    0x7da18(%rip),%rdx        # 0x18009dbe0
```

### Line 35168 (Address `0x180074080`)
```assembly
   1800201b9:	75 d5                	jne    0x180020190
   1800201bb:	41 b8 17 c5 00 00    	mov    $0xc517,%r8d
   1800201c1:	48 8d 15 18 da 07 00 	lea    0x7da18(%rip),%rdx        # 0x18009dbe0
   1800201c8:	eb 4a                	jmp    0x180020214
   1800201ca:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
   1800201d0:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   1800201d5:	ba 57 c5 00 00       	mov    $0xc557,%edx
   1800201da:	48 8b ce             	mov    %rsi,%rcx
   1800201dd:	ff cb                	dec    %ebx
   1800201df:	e8 0c e9 ff ff       	call   0x18001eaf0
   1800201e4:	85 c0                	test   %eax,%eax
   1800201e6:	75 22                	jne    0x18002020a
   1800201e8:	38 44 24 40          	cmp    %al,0x40(%rsp)
   1800201ec:	74 32                	je     0x180020220
   1800201ee:	41 8b cc             	mov    %r12d,%ecx
   1800201f1:	ff 15 89 3e 05 00    	call   *0x53e89(%rip)        # 0x180074080
   1800201f7:	85 db                	test   %ebx,%ebx
   1800201f9:	75 d5                	jne    0x1800201d0
   1800201fb:	41 b8 57 c5 00 00    	mov    $0xc557,%r8d
   180020201:	48 8d 15 d8 d9 07 00 	lea    0x7d9d8(%rip),%rdx        # 0x18009dbe0
```

### Line 35289 (Address `0x180074080`)
```assembly
   180020386:	e8 25 d4 ff ff       	call   0x18001d7b0
   18002038b:	8d 83 18 fc ff ff    	lea    -0x3e8(%rbx),%eax
   180020391:	e9 2c 01 00 00       	jmp    0x1800204c2
   180020396:	8b 86 70 05 00 00    	mov    0x570(%rsi),%eax
   18002039c:	85 c0                	test   %eax,%eax
   18002039e:	7e 08                	jle    0x1800203a8
   1800203a0:	ff c8                	dec    %eax
   1800203a2:	89 86 70 05 00 00    	mov    %eax,0x570(%rsi)
   1800203a8:	48 8b 0d 59 82 08 00 	mov    0x88259(%rip),%rcx        # 0x1800a8608
   1800203af:	48 8d 15 0a d7 07 00 	lea    0x7d70a(%rip),%rdx        # 0x18009dac0
   1800203b6:	40 84 ed             	test   %bpl,%bpl
   1800203b9:	75 07                	jne    0x1800203c2
   1800203bb:	48 8d 15 26 d7 07 00 	lea    0x7d726(%rip),%rdx        # 0x18009dae8
   1800203c2:	e8 c9 5e ff ff       	call   0x180016290
   1800203c7:	b9 0a 00 00 00       	mov    $0xa,%ecx
   1800203cc:	ff 15 ae 3c 05 00    	call   *0x53cae(%rip)        # 0x180074080
   1800203d2:	8b 46 28             	mov    0x28(%rsi),%eax
   1800203d5:	bb 64 00 00 00       	mov    $0x64,%ebx
   1800203da:	3d 32 91 00 00       	cmp    $0x9132,%eax
   1800203df:	75 45                	jne    0x180020426
```

### Line 35304 (Address `0x180074080`)
```assembly
   1800203cc:	ff 15 ae 3c 05 00    	call   *0x53cae(%rip)        # 0x180074080
   1800203d2:	8b 46 28             	mov    0x28(%rsi),%eax
   1800203d5:	bb 64 00 00 00       	mov    $0x64,%ebx
   1800203da:	3d 32 91 00 00       	cmp    $0x9132,%eax
   1800203df:	75 45                	jne    0x180020426
   1800203e1:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   1800203e6:	ba 8d 11 00 00       	mov    $0x118d,%edx
   1800203eb:	48 8b ce             	mov    %rsi,%rcx
   1800203ee:	ff cb                	dec    %ebx
   1800203f0:	e8 fb e6 ff ff       	call   0x18001eaf0
   1800203f5:	85 c0                	test   %eax,%eax
   1800203f7:	0f 85 ad 00 00 00    	jne    0x1800204aa
   1800203fd:	38 44 24 40          	cmp    %al,0x40(%rsp)
   180020401:	0f 84 b9 00 00 00    	je     0x1800204c0
   180020407:	41 8b ce             	mov    %r14d,%ecx
   18002040a:	ff 15 70 3c 05 00    	call   *0x53c70(%rip)        # 0x180074080
   180020410:	85 db                	test   %ebx,%ebx
   180020412:	75 cd                	jne    0x1800203e1
   180020414:	41 b8 8d 11 00 00    	mov    $0x118d,%r8d
   18002041a:	48 8d 15 bf d7 07 00 	lea    0x7d7bf(%rip),%rdx        # 0x18009dbe0
```

### Line 35323 (Address `0x180074080`)
```assembly
   18002041a:	48 8d 15 bf d7 07 00 	lea    0x7d7bf(%rip),%rdx        # 0x18009dbe0
   180020421:	e9 8e 00 00 00       	jmp    0x1800204b4
   180020426:	3d 20 51 00 00       	cmp    $0x5120,%eax
   18002042b:	75 43                	jne    0x180020470
   18002042d:	0f 1f 00             	nopl   (%rax)
   180020430:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020435:	ba 15 c5 00 00       	mov    $0xc515,%edx
   18002043a:	48 8b ce             	mov    %rsi,%rcx
   18002043d:	ff cb                	dec    %ebx
   18002043f:	e8 ac e6 ff ff       	call   0x18001eaf0
   180020444:	85 c0                	test   %eax,%eax
   180020446:	75 62                	jne    0x1800204aa
   180020448:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18002044c:	74 72                	je     0x1800204c0
   18002044e:	41 8b ce             	mov    %r14d,%ecx
   180020451:	ff 15 29 3c 05 00    	call   *0x53c29(%rip)        # 0x180074080
   180020457:	85 db                	test   %ebx,%ebx
   180020459:	75 d5                	jne    0x180020430
   18002045b:	41 b8 15 c5 00 00    	mov    $0xc515,%r8d
   180020461:	48 8d 15 78 d7 07 00 	lea    0x7d778(%rip),%rdx        # 0x18009dbe0
```

### Line 35340 (Address `0x180074080`)
```assembly
   180020459:	75 d5                	jne    0x180020430
   18002045b:	41 b8 15 c5 00 00    	mov    $0xc515,%r8d
   180020461:	48 8d 15 78 d7 07 00 	lea    0x7d778(%rip),%rdx        # 0x18009dbe0
   180020468:	eb 4a                	jmp    0x1800204b4
   18002046a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
   180020470:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020475:	ba 55 c5 00 00       	mov    $0xc555,%edx
   18002047a:	48 8b ce             	mov    %rsi,%rcx
   18002047d:	ff cb                	dec    %ebx
   18002047f:	e8 6c e6 ff ff       	call   0x18001eaf0
   180020484:	85 c0                	test   %eax,%eax
   180020486:	75 22                	jne    0x1800204aa
   180020488:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18002048c:	74 32                	je     0x1800204c0
   18002048e:	41 8b ce             	mov    %r14d,%ecx
   180020491:	ff 15 e9 3b 05 00    	call   *0x53be9(%rip)        # 0x180074080
   180020497:	85 db                	test   %ebx,%ebx
   180020499:	75 d5                	jne    0x180020470
   18002049b:	41 b8 55 c5 00 00    	mov    $0xc555,%r8d
   1800204a1:	48 8d 15 38 d7 07 00 	lea    0x7d738(%rip),%rdx        # 0x18009dbe0
```

### Line 35461 (Address `0x180074080`)
```assembly
   180020615:	ba 04 00 00 00       	mov    $0x4,%edx
   18002061a:	48 8b cf             	mov    %rdi,%rcx
   18002061d:	e8 8e d1 ff ff       	call   0x18001d7b0
   180020622:	8d 86 18 fc ff ff    	lea    -0x3e8(%rsi),%eax
   180020628:	e9 84 00 00 00       	jmp    0x1800206b1
   18002062d:	8b 87 70 05 00 00    	mov    0x570(%rdi),%eax
   180020633:	85 c0                	test   %eax,%eax
   180020635:	7e 08                	jle    0x18002063f
   180020637:	ff c8                	dec    %eax
   180020639:	89 87 70 05 00 00    	mov    %eax,0x570(%rdi)
   18002063f:	48 8b 0d c2 7f 08 00 	mov    0x87fc2(%rip),%rcx        # 0x1800a8608
   180020646:	48 8d 15 c3 d4 07 00 	lea    0x7d4c3(%rip),%rdx        # 0x18009db10
   18002064d:	e8 3e 5c ff ff       	call   0x180016290
   180020652:	bb 64 00 00 00       	mov    $0x64,%ebx
   180020657:	8b cb                	mov    %ebx,%ecx
   180020659:	ff 15 21 3a 05 00    	call   *0x53a21(%rip)        # 0x180074080
   18002065f:	90                   	nop
   180020660:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020665:	ba 54 c4 00 00       	mov    $0xc454,%edx
   18002066a:	48 8b cf             	mov    %rdi,%rcx
```

### Line 35473 (Address `0x180074080`)
```assembly
   18002064d:	e8 3e 5c ff ff       	call   0x180016290
   180020652:	bb 64 00 00 00       	mov    $0x64,%ebx
   180020657:	8b cb                	mov    %ebx,%ecx
   180020659:	ff 15 21 3a 05 00    	call   *0x53a21(%rip)        # 0x180074080
   18002065f:	90                   	nop
   180020660:	4c 8d 44 24 40       	lea    0x40(%rsp),%r8
   180020665:	ba 54 c4 00 00       	mov    $0xc454,%edx
   18002066a:	48 8b cf             	mov    %rdi,%rcx
   18002066d:	ff cb                	dec    %ebx
   18002066f:	e8 7c e4 ff ff       	call   0x18001eaf0
   180020674:	85 c0                	test   %eax,%eax
   180020676:	75 21                	jne    0x180020699
   180020678:	38 44 24 40          	cmp    %al,0x40(%rsp)
   18002067c:	74 31                	je     0x1800206af
   18002067e:	8b cd                	mov    %ebp,%ecx
   180020680:	ff 15 fa 39 05 00    	call   *0x539fa(%rip)        # 0x180074080
   180020686:	85 db                	test   %ebx,%ebx
   180020688:	75 d6                	jne    0x180020660
   18002068a:	41 b8 54 c4 00 00    	mov    $0xc454,%r8d
   180020690:	48 8d 15 49 d5 07 00 	lea    0x7d549(%rip),%rdx        # 0x18009dbe0
```

## `KERNEL32.dll!SuspendThread` (1 Call Sites)

### Line 23039 (Address `0x180074070`)
```assembly
   180015314:	49 8b 06             	mov    (%r14),%rax
   180015317:	49 8b ce             	mov    %r14,%rcx
   18001531a:	ff 50 08             	call   *0x8(%rax)
   18001531d:	48 81 c3 7c 02 00 00 	add    $0x27c,%rbx
   180015324:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
   180015329:	be 10 00 00 00       	mov    $0x10,%esi
   18001532e:	66 90                	xchg   %ax,%ax
   180015330:	80 7b fc 00          	cmpb   $0x0,-0x4(%rbx)
   180015334:	74 2d                	je     0x180015363
   180015336:	44 8b 03             	mov    (%rbx),%r8d
   180015339:	48 8d 15 b0 5a 08 00 	lea    0x85ab0(%rip),%rdx        # 0x18009adf0
   180015340:	48 8b 0d c1 32 09 00 	mov    0x932c1(%rip),%rcx        # 0x1800a8608
   180015347:	e8 44 0f 00 00       	call   0x180016290
   18001534c:	48 8b 7b 04          	mov    0x4(%rbx),%rdi
   180015350:	48 8b 4f 08          	mov    0x8(%rdi),%rcx
   180015354:	ff 15 16 ed 05 00    	call   *0x5ed16(%rip)        # 0x180074070
   18001535a:	83 f8 ff             	cmp    $0xffffffff,%eax
   18001535d:	0f 94 c0             	sete   %al
   180015360:	88 47 14             	mov    %al,0x14(%rdi)
   180015363:	48 83 c3 18          	add    $0x18,%rbx
```

## `KERNEL32.dll!SystemTimeToFileTime` (4 Call Sites)

### Line 23275 (Address `0x1800740b0`)
```assembly
   180015624:	4c 89 73 38          	mov    %r14,0x38(%rbx)
   180015628:	e8 83 16 00 00       	call   0x180016cb0
   18001562d:	48 89 43 30          	mov    %rax,0x30(%rbx)
   180015631:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   180015636:	4c 89 73 58          	mov    %r14,0x58(%rbx)
   18001563a:	48 b8 00 00 00 00 00 	movabs $0x4014000000000000,%rax
   180015641:	00 14 40 
   180015644:	48 89 43 60          	mov    %rax,0x60(%rbx)
   180015648:	33 c0                	xor    %eax,%eax
   18001564a:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001564f:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180015654:	4c 89 73 68          	mov    %r14,0x68(%rbx)
   180015658:	ff 15 4a ea 05 00    	call   *0x5ea4a(%rip)        # 0x1800740a8
   18001565e:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   180015663:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   180015668:	ff 15 42 ea 05 00    	call   *0x5ea42(%rip)        # 0x1800740b0
   18001566e:	48 8b 44 24 40       	mov    0x40(%rsp),%rax
   180015673:	48 8b d0             	mov    %rax,%rdx
   180015676:	8b c8                	mov    %eax,%ecx
   180015678:	48 c1 ea 20          	shr    $0x20,%rdx
```

### Line 23906 (Address `0x1800740b0`)
```assembly
   18001600f:	4c 8b 45 07          	mov    0x7(%rbp),%r8
   180016013:	48 8b 4d ff          	mov    -0x1(%rbp),%rcx
   180016017:	4c 2b c1             	sub    %rcx,%r8
   18001601a:	49 d1 f8             	sar    $1,%r8
   18001601d:	4d 03 c0             	add    %r8,%r8
   180016020:	48 8d 15 b5 49 08 00 	lea    0x849b5(%rip),%rdx        # 0x18009a9dc
   180016027:	e8 a4 09 04 00       	call   0x1800569d0
   18001602c:	90                   	nop
   18001602d:	33 c0                	xor    %eax,%eax
   18001602f:	48 89 45 e7          	mov    %rax,-0x19(%rbp)
   180016033:	48 89 45 ef          	mov    %rax,-0x11(%rbp)
   180016037:	48 8d 4d e7          	lea    -0x19(%rbp),%rcx
   18001603b:	ff 15 67 e0 05 00    	call   *0x5e067(%rip)        # 0x1800740a8
   180016041:	48 8d 55 d7          	lea    -0x29(%rbp),%rdx
   180016045:	48 8d 4d e7          	lea    -0x19(%rbp),%rcx
   180016049:	ff 15 61 e0 05 00    	call   *0x5e061(%rip)        # 0x1800740b0
   18001604f:	48 8b 45 d7          	mov    -0x29(%rbp),%rax
   180016053:	48 8b d0             	mov    %rax,%rdx
   180016056:	48 c1 ea 20          	shr    $0x20,%rdx
   18001605a:	48 c1 e2 20          	shl    $0x20,%rdx
```

### Line 29015 (Address `0x1800740b0`)
```assembly
   18001a62f:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
   18001a634:	4d 8b f8             	mov    %r8,%r15
   18001a637:	44 8b f2             	mov    %edx,%r14d
   18001a63a:	48 8b f1             	mov    %rcx,%rsi
   18001a63d:	ff 15 9d 9a 05 00    	call   *0x59a9d(%rip)        # 0x1800740e0
   18001a643:	8b f8                	mov    %eax,%edi
   18001a645:	ff 15 8d 9a 05 00    	call   *0x59a8d(%rip)        # 0x1800740d8
   18001a64b:	8b d8                	mov    %eax,%ebx
   18001a64d:	33 c0                	xor    %eax,%eax
   18001a64f:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001a654:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   18001a659:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18001a65e:	ff 15 44 9a 05 00    	call   *0x59a44(%rip)        # 0x1800740a8
   18001a664:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   18001a669:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18001a66e:	ff 15 3c 9a 05 00    	call   *0x59a3c(%rip)        # 0x1800740b0
   18001a674:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
   18001a679:	4c 8b c1             	mov    %rcx,%r8
   18001a67c:	49 c1 e8 20          	shr    $0x20,%r8
   18001a680:	49 c1 e0 20          	shl    $0x20,%r8
```

### Line 37214 (Address `0x1800740b0`)
```assembly
   180021e54:	48 33 c4             	xor    %rsp,%rax
   180021e57:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
   180021e5c:	49 8b f0             	mov    %r8,%rsi
   180021e5f:	4c 8b f1             	mov    %rcx,%r14
   180021e62:	ff 15 78 22 05 00    	call   *0x52278(%rip)        # 0x1800740e0
   180021e68:	8b f8                	mov    %eax,%edi
   180021e6a:	ff 15 68 22 05 00    	call   *0x52268(%rip)        # 0x1800740d8
   180021e70:	8b d8                	mov    %eax,%ebx
   180021e72:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180021e77:	33 c0                	xor    %eax,%eax
   180021e79:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   180021e7e:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   180021e83:	ff 15 1f 22 05 00    	call   *0x5221f(%rip)        # 0x1800740a8
   180021e89:	48 8d 54 24 30       	lea    0x30(%rsp),%rdx
   180021e8e:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180021e93:	ff 15 17 22 05 00    	call   *0x52217(%rip)        # 0x1800740b0
   180021e99:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
   180021e9e:	4c 8d 4c 24 38       	lea    0x38(%rsp),%r9
   180021ea3:	4c 8b c1             	mov    %rcx,%r8
   180021ea6:	8b d1                	mov    %ecx,%edx
```

## `KERNEL32.dll!TerminateProcess` (3 Call Sites)

### Line 97009 (Address `0x1800741f8`)
```assembly
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
   1800551af:	48 83 c4 28          	add    $0x28,%rsp
   1800551b3:	c3                   	ret
   1800551b4:	40 53                	rex push %rbx
   1800551b6:	48 83 ec 20          	sub    $0x20,%rsp
   1800551ba:	48 8b d9             	mov    %rcx,%rbx
   1800551bd:	33 c9                	xor    %ecx,%ecx
   1800551bf:	ff 15 2b f0 01 00    	call   *0x1f02b(%rip)        # 0x1800741f0
   1800551c5:	48 8b cb             	mov    %rbx,%rcx
   1800551c8:	ff 15 1a f0 01 00    	call   *0x1f01a(%rip)        # 0x1800741e8
   1800551ce:	ff 15 94 ef 01 00    	call   *0x1ef94(%rip)        # 0x180074168
   1800551d4:	48 8b c8             	mov    %rax,%rcx
   1800551d7:	ba 09 04 00 c0       	mov    $0xc0000409,%edx
   1800551dc:	48 83 c4 20          	add    $0x20,%rsp
   1800551e0:	5b                   	pop    %rbx
   1800551e1:	48 ff 25 10 f0 01 00 	rex.W jmp *0x1f010(%rip)        # 0x1800741f8
   1800551e8:	48 89 4c 24 08       	mov    %rcx,0x8(%rsp)
   1800551ed:	48 83 ec 38          	sub    $0x38,%rsp
   1800551f1:	b9 17 00 00 00       	mov    $0x17,%ecx
   1800551f6:	e8 8a d1 01 00       	call   0x180072385
```

### Line 107542 (Address `0x1800741f8`)
```assembly
   18005de34:	48 83 ec 28          	sub    $0x28,%rsp
   18005de38:	b9 17 00 00 00       	mov    $0x17,%ecx
   18005de3d:	ff 15 bd 63 01 00    	call   *0x163bd(%rip)        # 0x180074200
   18005de43:	85 c0                	test   %eax,%eax
   18005de45:	74 07                	je     0x18005de4e
   18005de47:	b9 05 00 00 00       	mov    $0x5,%ecx
   18005de4c:	cd 29                	int    $0x29
   18005de4e:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   18005de54:	ba 17 04 00 c0       	mov    $0xc0000417,%edx
   18005de59:	41 8d 48 01          	lea    0x1(%r8),%ecx
   18005de5d:	e8 6e fd ff ff       	call   0x18005dbd0
   18005de62:	ff 15 00 63 01 00    	call   *0x16300(%rip)        # 0x180074168
   18005de68:	48 8b c8             	mov    %rax,%rcx
   18005de6b:	ba 17 04 00 c0       	mov    $0xc0000417,%edx
   18005de70:	48 83 c4 28          	add    $0x28,%rsp
   18005de74:	48 ff 25 7d 63 01 00 	rex.W jmp *0x1637d(%rip)        # 0x1800741f8
   18005de7b:	cc                   	int3
   18005de7c:	f6 c1 04             	test   $0x4,%cl
   18005de7f:	75 19                	jne    0x18005de9a
   18005de81:	f6 c1 01             	test   $0x1,%cl
```

### Line 109514 (Address `0x1800741f8`)
```assembly
   18005f8ac:	40 53                	rex push %rbx
   18005f8ae:	48 83 ec 20          	sub    $0x20,%rsp
   18005f8b2:	8b d9                	mov    %ecx,%ebx
   18005f8b4:	e8 6b a7 00 00       	call   0x18006a024
   18005f8b9:	83 f8 01             	cmp    $0x1,%eax
   18005f8bc:	74 28                	je     0x18005f8e6
   18005f8be:	65 48 8b 04 25 60 00 	mov    %gs:0x60,%rax
   18005f8c5:	00 00 
   18005f8c7:	8b 90 bc 00 00 00    	mov    0xbc(%rax),%edx
   18005f8cd:	c1 ea 08             	shr    $0x8,%edx
   18005f8d0:	f6 c2 01             	test   $0x1,%dl
   18005f8d3:	75 11                	jne    0x18005f8e6
   18005f8d5:	ff 15 8d 48 01 00    	call   *0x1488d(%rip)        # 0x180074168
   18005f8db:	48 8b c8             	mov    %rax,%rcx
   18005f8de:	8b d3                	mov    %ebx,%edx
   18005f8e0:	ff 15 12 49 01 00    	call   *0x14912(%rip)        # 0x1800741f8
   18005f8e6:	8b cb                	mov    %ebx,%ecx
   18005f8e8:	e8 0b 00 00 00       	call   0x18005f8f8
   18005f8ed:	8b cb                	mov    %ebx,%ecx
   18005f8ef:	ff 15 b3 49 01 00    	call   *0x149b3(%rip)        # 0x1800742a8
```

## `KERNEL32.dll!TlsAlloc` (2 Call Sites)

### Line 101651 (Address `0x180074258`)
```assembly
   180058f3e:	48 83 ec 20          	sub    $0x20,%rsp
   180058f42:	48 8b d9             	mov    %rcx,%rbx
   180058f45:	4c 8d 0d d4 96 03 00 	lea    0x396d4(%rip),%r9        # 0x180092620
   180058f4c:	33 c9                	xor    %ecx,%ecx
   180058f4e:	4c 8d 05 c3 96 03 00 	lea    0x396c3(%rip),%r8        # 0x180092618
   180058f55:	48 8d 15 c4 96 03 00 	lea    0x396c4(%rip),%rdx        # 0x180092620
   180058f5c:	e8 03 fe ff ff       	call   0x180058d64
   180058f61:	48 85 c0             	test   %rax,%rax
   180058f64:	74 0f                	je     0x180058f75
   180058f66:	48 8b cb             	mov    %rbx,%rcx
   180058f69:	48 83 c4 20          	add    $0x20,%rsp
   180058f6d:	5b                   	pop    %rbx
   180058f6e:	48 ff 25 fb b3 01 00 	rex.W jmp *0x1b3fb(%rip)        # 0x180074370
   180058f75:	48 83 c4 20          	add    $0x20,%rsp
   180058f79:	5b                   	pop    %rbx
   180058f7a:	48 ff 25 d7 b2 01 00 	rex.W jmp *0x1b2d7(%rip)        # 0x180074258
   180058f81:	cc                   	int3
   180058f82:	cc                   	int3
   180058f83:	cc                   	int3
   180058f84:	40 53                	rex push %rbx
```

### Line 122418 (Address `0x180074258`)
```assembly
   18006a4ae:	48 83 ec 20          	sub    $0x20,%rsp
   18006a4b2:	48 8b d9             	mov    %rcx,%rbx
   18006a4b5:	4c 8d 0d a4 b3 02 00 	lea    0x2b3a4(%rip),%r9        # 0x180095860
   18006a4bc:	b9 03 00 00 00       	mov    $0x3,%ecx
   18006a4c1:	4c 8d 05 90 b3 02 00 	lea    0x2b390(%rip),%r8        # 0x180095858
   18006a4c8:	48 8d 15 91 b3 02 00 	lea    0x2b391(%rip),%rdx        # 0x180095860
   18006a4cf:	e8 f8 fb ff ff       	call   0x18006a0cc
   18006a4d4:	48 85 c0             	test   %rax,%rax
   18006a4d7:	74 0f                	je     0x18006a4e8
   18006a4d9:	48 8b cb             	mov    %rbx,%rcx
   18006a4dc:	48 83 c4 20          	add    $0x20,%rsp
   18006a4e0:	5b                   	pop    %rbx
   18006a4e1:	48 ff 25 88 9e 00 00 	rex.W jmp *0x9e88(%rip)        # 0x180074370
   18006a4e8:	48 83 c4 20          	add    $0x20,%rsp
   18006a4ec:	5b                   	pop    %rbx
   18006a4ed:	48 ff 25 64 9d 00 00 	rex.W jmp *0x9d64(%rip)        # 0x180074258
   18006a4f4:	40 53                	rex push %rbx
   18006a4f6:	48 83 ec 20          	sub    $0x20,%rsp
   18006a4fa:	8b d9                	mov    %ecx,%ebx
   18006a4fc:	4c 8d 0d 75 b3 02 00 	lea    0x2b375(%rip),%r9        # 0x180095878
```

## `KERNEL32.dll!TlsFree` (2 Call Sites)

### Line 101671 (Address `0x180074270`)
```assembly
   180058f86:	48 83 ec 20          	sub    $0x20,%rsp
   180058f8a:	8b d9                	mov    %ecx,%ebx
   180058f8c:	4c 8d 0d a5 96 03 00 	lea    0x396a5(%rip),%r9        # 0x180092638
   180058f93:	b9 01 00 00 00       	mov    $0x1,%ecx
   180058f98:	4c 8d 05 91 96 03 00 	lea    0x39691(%rip),%r8        # 0x180092630
   180058f9f:	48 8d 15 92 96 03 00 	lea    0x39692(%rip),%rdx        # 0x180092638
   180058fa6:	e8 b9 fd ff ff       	call   0x180058d64
   180058fab:	8b cb                	mov    %ebx,%ecx
   180058fad:	48 85 c0             	test   %rax,%rax
   180058fb0:	74 0c                	je     0x180058fbe
   180058fb2:	48 83 c4 20          	add    $0x20,%rsp
   180058fb6:	5b                   	pop    %rbx
   180058fb7:	48 ff 25 b2 b3 01 00 	rex.W jmp *0x1b3b2(%rip)        # 0x180074370
   180058fbe:	48 83 c4 20          	add    $0x20,%rsp
   180058fc2:	5b                   	pop    %rbx
   180058fc3:	48 ff 25 a6 b2 01 00 	rex.W jmp *0x1b2a6(%rip)        # 0x180074270
   180058fca:	cc                   	int3
   180058fcb:	cc                   	int3
   180058fcc:	40 53                	rex push %rbx
   180058fce:	48 83 ec 20          	sub    $0x20,%rsp
```

### Line 122435 (Address `0x180074270`)
```assembly
   18006a4f6:	48 83 ec 20          	sub    $0x20,%rsp
   18006a4fa:	8b d9                	mov    %ecx,%ebx
   18006a4fc:	4c 8d 0d 75 b3 02 00 	lea    0x2b375(%rip),%r9        # 0x180095878
   18006a503:	b9 04 00 00 00       	mov    $0x4,%ecx
   18006a508:	4c 8d 05 61 b3 02 00 	lea    0x2b361(%rip),%r8        # 0x180095870
   18006a50f:	48 8d 15 62 b3 02 00 	lea    0x2b362(%rip),%rdx        # 0x180095878
   18006a516:	e8 b1 fb ff ff       	call   0x18006a0cc
   18006a51b:	8b cb                	mov    %ebx,%ecx
   18006a51d:	48 85 c0             	test   %rax,%rax
   18006a520:	74 0c                	je     0x18006a52e
   18006a522:	48 83 c4 20          	add    $0x20,%rsp
   18006a526:	5b                   	pop    %rbx
   18006a527:	48 ff 25 42 9e 00 00 	rex.W jmp *0x9e42(%rip)        # 0x180074370
   18006a52e:	48 83 c4 20          	add    $0x20,%rsp
   18006a532:	5b                   	pop    %rbx
   18006a533:	48 ff 25 36 9d 00 00 	rex.W jmp *0x9d36(%rip)        # 0x180074270
   18006a53a:	cc                   	int3
   18006a53b:	cc                   	int3
   18006a53c:	40 53                	rex push %rbx
   18006a53e:	48 83 ec 20          	sub    $0x20,%rsp
```

## `KERNEL32.dll!TlsGetValue` (2 Call Sites)

### Line 101690 (Address `0x180074260`)
```assembly
   180058fce:	48 83 ec 20          	sub    $0x20,%rsp
   180058fd2:	8b d9                	mov    %ecx,%ebx
   180058fd4:	4c 8d 0d 6d 96 03 00 	lea    0x3966d(%rip),%r9        # 0x180092648
   180058fdb:	b9 02 00 00 00       	mov    $0x2,%ecx
   180058fe0:	4c 8d 05 59 96 03 00 	lea    0x39659(%rip),%r8        # 0x180092640
   180058fe7:	48 8d 15 5a 96 03 00 	lea    0x3965a(%rip),%rdx        # 0x180092648
   180058fee:	e8 71 fd ff ff       	call   0x180058d64
   180058ff3:	8b cb                	mov    %ebx,%ecx
   180058ff5:	48 85 c0             	test   %rax,%rax
   180058ff8:	74 0c                	je     0x180059006
   180058ffa:	48 83 c4 20          	add    $0x20,%rsp
   180058ffe:	5b                   	pop    %rbx
   180058fff:	48 ff 25 6a b3 01 00 	rex.W jmp *0x1b36a(%rip)        # 0x180074370
   180059006:	48 83 c4 20          	add    $0x20,%rsp
   18005900a:	5b                   	pop    %rbx
   18005900b:	48 ff 25 4e b2 01 00 	rex.W jmp *0x1b24e(%rip)        # 0x180074260
   180059012:	cc                   	int3
   180059013:	cc                   	int3
   180059014:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   180059019:	57                   	push   %rdi
```

### Line 122454 (Address `0x180074260`)
```assembly
   18006a53e:	48 83 ec 20          	sub    $0x20,%rsp
   18006a542:	8b d9                	mov    %ecx,%ebx
   18006a544:	4c 8d 0d 3d b3 02 00 	lea    0x2b33d(%rip),%r9        # 0x180095888
   18006a54b:	b9 05 00 00 00       	mov    $0x5,%ecx
   18006a550:	4c 8d 05 29 b3 02 00 	lea    0x2b329(%rip),%r8        # 0x180095880
   18006a557:	48 8d 15 2a b3 02 00 	lea    0x2b32a(%rip),%rdx        # 0x180095888
   18006a55e:	e8 69 fb ff ff       	call   0x18006a0cc
   18006a563:	8b cb                	mov    %ebx,%ecx
   18006a565:	48 85 c0             	test   %rax,%rax
   18006a568:	74 0c                	je     0x18006a576
   18006a56a:	48 83 c4 20          	add    $0x20,%rsp
   18006a56e:	5b                   	pop    %rbx
   18006a56f:	48 ff 25 fa 9d 00 00 	rex.W jmp *0x9dfa(%rip)        # 0x180074370
   18006a576:	48 83 c4 20          	add    $0x20,%rsp
   18006a57a:	5b                   	pop    %rbx
   18006a57b:	48 ff 25 de 9c 00 00 	rex.W jmp *0x9cde(%rip)        # 0x180074260
   18006a582:	cc                   	int3
   18006a583:	cc                   	int3
   18006a584:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
   18006a589:	57                   	push   %rdi
```

## `KERNEL32.dll!TlsSetValue` (2 Call Sites)

### Line 101709 (Address `0x180074268`)
```assembly
   180059019:	57                   	push   %rdi
   18005901a:	48 83 ec 20          	sub    $0x20,%rsp
   18005901e:	48 8b da             	mov    %rdx,%rbx
   180059021:	4c 8d 0d 38 96 03 00 	lea    0x39638(%rip),%r9        # 0x180092660
   180059028:	8b f9                	mov    %ecx,%edi
   18005902a:	48 8d 15 2f 96 03 00 	lea    0x3962f(%rip),%rdx        # 0x180092660
   180059031:	b9 03 00 00 00       	mov    $0x3,%ecx
   180059036:	4c 8d 05 1b 96 03 00 	lea    0x3961b(%rip),%r8        # 0x180092658
   18005903d:	e8 22 fd ff ff       	call   0x180058d64
   180059042:	48 8b d3             	mov    %rbx,%rdx
   180059045:	8b cf                	mov    %edi,%ecx
   180059047:	48 85 c0             	test   %rax,%rax
   18005904a:	74 08                	je     0x180059054
   18005904c:	ff 15 1e b3 01 00    	call   *0x1b31e(%rip)        # 0x180074370
   180059052:	eb 06                	jmp    0x18005905a
   180059054:	ff 15 0e b2 01 00    	call   *0x1b20e(%rip)        # 0x180074268
   18005905a:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18005905f:	48 83 c4 20          	add    $0x20,%rsp
   180059063:	5f                   	pop    %rdi
   180059064:	c3                   	ret
```

### Line 122473 (Address `0x180074268`)
```assembly
   18006a589:	57                   	push   %rdi
   18006a58a:	48 83 ec 20          	sub    $0x20,%rsp
   18006a58e:	48 8b da             	mov    %rdx,%rbx
   18006a591:	4c 8d 0d 08 b3 02 00 	lea    0x2b308(%rip),%r9        # 0x1800958a0
   18006a598:	8b f9                	mov    %ecx,%edi
   18006a59a:	48 8d 15 ff b2 02 00 	lea    0x2b2ff(%rip),%rdx        # 0x1800958a0
   18006a5a1:	b9 06 00 00 00       	mov    $0x6,%ecx
   18006a5a6:	4c 8d 05 eb b2 02 00 	lea    0x2b2eb(%rip),%r8        # 0x180095898
   18006a5ad:	e8 1a fb ff ff       	call   0x18006a0cc
   18006a5b2:	48 8b d3             	mov    %rbx,%rdx
   18006a5b5:	8b cf                	mov    %edi,%ecx
   18006a5b7:	48 85 c0             	test   %rax,%rax
   18006a5ba:	74 08                	je     0x18006a5c4
   18006a5bc:	ff 15 ae 9d 00 00    	call   *0x9dae(%rip)        # 0x180074370
   18006a5c2:	eb 06                	jmp    0x18006a5ca
   18006a5c4:	ff 15 9e 9c 00 00    	call   *0x9c9e(%rip)        # 0x180074268
   18006a5ca:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18006a5cf:	48 83 c4 20          	add    $0x20,%rsp
   18006a5d3:	5f                   	pop    %rdi
   18006a5d4:	c3                   	ret
```

## `KERNEL32.dll!UnhandledExceptionFilter` (3 Call Sites)

### Line 97003 (Address `0x1800741e8`)
```assembly
   18005518c:	48 83 ec 28          	sub    $0x28,%rsp
   180055190:	48 8d 0d c1 21 05 00 	lea    0x521c1(%rip),%rcx        # 0x1800a7358
   180055197:	ff 15 33 ef 01 00    	call   *0x1ef33(%rip)        # 0x1800740d0
   18005519d:	48 8b 0d e4 21 05 00 	mov    0x521e4(%rip),%rcx        # 0x1800a7388
   1800551a4:	48 85 c9             	test   %rcx,%rcx
   1800551a7:	74 06                	je     0x1800551af
   1800551a9:	ff 15 d9 ee 01 00    	call   *0x1eed9(%rip)        # 0x180074088
   1800551af:	48 83 c4 28          	add    $0x28,%rsp
   1800551b3:	c3                   	ret
   1800551b4:	40 53                	rex push %rbx
   1800551b6:	48 83 ec 20          	sub    $0x20,%rsp
   1800551ba:	48 8b d9             	mov    %rcx,%rbx
   1800551bd:	33 c9                	xor    %ecx,%ecx
   1800551bf:	ff 15 2b f0 01 00    	call   *0x1f02b(%rip)        # 0x1800741f0
   1800551c5:	48 8b cb             	mov    %rbx,%rcx
   1800551c8:	ff 15 1a f0 01 00    	call   *0x1f01a(%rip)        # 0x1800741e8
   1800551ce:	ff 15 94 ef 01 00    	call   *0x1ef94(%rip)        # 0x180074168
   1800551d4:	48 8b c8             	mov    %rax,%rcx
   1800551d7:	ba 09 04 00 c0       	mov    $0xc0000409,%edx
   1800551dc:	48 83 c4 20          	add    $0x20,%rsp
```

### Line 97776 (Address `0x1800741e8`)
```assembly
   180055c72:	48 89 44 24 60       	mov    %rax,0x60(%rsp)
   180055c77:	c7 44 24 50 15 00 00 	movl   $0x40000015,0x50(%rsp)
   180055c7e:	40 
   180055c7f:	c7 44 24 54 01 00 00 	movl   $0x1,0x54(%rsp)
   180055c86:	00 
   180055c87:	ff 15 93 e5 01 00    	call   *0x1e593(%rip)        # 0x180074220
   180055c8d:	83 f8 01             	cmp    $0x1,%eax
   180055c90:	48 8d 44 24 50       	lea    0x50(%rsp),%rax
   180055c95:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   180055c9a:	48 8d 45 f0          	lea    -0x10(%rbp),%rax
   180055c9e:	0f 94 c3             	sete   %bl
   180055ca1:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   180055ca6:	33 c9                	xor    %ecx,%ecx
   180055ca8:	ff 15 42 e5 01 00    	call   *0x1e542(%rip)        # 0x1800741f0
   180055cae:	48 8d 4c 24 40       	lea    0x40(%rsp),%rcx
   180055cb3:	ff 15 2f e5 01 00    	call   *0x1e52f(%rip)        # 0x1800741e8
   180055cb9:	85 c0                	test   %eax,%eax
   180055cbb:	75 0c                	jne    0x180055cc9
   180055cbd:	84 db                	test   %bl,%bl
   180055cbf:	75 08                	jne    0x180055cc9
```

### Line 107428 (Address `0x1800741e8`)
```assembly
   18005dc9c:	ff 15 3e 65 01 00    	call   *0x1653e(%rip)        # 0x1800741e0
   18005dca2:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dca9:	48 89 85 08 01 00 00 	mov    %rax,0x108(%rbp)
   18005dcb0:	48 8d 85 08 05 00 00 	lea    0x508(%rbp),%rax
   18005dcb7:	48 83 c0 08          	add    $0x8,%rax
   18005dcbb:	89 74 24 70          	mov    %esi,0x70(%rsp)
   18005dcbf:	48 89 85 a8 00 00 00 	mov    %rax,0xa8(%rbp)
   18005dcc6:	48 8b 85 08 05 00 00 	mov    0x508(%rbp),%rax
   18005dccd:	48 89 45 80          	mov    %rax,-0x80(%rbp)
   18005dcd1:	89 7c 24 74          	mov    %edi,0x74(%rsp)
   18005dcd5:	ff 15 45 65 01 00    	call   *0x16545(%rip)        # 0x180074220
   18005dcdb:	33 c9                	xor    %ecx,%ecx
   18005dcdd:	8b f8                	mov    %eax,%edi
   18005dcdf:	ff 15 0b 65 01 00    	call   *0x1650b(%rip)        # 0x1800741f0
   18005dce5:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   18005dcea:	ff 15 f8 64 01 00    	call   *0x164f8(%rip)        # 0x1800741e8
   18005dcf0:	85 c0                	test   %eax,%eax
   18005dcf2:	75 10                	jne    0x18005dd04
   18005dcf4:	85 ff                	test   %edi,%edi
   18005dcf6:	75 0c                	jne    0x18005dd04
```

## `KERNEL32.dll!WaitForSingleObject` (3 Call Sites)

### Line 22119 (Address `0x180074068`)
```assembly
   180014714:	83 3d e5 3e 09 00 01 	cmpl   $0x1,0x93ee5(%rip)        # 0x1800a8600
   18001471b:	74 0a                	je     0x180014727
   18001471d:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014722:	48 83 c4 28          	add    $0x28,%rsp
   180014726:	c3                   	ret
   180014727:	48 8b 0d ba 3e 09 00 	mov    0x93eba(%rip),%rcx        # 0x1800a85e8
   18001472e:	48 85 c9             	test   %rcx,%rcx
   180014731:	74 43                	je     0x180014776
   180014733:	48 8b 01             	mov    (%rcx),%rax
   180014736:	ff 50 08             	call   *0x8(%rax)
   180014739:	48 8b 0d a8 3e 09 00 	mov    0x93ea8(%rip),%rcx        # 0x1800a85e8
   180014740:	80 79 14 00          	cmpb   $0x0,0x14(%rcx)
   180014744:	74 16                	je     0x18001475c
   180014746:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   18001474a:	ba ff ff ff ff       	mov    $0xffffffff,%edx
   18001474f:	ff 15 13 f9 05 00    	call   *0x5f913(%rip)        # 0x180074068
   180014755:	48 8b 0d 8c 3e 09 00 	mov    0x93e8c(%rip),%rcx        # 0x1800a85e8
   18001475c:	48 85 c9             	test   %rcx,%rcx
   18001475f:	74 0a                	je     0x18001476b
   180014761:	48 8b 01             	mov    (%rcx),%rax
```

### Line 26554 (Address `0x180074068`)
```assembly
   180018393:	48 89 5c 24 50       	mov    %rbx,0x50(%rsp)
   180018398:	48 89 6c 24 58       	mov    %rbp,0x58(%rsp)
   18001839d:	48 89 74 24 60       	mov    %rsi,0x60(%rsp)
   1800183a2:	48 89 7c 24 68       	mov    %rdi,0x68(%rsp)
   1800183a7:	48 8b f1             	mov    %rcx,%rsi
   1800183aa:	48 8d 05 37 28 08 00 	lea    0x82837(%rip),%rax        # 0x18009abe8
   1800183b1:	48 89 01             	mov    %rax,(%rcx)
   1800183b4:	c6 41 15 01          	movb   $0x1,0x15(%rcx)
   1800183b8:	48 8b 01             	mov    (%rcx),%rax
   1800183bb:	ff 50 10             	call   *0x10(%rax)
   1800183be:	90                   	nop
   1800183bf:	80 7e 14 00          	cmpb   $0x0,0x14(%rsi)
   1800183c3:	74 10                	je     0x1800183d5
   1800183c5:	ba ff ff ff ff       	mov    $0xffffffff,%edx
   1800183ca:	48 8b 4e 08          	mov    0x8(%rsi),%rcx
   1800183ce:	ff 15 94 bc 05 00    	call   *0x5bc94(%rip)        # 0x180074068
   1800183d4:	90                   	nop
   1800183d5:	48 c7 05 38 02 09 00 	movq   $0x0,0x90238(%rip)        # 0x1800a8618
   1800183dc:	00 00 00 00 
   1800183e0:	4c 8d be 10 02 00 00 	lea    0x210(%rsi),%r15
```

### Line 29819 (Address `0x180074068`)
```assembly
   18001b1c1:	ff ff 
   18001b1c3:	48 89 5c 24 50       	mov    %rbx,0x50(%rsp)
   18001b1c8:	48 89 6c 24 58       	mov    %rbp,0x58(%rsp)
   18001b1cd:	48 89 74 24 60       	mov    %rsi,0x60(%rsp)
   18001b1d2:	4c 8b f1             	mov    %rcx,%r14
   18001b1d5:	48 8d 05 54 17 08 00 	lea    0x81754(%rip),%rax        # 0x18009c930
   18001b1dc:	48 89 01             	mov    %rax,(%rcx)
   18001b1df:	c6 41 15 01          	movb   $0x1,0x15(%rcx)
   18001b1e3:	48 8b 01             	mov    (%rcx),%rax
   18001b1e6:	ff 50 10             	call   *0x10(%rax)
   18001b1e9:	90                   	nop
   18001b1ea:	41 80 7e 14 00       	cmpb   $0x0,0x14(%r14)
   18001b1ef:	74 10                	je     0x18001b201
   18001b1f1:	ba ff ff ff ff       	mov    $0xffffffff,%edx
   18001b1f6:	49 8b 4e 08          	mov    0x8(%r14),%rcx
   18001b1fa:	ff 15 68 8e 05 00    	call   *0x58e68(%rip)        # 0x180074068
   18001b200:	90                   	nop
   18001b201:	41 80 be a9 05 00 00 	cmpb   $0x0,0x5a9(%r14)
   18001b208:	00 
   18001b209:	74 37                	je     0x18001b242
```

## `KERNEL32.dll!WideCharToMultiByte` (1 Call Sites)

### Line 121430 (Address `0x1800742b0`)
```assembly
   180069759:	74 0f                	je     0x18006976a
   18006975b:	41 81 fa e9 fd 00 00 	cmp    $0xfde9,%r10d
   180069762:	74 06                	je     0x18006976a
   180069764:	0f ba f2 07          	btr    $0x7,%edx
   180069768:	eb 02                	jmp    0x18006976c
   18006976a:	8b d3                	mov    %ebx,%edx
   18006976c:	48 8b 4c 24 48       	mov    0x48(%rsp),%rcx
   180069771:	45 84 db             	test   %r11b,%r11b
   180069774:	48 8b 44 24 40       	mov    0x40(%rsp),%rax
   180069779:	48 0f 45 c3          	cmovne %rbx,%rax
   18006977d:	48 0f 45 cb          	cmovne %rbx,%rcx
   180069781:	48 89 4c 24 48       	mov    %rcx,0x48(%rsp)
   180069786:	41 8b ca             	mov    %r10d,%ecx
   180069789:	48 89 44 24 40       	mov    %rax,0x40(%rsp)
   18006978e:	5b                   	pop    %rbx
   18006978f:	48 ff 25 1a ab 00 00 	rex.W jmp *0xab1a(%rip)        # 0x1800742b0
   180069796:	cc                   	int3
   180069797:	cc                   	int3
   180069798:	40 53                	rex push %rbx
   18006979a:	48 83 ec 20          	sub    $0x20,%rsp
```

## `KERNEL32.dll!WriteConsoleW` (3 Call Sites)

### Line 109047 (Address `0x1800742a0`)
```assembly
   18005f2ab:	e8 a8 01 00 00       	call   0x18005f458
   18005f2b0:	33 ff                	xor    %edi,%edi
   18005f2b2:	85 c0                	test   %eax,%eax
   18005f2b4:	78 3b                	js     0x18005f2f1
   18005f2b6:	48 8d 4c 24 60       	lea    0x60(%rsp),%rcx
   18005f2bb:	48 83 c8 ff          	or     $0xffffffffffffffff,%rax
   18005f2bf:	48 ff c0             	inc    %rax
   18005f2c2:	66 39 3c 41          	cmp    %di,(%rcx,%rax,2)
   18005f2c6:	75 f7                	jne    0x18005f2bf
   18005f2c8:	4c 8d 4c 24 30       	lea    0x30(%rsp),%r9
   18005f2cd:	89 7c 24 30          	mov    %edi,0x30(%rsp)
   18005f2d1:	44 8b c0             	mov    %eax,%r8d
   18005f2d4:	48 89 7c 24 20       	mov    %rdi,0x20(%rsp)
   18005f2d9:	48 8d 54 24 60       	lea    0x60(%rsp),%rdx
   18005f2de:	48 8b cb             	mov    %rbx,%rcx
   18005f2e1:	ff 15 b9 4f 01 00    	call   *0x14fb9(%rip)        # 0x1800742a0
   18005f2e7:	85 c0                	test   %eax,%eax
   18005f2e9:	74 06                	je     0x18005f2f1
   18005f2eb:	e8 78 72 00 00       	call   0x180066568
   18005f2f0:	cc                   	int3
```

### Line 130906 (Address `0x1800742a0`)
```assembly
   180071a1b:	c3                   	ret
   180071a1c:	48 8b c4             	mov    %rsp,%rax
   180071a1f:	48 89 58 08          	mov    %rbx,0x8(%rax)
   180071a23:	48 89 68 10          	mov    %rbp,0x10(%rax)
   180071a27:	48 89 70 18          	mov    %rsi,0x18(%rax)
   180071a2b:	57                   	push   %rdi
   180071a2c:	48 83 ec 40          	sub    $0x40,%rsp
   180071a30:	48 83 60 d8 00       	andq   $0x0,-0x28(%rax)
   180071a35:	49 8b f8             	mov    %r8,%rdi
   180071a38:	4d 8b c8             	mov    %r8,%r9
   180071a3b:	8b f2                	mov    %edx,%esi
   180071a3d:	44 8b c2             	mov    %edx,%r8d
   180071a40:	48 8b e9             	mov    %rcx,%rbp
   180071a43:	48 8b d1             	mov    %rcx,%rdx
   180071a46:	48 8b 0d 13 53 03 00 	mov    0x35313(%rip),%rcx        # 0x1800a6d60
   180071a4d:	ff 15 4d 28 00 00    	call   *0x284d(%rip)        # 0x1800742a0
   180071a53:	8b d8                	mov    %eax,%ebx
   180071a55:	85 c0                	test   %eax,%eax
   180071a57:	75 6a                	jne    0x180071ac3
   180071a59:	ff 15 a9 26 00 00    	call   *0x26a9(%rip)        # 0x180074108
```

### Line 130931 (Address `0x1800742a0`)
```assembly
   180071a71:	ff 15 11 26 00 00    	call   *0x2611(%rip)        # 0x180074088
   180071a77:	48 83 64 24 30 00    	andq   $0x0,0x30(%rsp)
   180071a7d:	48 8d 0d 9c 75 02 00 	lea    0x2759c(%rip),%rcx        # 0x180099020
   180071a84:	83 64 24 28 00       	andl   $0x0,0x28(%rsp)
   180071a89:	41 b8 03 00 00 00    	mov    $0x3,%r8d
   180071a8f:	45 33 c9             	xor    %r9d,%r9d
   180071a92:	44 89 44 24 20       	mov    %r8d,0x20(%rsp)
   180071a97:	ba 00 00 00 40       	mov    $0x40000000,%edx
   180071a9c:	ff 15 5e 26 00 00    	call   *0x265e(%rip)        # 0x180074100
   180071aa2:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   180071aa8:	4c 8b cf             	mov    %rdi,%r9
   180071aab:	48 8b c8             	mov    %rax,%rcx
   180071aae:	48 89 05 ab 52 03 00 	mov    %rax,0x352ab(%rip)        # 0x1800a6d60
   180071ab5:	44 8b c6             	mov    %esi,%r8d
   180071ab8:	48 8b d5             	mov    %rbp,%rdx
   180071abb:	ff 15 df 27 00 00    	call   *0x27df(%rip)        # 0x1800742a0
   180071ac1:	8b d8                	mov    %eax,%ebx
   180071ac3:	48 8b 6c 24 58       	mov    0x58(%rsp),%rbp
   180071ac8:	8b c3                	mov    %ebx,%eax
   180071aca:	48 8b 5c 24 50       	mov    0x50(%rsp),%rbx
```

## `KERNEL32.dll!WriteFile` (7 Call Sites)

### Line 29362 (Address `0x1800740f0`)
```assembly
   18001aadd:	c3                   	ret
   18001aade:	cc                   	int3
   18001aadf:	cc                   	int3
   18001aae0:	4c 8b dc             	mov    %rsp,%r11
   18001aae3:	48 81 ec 98 00 00 00 	sub    $0x98,%rsp
   18001aaea:	49 c7 43 98 fe ff ff 	movq   $0xfffffffffffffffe,-0x68(%r11)
   18001aaf1:	ff 
   18001aaf2:	41 8b c0             	mov    %r8d,%eax
   18001aaf5:	4c 3b c0             	cmp    %rax,%r8
   18001aaf8:	75 69                	jne    0x18001ab63
   18001aafa:	33 c0                	xor    %eax,%eax
   18001aafc:	41 89 43 18          	mov    %eax,0x18(%r11)
   18001ab00:	49 89 43 88          	mov    %rax,-0x78(%r11)
   18001ab04:	4d 8d 4b 18          	lea    0x18(%r11),%r9
   18001ab08:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   18001ab0c:	ff 15 de 95 05 00    	call   *0x595de(%rip)        # 0x1800740f0
   18001ab12:	85 c0                	test   %eax,%eax
   18001ab14:	74 0f                	je     0x18001ab25
   18001ab16:	8b 84 24 b0 00 00 00 	mov    0xb0(%rsp),%eax
   18001ab1d:	48 81 c4 98 00 00 00 	add    $0x98,%rsp
```

### Line 123113 (Address `0x1800740f0`)
```assembly
   18006aebb:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   18006aec0:	45 8b cf             	mov    %r15d,%r9d
   18006aec3:	c7 44 24 28 05 00 00 	movl   $0x5,0x28(%rsp)
   18006aeca:	00 
   18006aecb:	33 d2                	xor    %edx,%edx
   18006aecd:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18006aed2:	e8 29 e8 ff ff       	call   0x180069700
   18006aed7:	8b f8                	mov    %eax,%edi
   18006aed9:	85 c0                	test   %eax,%eax
   18006aedb:	0f 84 c9 01 00 00    	je     0x18006b0aa
   18006aee1:	48 8b 4d bf          	mov    -0x41(%rbp),%rcx
   18006aee5:	4c 8d 4c 24 48       	lea    0x48(%rsp),%r9
   18006aeea:	44 8b c0             	mov    %eax,%r8d
   18006aeed:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   18006aef2:	48 8d 55 17          	lea    0x17(%rbp),%rdx
   18006aef6:	ff 15 f4 91 00 00    	call   *0x91f4(%rip)        # 0x1800740f0
   18006aefc:	45 33 d2             	xor    %r10d,%r10d
   18006aeff:	85 c0                	test   %eax,%eax
   18006af01:	0f 84 9a 01 00 00    	je     0x18006b0a1
   18006af07:	4c 8b 7d af          	mov    -0x51(%rbp),%r15
```

### Line 123133 (Address `0x1800740f0`)
```assembly
   18006af0b:	8b ce                	mov    %esi,%ecx
   18006af0d:	2b 4d e7             	sub    -0x19(%rbp),%ecx
   18006af10:	42 8d 1c 39          	lea    (%rcx,%r15,1),%ebx
   18006af14:	89 5d 9b             	mov    %ebx,-0x65(%rbp)
   18006af17:	39 7c 24 48          	cmp    %edi,0x48(%rsp)
   18006af1b:	0f 82 9a 00 00 00    	jb     0x18006afbb
   18006af21:	80 7c 24 40 0a       	cmpb   $0xa,0x40(%rsp)
   18006af26:	75 44                	jne    0x18006af6c
   18006af28:	48 8b 4d bf          	mov    -0x41(%rbp),%rcx
   18006af2c:	41 8d 42 0d          	lea    0xd(%r10),%eax
   18006af30:	4c 8d 4c 24 48       	lea    0x48(%rsp),%r9
   18006af35:	66 89 44 24 40       	mov    %ax,0x40(%rsp)
   18006af3a:	45 8d 42 01          	lea    0x1(%r10),%r8d
   18006af3e:	4c 89 54 24 20       	mov    %r10,0x20(%rsp)
   18006af43:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18006af48:	ff 15 a2 91 00 00    	call   *0x91a2(%rip)        # 0x1800740f0
   18006af4e:	45 33 d2             	xor    %r10d,%r10d
   18006af51:	85 c0                	test   %eax,%eax
   18006af53:	0f 84 36 01 00 00    	je     0x18006b08f
   18006af59:	83 7c 24 48 01       	cmpl   $0x1,0x48(%rsp)
```

### Line 123289 (Address `0x1800740f0`)
```assembly
   18006b132:	c6 03 0d             	movb   $0xd,(%rbx)
   18006b135:	48 ff c3             	inc    %rbx
   18006b138:	88 03                	mov    %al,(%rbx)
   18006b13a:	48 ff c3             	inc    %rbx
   18006b13d:	48 8d 84 24 3f 14 00 	lea    0x143f(%rsp),%rax
   18006b144:	00 
   18006b145:	48 3b d8             	cmp    %rax,%rbx
   18006b148:	72 d7                	jb     0x18006b121
   18006b14a:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   18006b150:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18006b155:	2b d8                	sub    %eax,%ebx
   18006b157:	4c 8d 4c 24 30       	lea    0x30(%rsp),%r9
   18006b15c:	44 8b c3             	mov    %ebx,%r8d
   18006b15f:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18006b164:	49 8b ce             	mov    %r14,%rcx
   18006b167:	ff 15 83 8f 00 00    	call   *0x8f83(%rip)        # 0x1800740f0
   18006b16d:	85 c0                	test   %eax,%eax
   18006b16f:	74 12                	je     0x18006b183
   18006b171:	8b 44 24 30          	mov    0x30(%rsp),%eax
   18006b175:	01 47 04             	add    %eax,0x4(%rdi)
```

### Line 123372 (Address `0x1800740f0`)
```assembly
   18006b24b:	66 89 03             	mov    %ax,(%rbx)
   18006b24e:	48 83 c3 02          	add    $0x2,%rbx
   18006b252:	48 8d 84 24 3e 14 00 	lea    0x143e(%rsp),%rax
   18006b259:	00 
   18006b25a:	48 3b d8             	cmp    %rax,%rbx
   18006b25d:	72 ca                	jb     0x18006b229
   18006b25f:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   18006b265:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18006b26a:	48 2b d8             	sub    %rax,%rbx
   18006b26d:	4c 8d 4c 24 30       	lea    0x30(%rsp),%r9
   18006b272:	48 d1 fb             	sar    $1,%rbx
   18006b275:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
   18006b27a:	03 db                	add    %ebx,%ebx
   18006b27c:	49 8b ce             	mov    %r14,%rcx
   18006b27f:	44 8b c3             	mov    %ebx,%r8d
   18006b282:	ff 15 68 8e 00 00    	call   *0x8e68(%rip)        # 0x1800740f0
   18006b288:	85 c0                	test   %eax,%eax
   18006b28a:	74 12                	je     0x18006b29e
   18006b28c:	8b 44 24 30          	mov    0x30(%rsp),%eax
   18006b290:	01 47 04             	add    %eax,0x4(%rdi)
```

### Line 123479 (Address `0x1800740f0`)
```assembly
   18006b3be:	8b e8                	mov    %eax,%ebp
   18006b3c0:	85 c0                	test   %eax,%eax
   18006b3c2:	74 49                	je     0x18006b40d
   18006b3c4:	33 f6                	xor    %esi,%esi
   18006b3c6:	85 c0                	test   %eax,%eax
   18006b3c8:	74 33                	je     0x18006b3fd
   18006b3ca:	48 83 64 24 20 00    	andq   $0x0,0x20(%rsp)
   18006b3d0:	48 8d 94 24 00 07 00 	lea    0x700(%rsp),%rdx
   18006b3d7:	00 
   18006b3d8:	8b ce                	mov    %esi,%ecx
   18006b3da:	4c 8d 4c 24 40       	lea    0x40(%rsp),%r9
   18006b3df:	44 8b c5             	mov    %ebp,%r8d
   18006b3e2:	48 03 d1             	add    %rcx,%rdx
   18006b3e5:	49 8b cc             	mov    %r12,%rcx
   18006b3e8:	44 2b c6             	sub    %esi,%r8d
   18006b3eb:	ff 15 ff 8c 00 00    	call   *0x8cff(%rip)        # 0x1800740f0
   18006b3f1:	85 c0                	test   %eax,%eax
   18006b3f3:	74 18                	je     0x18006b40d
   18006b3f5:	03 74 24 40          	add    0x40(%rsp),%esi
   18006b3f9:	3b f5                	cmp    %ebp,%esi
```

### Line 123730 (Address `0x1800740f0`)
```assembly
   18006b729:	eb a7                	jmp    0x18006b6d2
   18006b72b:	45 8b ce             	mov    %r14d,%r9d
   18006b72e:	48 8d 4d d0          	lea    -0x30(%rbp),%rcx
   18006b732:	4c 8b c7             	mov    %rdi,%r8
   18006b735:	41 8b d4             	mov    %r12d,%edx
   18006b738:	e8 77 f9 ff ff       	call   0x18006b0b4
   18006b73d:	eb 93                	jmp    0x18006b6d2
   18006b73f:	4a 8b 4c f9 28       	mov    0x28(%rcx,%r15,8),%rcx
   18006b744:	4c 8d 4d d4          	lea    -0x2c(%rbp),%r9
   18006b748:	33 c0                	xor    %eax,%eax
   18006b74a:	45 8b c6             	mov    %r14d,%r8d
   18006b74d:	48 21 44 24 20       	and    %rax,0x20(%rsp)
   18006b752:	48 8b d7             	mov    %rdi,%rdx
   18006b755:	48 89 45 d0          	mov    %rax,-0x30(%rbp)
   18006b759:	89 45 d8             	mov    %eax,-0x28(%rbp)
   18006b75c:	ff 15 8e 89 00 00    	call   *0x898e(%rip)        # 0x1800740f0
   18006b762:	85 c0                	test   %eax,%eax
   18006b764:	75 09                	jne    0x18006b76f
   18006b766:	ff 15 9c 89 00 00    	call   *0x899c(%rip)        # 0x180074108
   18006b76c:	89 45 d0             	mov    %eax,-0x30(%rbp)
```

## `SETUPAPI.dll!SetupDiDestroyDeviceInfoList` (1 Call Sites)

### Line 29522 (Address `0x1800742e0`)
```assembly
   18001ad4f:	4c 8b c3             	mov    %rbx,%r8
   18001ad52:	33 d2                	xor    %edx,%edx
   18001ad54:	48 8b c8             	mov    %rax,%rcx
   18001ad57:	ff 15 bb 93 05 00    	call   *0x593bb(%rip)        # 0x180074118
   18001ad5d:	eb 1c                	jmp    0x18001ad7b
   18001ad5f:	ff 15 a3 93 05 00    	call   *0x593a3(%rip)        # 0x180074108
   18001ad65:	48 8b 0d 9c d8 08 00 	mov    0x8d89c(%rip),%rcx        # 0x1800a8608
   18001ad6c:	48 8d 15 0d 17 08 00 	lea    0x8170d(%rip),%rdx        # 0x18009c480
   18001ad73:	44 8b c0             	mov    %eax,%r8d
   18001ad76:	e8 15 b5 ff ff       	call   0x180016290
   18001ad7b:	48 8b 9c 24 80 00 00 	mov    0x80(%rsp),%rbx
   18001ad82:	00 
   18001ad83:	4c 8b b4 24 90 00 00 	mov    0x90(%rsp),%r14
   18001ad8a:	00 
   18001ad8b:	48 8b cd             	mov    %rbp,%rcx
   18001ad8e:	ff 15 4c 95 05 00    	call   *0x5954c(%rip)        # 0x1800742e0
   18001ad94:	40 0f b6 c6          	movzbl %sil,%eax
   18001ad98:	48 8b 4c 24 58       	mov    0x58(%rsp),%rcx
   18001ad9d:	48 33 cc             	xor    %rsp,%rcx
   18001ada0:	e8 7b 9e 03 00       	call   0x180054c20
```

## `SETUPAPI.dll!SetupDiEnumDeviceInterfaces` (1 Call Sites)

### Line 29429 (Address `0x1800742d8`)
```assembly
   18001abc6:	45 8d 4f 12          	lea    0x12(%r15),%r9d
   18001abca:	ff 15 18 97 05 00    	call   *0x59718(%rip)        # 0x1800742e8
   18001abd0:	48 8b e8             	mov    %rax,%rbp
   18001abd3:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18001abd7:	75 07                	jne    0x18001abe0
   18001abd9:	32 c0                	xor    %al,%al
   18001abdb:	e9 b8 01 00 00       	jmp    0x18001ad98
   18001abe0:	48 8d 44 24 38       	lea    0x38(%rsp),%rax
   18001abe5:	c7 44 24 38 20 00 00 	movl   $0x20,0x38(%rsp)
   18001abec:	00 
   18001abed:	45 33 c9             	xor    %r9d,%r9d
   18001abf0:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001abf5:	4c 8d 05 84 c1 08 00 	lea    0x8c184(%rip),%r8        # 0x1800a6d80
   18001abfc:	33 d2                	xor    %edx,%edx
   18001abfe:	48 8b cd             	mov    %rbp,%rcx
   18001ac01:	ff 15 d1 96 05 00    	call   *0x596d1(%rip)        # 0x1800742d8
   18001ac07:	85 c0                	test   %eax,%eax
   18001ac09:	0f 84 7c 01 00 00    	je     0x18001ad8b
   18001ac0f:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001ac14:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
```

## `SETUPAPI.dll!SetupDiGetClassDevsW` (1 Call Sites)

### Line 29415 (Address `0x1800742e8`)
```assembly
   18001ab95:	56                   	push   %rsi
   18001ab96:	57                   	push   %rdi
   18001ab97:	41 57                	push   %r15
   18001ab99:	48 83 ec 60          	sub    $0x60,%rsp
   18001ab9d:	48 8b 05 bc b7 08 00 	mov    0x8b7bc(%rip),%rax        # 0x1800a6360
   18001aba4:	48 33 c4             	xor    %rsp,%rax
   18001aba7:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
   18001abac:	45 33 ff             	xor    %r15d,%r15d
   18001abaf:	48 8d 0d ca c1 08 00 	lea    0x8c1ca(%rip),%rcx        # 0x1800a6d80
   18001abb6:	48 8b fa             	mov    %rdx,%rdi
   18001abb9:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001abbe:	45 33 c0             	xor    %r8d,%r8d
   18001abc1:	33 d2                	xor    %edx,%edx
   18001abc3:	40 32 f6             	xor    %sil,%sil
   18001abc6:	45 8d 4f 12          	lea    0x12(%r15),%r9d
   18001abca:	ff 15 18 97 05 00    	call   *0x59718(%rip)        # 0x1800742e8
   18001abd0:	48 8b e8             	mov    %rax,%rbp
   18001abd3:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
   18001abd7:	75 07                	jne    0x18001abe0
   18001abd9:	32 c0                	xor    %al,%al
```

## `SETUPAPI.dll!SetupDiGetDeviceInterfaceDetailW` (2 Call Sites)

### Line 29439 (Address `0x1800742f0`)
```assembly
   18001abed:	45 33 c9             	xor    %r9d,%r9d
   18001abf0:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001abf5:	4c 8d 05 84 c1 08 00 	lea    0x8c184(%rip),%r8        # 0x1800a6d80
   18001abfc:	33 d2                	xor    %edx,%edx
   18001abfe:	48 8b cd             	mov    %rbp,%rcx
   18001ac01:	ff 15 d1 96 05 00    	call   *0x596d1(%rip)        # 0x1800742d8
   18001ac07:	85 c0                	test   %eax,%eax
   18001ac09:	0f 84 7c 01 00 00    	je     0x18001ad8b
   18001ac0f:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001ac14:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
   18001ac19:	45 33 c9             	xor    %r9d,%r9d
   18001ac1c:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001ac21:	45 33 c0             	xor    %r8d,%r8d
   18001ac24:	48 8d 54 24 38       	lea    0x38(%rsp),%rdx
   18001ac29:	48 8b cd             	mov    %rbp,%rcx
   18001ac2c:	ff 15 be 96 05 00    	call   *0x596be(%rip)        # 0x1800742f0
   18001ac32:	ff 15 d0 94 05 00    	call   *0x594d0(%rip)        # 0x180074108
   18001ac38:	83 f8 7a             	cmp    $0x7a,%eax
   18001ac3b:	74 21                	je     0x18001ac5e
   18001ac3d:	ff 15 c5 94 05 00    	call   *0x594c5(%rip)        # 0x180074108
```

### Line 29470 (Address `0x1800742f0`)
```assembly
   18001ac79:	45 8b c6             	mov    %r14d,%r8d
   18001ac7c:	ba 08 00 00 00       	mov    $0x8,%edx
   18001ac81:	48 8b c8             	mov    %rax,%rcx
   18001ac84:	ff 15 9e 94 05 00    	call   *0x5949e(%rip)        # 0x180074128
   18001ac8a:	48 8b d8             	mov    %rax,%rbx
   18001ac8d:	48 85 c0             	test   %rax,%rax
   18001ac90:	0f 84 c9 00 00 00    	je     0x18001ad5f
   18001ac96:	c7 00 08 00 00 00    	movl   $0x8,(%rax)
   18001ac9c:	48 8d 54 24 38       	lea    0x38(%rsp),%rdx
   18001aca1:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
   18001aca6:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
   18001acab:	45 8b ce             	mov    %r14d,%r9d
   18001acae:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
   18001acb3:	4c 8b c3             	mov    %rbx,%r8
   18001acb6:	48 8b cd             	mov    %rbp,%rcx
   18001acb9:	ff 15 31 96 05 00    	call   *0x59631(%rip)        # 0x1800742f0
   18001acbf:	85 c0                	test   %eax,%eax
   18001acc1:	75 1e                	jne    0x18001ace1
   18001acc3:	ff 15 3f 94 05 00    	call   *0x5943f(%rip)        # 0x180074108
   18001acc9:	48 8b 0d 38 d9 08 00 	mov    0x8d938(%rip),%rcx        # 0x1800a8608
```

## `SHELL32.dll!SHGetSpecialFolderPathW` (2 Call Sites)

### Line 23788 (Address `0x180074300`)
```assembly
   180015e75:	8d 50 01             	lea    0x1(%rax),%edx
   180015e78:	48 8d 4c 24 30       	lea    0x30(%rsp),%rcx
   180015e7d:	e8 7e 44 00 00       	call   0x18001a300
   180015e82:	4c 8b 44 24 38       	mov    0x38(%rsp),%r8
   180015e87:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
   180015e8c:	4c 2b c1             	sub    %rcx,%r8
   180015e8f:	49 d1 f8             	sar    $1,%r8
   180015e92:	4d 03 c0             	add    %r8,%r8
   180015e95:	48 8d 15 40 4b 08 00 	lea    0x84b40(%rip),%rdx        # 0x18009a9dc
   180015e9c:	e8 2f 0b 04 00       	call   0x1800569d0
   180015ea1:	90                   	nop
   180015ea2:	41 b9 01 00 00 00    	mov    $0x1,%r9d
   180015ea8:	45 8d 41 19          	lea    0x19(%r9),%r8d
   180015eac:	48 8d 54 24 70       	lea    0x70(%rsp),%rdx
   180015eb1:	33 c9                	xor    %ecx,%ecx
   180015eb3:	ff 15 47 e4 05 00    	call   *0x5e447(%rip)        # 0x180074300
   180015eb9:	83 f8 01             	cmp    $0x1,%eax
   180015ebc:	75 16                	jne    0x180015ed4
   180015ebe:	48 8d 4b 40          	lea    0x40(%rbx),%rcx
   180015ec2:	4c 8d 44 24 70       	lea    0x70(%rsp),%r8
```

### Line 25881 (Address `0x180074300`)
```assembly
   180017b33:	ba 01 00 00 00       	mov    $0x1,%edx
   180017b38:	48 8d 4c 24 28       	lea    0x28(%rsp),%rcx
   180017b3d:	e8 be 27 00 00       	call   0x18001a300
   180017b42:	4c 8b 44 24 30       	mov    0x30(%rsp),%r8
   180017b47:	48 8b 4c 24 28       	mov    0x28(%rsp),%rcx
   180017b4c:	4c 2b c1             	sub    %rcx,%r8
   180017b4f:	49 d1 f8             	sar    $1,%r8
   180017b52:	4d 03 c0             	add    %r8,%r8
   180017b55:	48 8d 15 80 2e 08 00 	lea    0x82e80(%rip),%rdx        # 0x18009a9dc
   180017b5c:	e8 6f ee 03 00       	call   0x1800569d0
   180017b61:	90                   	nop
   180017b62:	41 b9 01 00 00 00    	mov    $0x1,%r9d
   180017b68:	45 8d 41 19          	lea    0x19(%r9),%r8d
   180017b6c:	48 8d 54 24 70       	lea    0x70(%rsp),%rdx
   180017b71:	33 c9                	xor    %ecx,%ecx
   180017b73:	ff 15 87 c7 05 00    	call   *0x5c787(%rip)        # 0x180074300
   180017b79:	83 f8 01             	cmp    $0x1,%eax
   180017b7c:	75 19                	jne    0x180017b97
   180017b7e:	48 8d 8b f0 03 00 00 	lea    0x3f0(%rbx),%rcx
   180017b85:	4c 8d 44 24 70       	lea    0x70(%rsp),%r8
```

## `libusb0.dll!usb_bulk_write` (2 Call Sites)

### Line 32544 (Address `0x180074340`)
```assembly
   18001daee:	44 8b be bc 01 00 00 	mov    0x1bc(%rsi),%r15d
   18001daf5:	48 8b be c0 01 00 00 	mov    0x1c0(%rsi),%rdi
   18001dafc:	48 39 ab 90 01 00 00 	cmp    %rbp,0x190(%rbx)
   18001db03:	75 0a                	jne    0x18001db0f
   18001db05:	bf ff ff ff ff       	mov    $0xffffffff,%edi
   18001db0a:	e9 bc 00 00 00       	jmp    0x18001dbcb
   18001db0f:	48 8b 43 50          	mov    0x50(%rbx),%rax
   18001db13:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001db17:	ff 50 08             	call   *0x8(%rax)
   18001db1a:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001db21:	45 8b cf             	mov    %r15d,%r9d
   18001db24:	4c 8b c7             	mov    %rdi,%r8
   18001db27:	c7 44 24 20 b8 0b 00 	movl   $0xbb8,0x20(%rsp)
   18001db2e:	00 
   18001db2f:	ba 04 00 00 00       	mov    $0x4,%edx
   18001db34:	ff 15 06 68 05 00    	call   *0x56806(%rip)        # 0x180074340
   18001db3a:	8b f8                	mov    %eax,%edi
   18001db3c:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001db40:	48 8b 43 50          	mov    0x50(%rbx),%rax
   18001db44:	ff 50 10             	call   *0x10(%rax)
```

### Line 32571 (Address `0x180074340`)
```assembly
   18001db63:	e8 28 87 ff ff       	call   0x180016290
   18001db68:	eb 61                	jmp    0x18001dbcb
   18001db6a:	48 39 ab 90 01 00 00 	cmp    %rbp,0x190(%rbx)
   18001db71:	75 07                	jne    0x18001db7a
   18001db73:	bf ff ff ff ff       	mov    $0xffffffff,%edi
   18001db78:	eb 51                	jmp    0x18001dbcb
   18001db7a:	48 8b 43 50          	mov    0x50(%rbx),%rax
   18001db7e:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001db82:	ff 50 08             	call   *0x8(%rax)
   18001db85:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001db8c:	4c 8d 44 24 34       	lea    0x34(%rsp),%r8
   18001db91:	45 33 c9             	xor    %r9d,%r9d
   18001db94:	c7 44 24 20 b8 0b 00 	movl   $0xbb8,0x20(%rsp)
   18001db9b:	00 
   18001db9c:	41 8d 51 04          	lea    0x4(%r9),%edx
   18001dba0:	ff 15 9a 67 05 00    	call   *0x5679a(%rip)        # 0x180074340
   18001dba6:	48 8b 43 50          	mov    0x50(%rbx),%rax
   18001dbaa:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001dbae:	ff 50 10             	call   *0x10(%rax)
   18001dbb1:	eb 18                	jmp    0x18001dbcb
```

## `libusb0.dll!usb_claim_interface` (1 Call Sites)

### Line 29949 (Address `0x180074318`)
```assembly
   18001b3a4:	48 8b ec             	mov    %rsp,%rbp
   18001b3a7:	48 83 ec 70          	sub    $0x70,%rsp
   18001b3ab:	48 8b 05 ae af 08 00 	mov    0x8afae(%rip),%rax        # 0x1800a6360
   18001b3b2:	48 33 c4             	xor    %rsp,%rax
   18001b3b5:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
   18001b3b9:	44 8b 81 84 00 00 00 	mov    0x84(%rcx),%r8d
   18001b3c0:	48 8d 15 a1 17 08 00 	lea    0x817a1(%rip),%rdx        # 0x18009cb68
   18001b3c7:	48 8b d9             	mov    %rcx,%rbx
   18001b3ca:	48 8b 0d 37 d2 08 00 	mov    0x8d237(%rip),%rcx        # 0x1800a8608
   18001b3d1:	e8 ba ae ff ff       	call   0x180016290
   18001b3d6:	80 bb 95 05 00 00 00 	cmpb   $0x0,0x595(%rbx)
   18001b3dd:	bf 03 00 00 00       	mov    $0x3,%edi
   18001b3e2:	75 6c                	jne    0x18001b450
   18001b3e4:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001b3eb:	8b d7                	mov    %edi,%edx
   18001b3ed:	ff 15 25 8f 05 00    	call   *0x58f25(%rip)        # 0x180074318
   18001b3f3:	85 c0                	test   %eax,%eax
   18001b3f5:	74 52                	je     0x18001b449
   18001b3f7:	48 8b 0d 0a d2 08 00 	mov    0x8d20a(%rip),%rcx        # 0x1800a8608
   18001b3fe:	48 8d 15 8b 17 08 00 	lea    0x8178b(%rip),%rdx        # 0x18009cb90
```

## `libusb0.dll!usb_close` (1 Call Sites)

### Line 29851 (Address `0x180074320`)
```assembly
   18001b23a:	41 c6 86 a9 05 00 00 	movb   $0x0,0x5a9(%r14)
   18001b241:	00 
   18001b242:	48 8d 15 37 25 08 00 	lea    0x82537(%rip),%rdx        # 0x18009d780
   18001b249:	48 8b 0d b8 d3 08 00 	mov    0x8d3b8(%rip),%rcx        # 0x1800a8608
   18001b250:	e8 3b b0 ff ff       	call   0x180016290
   18001b255:	90                   	nop
   18001b256:	ba 03 00 00 00       	mov    $0x3,%edx
   18001b25b:	49 8b 8e 90 01 00 00 	mov    0x190(%r14),%rcx
   18001b262:	ff 15 c8 90 05 00    	call   *0x590c8(%rip)        # 0x180074330
   18001b268:	90                   	nop
   18001b269:	48 8d 15 40 25 08 00 	lea    0x82540(%rip),%rdx        # 0x18009d7b0
   18001b270:	48 8b 0d 91 d3 08 00 	mov    0x8d391(%rip),%rcx        # 0x1800a8608
   18001b277:	e8 14 b0 ff ff       	call   0x180016290
   18001b27c:	90                   	nop
   18001b27d:	49 8b 8e 90 01 00 00 	mov    0x190(%r14),%rcx
   18001b284:	ff 15 96 90 05 00    	call   *0x59096(%rip)        # 0x180074320
   18001b28a:	90                   	nop
   18001b28b:	33 f6                	xor    %esi,%esi
   18001b28d:	49 89 b6 90 01 00 00 	mov    %rsi,0x190(%r14)
   18001b294:	48 8d 15 4d 24 08 00 	lea    0x8244d(%rip),%rdx        # 0x18009d6e8
```

## `libusb0.dll!usb_control_msg` (23 Call Sites)

### Line 27133 (Address `0x180074328`)
```assembly
   180018c58:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   180018c5f:	8d 43 06             	lea    0x6(%rbx),%eax
   180018c62:	45 33 c9             	xor    %r9d,%r9d
   180018c65:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   180018c6c:	00 
   180018c6d:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   180018c74:	ba 21 00 00 00       	mov    $0x21,%edx
   180018c79:	89 44 24 30          	mov    %eax,0x30(%rsp)
   180018c7d:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   180018c82:	41 0f 95 c1          	setne  %r9b
   180018c86:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   180018c8b:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   180018c92:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   180018c99:	00 
   180018c9a:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   180018c9e:	ff 15 84 b6 05 00    	call   *0x5b684(%rip)        # 0x180074328
   180018ca4:	8b d8                	mov    %eax,%ebx
   180018ca6:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   180018caa:	48 8b 46 50          	mov    0x50(%rsi),%rax
   180018cae:	ff 50 10             	call   *0x10(%rax)
```

### Line 32791 (Address `0x180074328`)
```assembly
   18001de96:	ff 50 08             	call   *0x8(%rax)
   18001de99:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001dea0:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001dea5:	45 33 c9             	xor    %r9d,%r9d
   18001dea8:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001deaf:	00 
   18001deb0:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001deb7:	ba 21 00 00 00       	mov    $0x21,%edx
   18001debc:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001dec1:	41 0f 95 c1          	setne  %r9b
   18001dec5:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001deca:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001ded1:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001ded8:	00 
   18001ded9:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001dedd:	ff 15 45 64 05 00    	call   *0x56445(%rip)        # 0x180074328
   18001dee3:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001dee7:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001deeb:	44 8b f0             	mov    %eax,%r14d
   18001deee:	ff 52 10             	call   *0x10(%rdx)
```

### Line 32820 (Address `0x180074328`)
```assembly
   18001df14:	ff 50 08             	call   *0x8(%rax)
   18001df17:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001df1e:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001df23:	45 33 c9             	xor    %r9d,%r9d
   18001df26:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001df2d:	00 
   18001df2e:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001df35:	ba a1 00 00 00       	mov    $0xa1,%edx
   18001df3a:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001df3f:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   18001df45:	41 0f 95 c1          	setne  %r9b
   18001df49:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001df4e:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001df55:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001df5c:	00 
   18001df5d:	ff 15 c5 63 05 00    	call   *0x563c5(%rip)        # 0x180074328
   18001df63:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001df67:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001df6b:	44 8b f0             	mov    %eax,%r14d
   18001df6e:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33103 (Address `0x180074328`)
```assembly
   18001e325:	ff 50 08             	call   *0x8(%rax)
   18001e328:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001e32f:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001e334:	45 33 c9             	xor    %r9d,%r9d
   18001e337:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e33e:	00 
   18001e33f:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001e346:	41 8d 55 20          	lea    0x20(%r13),%edx
   18001e34a:	89 6c 24 30          	mov    %ebp,0x30(%rsp)
   18001e34e:	45 8d 45 08          	lea    0x8(%r13),%r8d
   18001e352:	41 0f 95 c1          	setne  %r9b
   18001e356:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e35b:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e362:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001e369:	00 
   18001e36a:	ff 15 b8 5f 05 00    	call   *0x55fb8(%rip)        # 0x180074328
   18001e370:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001e374:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001e378:	8b f8                	mov    %eax,%edi
   18001e37a:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33132 (Address `0x180074328`)
```assembly
   18001e39b:	ff 50 08             	call   *0x8(%rax)
   18001e39e:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001e3a5:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001e3aa:	45 33 c9             	xor    %r9d,%r9d
   18001e3ad:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e3b4:	00 
   18001e3b5:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001e3bc:	45 8b c5             	mov    %r13d,%r8d
   18001e3bf:	89 6c 24 30          	mov    %ebp,0x30(%rsp)
   18001e3c3:	ba a1 00 00 00       	mov    $0xa1,%edx
   18001e3c8:	41 0f 95 c1          	setne  %r9b
   18001e3cc:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e3d1:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e3d8:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001e3df:	00 
   18001e3e0:	ff 15 42 5f 05 00    	call   *0x55f42(%rip)        # 0x180074328
   18001e3e6:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001e3ea:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001e3ee:	8b f8                	mov    %eax,%edi
   18001e3f0:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33248 (Address `0x180074328`)
```assembly
   18001e543:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001e54a:	8d 43 06             	lea    0x6(%rbx),%eax
   18001e54d:	45 33 c9             	xor    %r9d,%r9d
   18001e550:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e557:	00 
   18001e558:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001e55f:	ba 21 00 00 00       	mov    $0x21,%edx
   18001e564:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001e568:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001e56d:	41 0f 95 c1          	setne  %r9b
   18001e571:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e576:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e57d:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001e584:	00 
   18001e585:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001e589:	ff 15 99 5d 05 00    	call   *0x55d99(%rip)        # 0x180074328
   18001e58f:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001e593:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001e597:	8b d8                	mov    %eax,%ebx
   18001e599:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33372 (Address `0x180074328`)
```assembly
   18001e6f6:	ff 50 08             	call   *0x8(%rax)
   18001e6f9:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001e700:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001e705:	45 33 c9             	xor    %r9d,%r9d
   18001e708:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e70f:	00 
   18001e710:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001e717:	ba 21 00 00 00       	mov    $0x21,%edx
   18001e71c:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001e721:	41 0f 95 c1          	setne  %r9b
   18001e725:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e72a:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e731:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001e738:	00 
   18001e739:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001e73d:	ff 15 e5 5b 05 00    	call   *0x55be5(%rip)        # 0x180074328
   18001e743:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001e747:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001e74b:	44 8b f0             	mov    %eax,%r14d
   18001e74e:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33401 (Address `0x180074328`)
```assembly
   18001e774:	ff 50 08             	call   *0x8(%rax)
   18001e777:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001e77e:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001e783:	45 33 c9             	xor    %r9d,%r9d
   18001e786:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e78d:	00 
   18001e78e:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001e795:	ba a1 00 00 00       	mov    $0xa1,%edx
   18001e79a:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001e79f:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   18001e7a5:	41 0f 95 c1          	setne  %r9b
   18001e7a9:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e7ae:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e7b5:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001e7bc:	00 
   18001e7bd:	ff 15 65 5b 05 00    	call   *0x55b65(%rip)        # 0x180074328
   18001e7c3:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001e7c7:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001e7cb:	44 8b f0             	mov    %eax,%r14d
   18001e7ce:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33550 (Address `0x180074328`)
```assembly
   18001e999:	45 8b cd             	mov    %r13d,%r9d
   18001e99c:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001e9a3:	00 
   18001e9a4:	40 84 ff             	test   %dil,%dil
   18001e9a7:	ba 21 00 00 00       	mov    $0x21,%edx
   18001e9ac:	0f 95 c0             	setne  %al
   18001e9af:	83 c0 08             	add    $0x8,%eax
   18001e9b2:	44 38 ab a8 05 00 00 	cmp    %r13b,0x5a8(%rbx)
   18001e9b9:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001e9bd:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001e9c1:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001e9c6:	41 0f 95 c1          	setne  %r9b
   18001e9ca:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001e9cf:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001e9d6:	44 89 6c 24 20       	mov    %r13d,0x20(%rsp)
   18001e9db:	ff 15 47 59 05 00    	call   *0x55947(%rip)        # 0x180074328
   18001e9e1:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001e9e5:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001e9e9:	8b f8                	mov    %eax,%edi
   18001e9eb:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33706 (Address `0x180074328`)
```assembly
   18001ebcb:	ff 50 08             	call   *0x8(%rax)
   18001ebce:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001ebd5:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001ebda:	45 33 c9             	xor    %r9d,%r9d
   18001ebdd:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001ebe4:	00 
   18001ebe5:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001ebec:	41 8d 55 20          	lea    0x20(%r13),%edx
   18001ebf0:	89 6c 24 30          	mov    %ebp,0x30(%rsp)
   18001ebf4:	45 8d 45 08          	lea    0x8(%r13),%r8d
   18001ebf8:	41 0f 95 c1          	setne  %r9b
   18001ebfc:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001ec01:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001ec08:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001ec0f:	00 
   18001ec10:	ff 15 12 57 05 00    	call   *0x55712(%rip)        # 0x180074328
   18001ec16:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001ec1a:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001ec1e:	8b f8                	mov    %eax,%edi
   18001ec20:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33735 (Address `0x180074328`)
```assembly
   18001ec41:	ff 50 08             	call   *0x8(%rax)
   18001ec44:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001ec4b:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001ec50:	45 33 c9             	xor    %r9d,%r9d
   18001ec53:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001ec5a:	00 
   18001ec5b:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001ec62:	45 8b c5             	mov    %r13d,%r8d
   18001ec65:	89 6c 24 30          	mov    %ebp,0x30(%rsp)
   18001ec69:	ba a1 00 00 00       	mov    $0xa1,%edx
   18001ec6e:	41 0f 95 c1          	setne  %r9b
   18001ec72:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001ec77:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001ec7e:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001ec85:	00 
   18001ec86:	ff 15 9c 56 05 00    	call   *0x5569c(%rip)        # 0x180074328
   18001ec8c:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001ec90:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001ec94:	8b f8                	mov    %eax,%edi
   18001ec96:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33864 (Address `0x180074328`)
```assembly
   18001ee18:	ff 50 08             	call   *0x8(%rax)
   18001ee1b:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001ee22:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001ee27:	45 33 c9             	xor    %r9d,%r9d
   18001ee2a:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001ee31:	00 
   18001ee32:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001ee39:	ba 21 00 00 00       	mov    $0x21,%edx
   18001ee3e:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001ee43:	41 0f 95 c1          	setne  %r9b
   18001ee47:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001ee4c:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001ee53:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001ee5a:	00 
   18001ee5b:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001ee5f:	ff 15 c3 54 05 00    	call   *0x554c3(%rip)        # 0x180074328
   18001ee65:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001ee69:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001ee6d:	44 8b f0             	mov    %eax,%r14d
   18001ee70:	ff 52 10             	call   *0x10(%rdx)
```

### Line 33893 (Address `0x180074328`)
```assembly
   18001ee96:	ff 50 08             	call   *0x8(%rax)
   18001ee99:	48 8b 8b 90 01 00 00 	mov    0x190(%rbx),%rcx
   18001eea0:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001eea5:	45 33 c9             	xor    %r9d,%r9d
   18001eea8:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001eeaf:	00 
   18001eeb0:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001eeb7:	ba a1 00 00 00       	mov    $0xa1,%edx
   18001eebc:	44 89 7c 24 30       	mov    %r15d,0x30(%rsp)
   18001eec1:	41 b8 01 00 00 00    	mov    $0x1,%r8d
   18001eec7:	41 0f 95 c1          	setne  %r9b
   18001eecb:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001eed0:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001eed7:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001eede:	00 
   18001eedf:	ff 15 43 54 05 00    	call   *0x55443(%rip)        # 0x180074328
   18001eee5:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001eee9:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001eeed:	44 8b f0             	mov    %eax,%r14d
   18001eef0:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34029 (Address `0x180074328`)
```assembly
   18001f096:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001f09d:	8d 43 06             	lea    0x6(%rbx),%eax
   18001f0a0:	45 33 c9             	xor    %r9d,%r9d
   18001f0a3:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001f0aa:	00 
   18001f0ab:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001f0b2:	ba 21 00 00 00       	mov    $0x21,%edx
   18001f0b7:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001f0bb:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001f0c0:	41 0f 95 c1          	setne  %r9b
   18001f0c4:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001f0c9:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001f0d0:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001f0d7:	00 
   18001f0d8:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001f0dc:	ff 15 46 52 05 00    	call   *0x55246(%rip)        # 0x180074328
   18001f0e2:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001f0e6:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001f0ea:	8b d8                	mov    %eax,%ebx
   18001f0ec:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34147 (Address `0x180074328`)
```assembly
   18001f249:	45 8b cd             	mov    %r13d,%r9d
   18001f24c:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001f253:	00 
   18001f254:	40 84 ff             	test   %dil,%dil
   18001f257:	ba 21 00 00 00       	mov    $0x21,%edx
   18001f25c:	0f 95 c0             	setne  %al
   18001f25f:	83 c0 08             	add    $0x8,%eax
   18001f262:	44 38 ab a8 05 00 00 	cmp    %r13b,0x5a8(%rbx)
   18001f269:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001f26d:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001f271:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001f276:	41 0f 95 c1          	setne  %r9b
   18001f27a:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001f27f:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001f286:	44 89 6c 24 20       	mov    %r13d,0x20(%rsp)
   18001f28b:	ff 15 97 50 05 00    	call   *0x55097(%rip)        # 0x180074328
   18001f291:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001f295:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001f299:	8b f8                	mov    %eax,%edi
   18001f29b:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34319 (Address `0x180074328`)
```assembly
   18001f4d1:	00 
   18001f4d2:	40 84 f6             	test   %sil,%sil
   18001f4d5:	ba 21 00 00 00       	mov    $0x21,%edx
   18001f4da:	0f 95 c0             	setne  %al
   18001f4dd:	45 33 c9             	xor    %r9d,%r9d
   18001f4e0:	83 c0 08             	add    $0x8,%eax
   18001f4e3:	44 38 8b a8 05 00 00 	cmp    %r9b,0x5a8(%rbx)
   18001f4ea:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001f4ee:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001f4f2:	41 0f 95 c1          	setne  %r9b
   18001f4f6:	48 8d 44 24 50       	lea    0x50(%rsp),%rax
   18001f4fb:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001f500:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001f507:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001f50e:	00 
   18001f50f:	ff 15 13 4e 05 00    	call   *0x54e13(%rip)        # 0x180074328
   18001f515:	48 8b 53 50          	mov    0x50(%rbx),%rdx
   18001f519:	48 8d 4b 50          	lea    0x50(%rbx),%rcx
   18001f51d:	8b f0                	mov    %eax,%esi
   18001f51f:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34447 (Address `0x180074328`)
```assembly
   18001f6ba:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001f6c1:	8d 43 02             	lea    0x2(%rbx),%eax
   18001f6c4:	45 33 c9             	xor    %r9d,%r9d
   18001f6c7:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001f6ce:	00 
   18001f6cf:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001f6d6:	ba 21 00 00 00       	mov    $0x21,%edx
   18001f6db:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001f6df:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001f6e4:	41 0f 95 c1          	setne  %r9b
   18001f6e8:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001f6ed:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001f6f4:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001f6fb:	00 
   18001f6fc:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001f700:	ff 15 22 4c 05 00    	call   *0x54c22(%rip)        # 0x180074328
   18001f706:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001f70a:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001f70e:	8b d8                	mov    %eax,%ebx
   18001f710:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34567 (Address `0x180074328`)
```assembly
   18001f887:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001f88e:	8d 43 06             	lea    0x6(%rbx),%eax
   18001f891:	45 33 c9             	xor    %r9d,%r9d
   18001f894:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001f89b:	00 
   18001f89c:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001f8a3:	ba 21 00 00 00       	mov    $0x21,%edx
   18001f8a8:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001f8ac:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   18001f8b1:	41 0f 95 c1          	setne  %r9b
   18001f8b5:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001f8ba:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001f8c1:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001f8c8:	00 
   18001f8c9:	44 8d 42 e8          	lea    -0x18(%rdx),%r8d
   18001f8cd:	ff 15 55 4a 05 00    	call   *0x54a55(%rip)        # 0x180074328
   18001f8d3:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001f8d7:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001f8db:	8b d8                	mov    %eax,%ebx
   18001f8dd:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34688 (Address `0x180074328`)
```assembly
   18001fa5b:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001fa62:	8d 43 06             	lea    0x6(%rbx),%eax
   18001fa65:	45 33 c9             	xor    %r9d,%r9d
   18001fa68:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001fa6f:	00 
   18001fa70:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001fa77:	8d 55 20             	lea    0x20(%rbp),%edx
   18001fa7a:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001fa7e:	44 8d 45 08          	lea    0x8(%rbp),%r8d
   18001fa82:	41 0f 95 c1          	setne  %r9b
   18001fa86:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001fa8b:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001fa90:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001fa97:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001fa9e:	00 
   18001fa9f:	ff 15 83 48 05 00    	call   *0x54883(%rip)        # 0x180074328
   18001faa5:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001faa9:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001faad:	8b d8                	mov    %eax,%ebx
   18001faaf:	ff 52 10             	call   *0x10(%rdx)
```

### Line 34874 (Address `0x180074328`)
```assembly
   18001fd0e:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18001fd15:	8d 43 02             	lea    0x2(%rbx),%eax
   18001fd18:	45 33 c9             	xor    %r9d,%r9d
   18001fd1b:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   18001fd22:	00 
   18001fd23:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18001fd2a:	41 8d 54 24 20       	lea    0x20(%r12),%edx
   18001fd2f:	89 44 24 30          	mov    %eax,0x30(%rsp)
   18001fd33:	45 8d 44 24 08       	lea    0x8(%r12),%r8d
   18001fd38:	41 0f 95 c1          	setne  %r9b
   18001fd3c:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   18001fd41:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18001fd46:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   18001fd4d:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18001fd54:	00 
   18001fd55:	ff 15 cd 45 05 00    	call   *0x545cd(%rip)        # 0x180074328
   18001fd5b:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   18001fd5f:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18001fd63:	8b d8                	mov    %eax,%ebx
   18001fd65:	ff 52 10             	call   *0x10(%rdx)
```

### Line 35068 (Address `0x180074328`)
```assembly
   180020003:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   18002000a:	8d 43 02             	lea    0x2(%rbx),%eax
   18002000d:	45 33 c9             	xor    %r9d,%r9d
   180020010:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   180020017:	00 
   180020018:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   18002001f:	41 8d 54 24 20       	lea    0x20(%r12),%edx
   180020024:	89 44 24 30          	mov    %eax,0x30(%rsp)
   180020028:	45 8d 44 24 08       	lea    0x8(%r12),%r8d
   18002002d:	41 0f 95 c1          	setne  %r9b
   180020031:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   180020036:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18002003b:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   180020042:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   180020049:	00 
   18002004a:	ff 15 d8 42 05 00    	call   *0x542d8(%rip)        # 0x180074328
   180020050:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   180020054:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   180020058:	8b d8                	mov    %eax,%ebx
   18002005a:	ff 52 10             	call   *0x10(%rdx)
```

### Line 35249 (Address `0x180074328`)
```assembly
   1800202d7:	48 8b 8e 90 01 00 00 	mov    0x190(%rsi),%rcx
   1800202de:	8d 43 06             	lea    0x6(%rbx),%eax
   1800202e1:	45 33 c9             	xor    %r9d,%r9d
   1800202e4:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   1800202eb:	00 
   1800202ec:	44 38 8e a8 05 00 00 	cmp    %r9b,0x5a8(%rsi)
   1800202f3:	41 8d 56 20          	lea    0x20(%r14),%edx
   1800202f7:	89 44 24 30          	mov    %eax,0x30(%rsp)
   1800202fb:	45 8d 46 08          	lea    0x8(%r14),%r8d
   1800202ff:	41 0f 95 c1          	setne  %r9b
   180020303:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   180020308:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   18002030d:	41 81 c1 00 03 00 00 	add    $0x300,%r9d
   180020314:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   18002031b:	00 
   18002031c:	ff 15 06 40 05 00    	call   *0x54006(%rip)        # 0x180074328
   180020322:	48 8b 56 50          	mov    0x50(%rsi),%rdx
   180020326:	48 8d 4e 50          	lea    0x50(%rsi),%rcx
   18002032a:	8b d8                	mov    %eax,%ebx
   18002032c:	ff 52 10             	call   *0x10(%rdx)
```

### Line 35423 (Address `0x180074328`)
```assembly
   180020571:	48 8d 4f 50          	lea    0x50(%rdi),%rcx
   180020575:	c6 44 14 4f 00       	movb   $0x0,0x4f(%rsp,%rdx,1)
   18002057a:	ff 50 08             	call   *0x8(%rax)
   18002057d:	48 8b 8f 90 01 00 00 	mov    0x190(%rdi),%rcx
   180020584:	48 8d 44 24 48       	lea    0x48(%rsp),%rax
   180020589:	c7 44 24 38 e8 03 00 	movl   $0x3e8,0x38(%rsp)
   180020590:	00 
   180020591:	8d 55 20             	lea    0x20(%rbp),%edx
   180020594:	c7 44 24 30 08 00 00 	movl   $0x8,0x30(%rsp)
   18002059b:	00 
   18002059c:	44 8d 45 08          	lea    0x8(%rbp),%r8d
   1800205a0:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
   1800205a5:	41 b9 00 03 00 00    	mov    $0x300,%r9d
   1800205ab:	c7 44 24 20 00 00 00 	movl   $0x0,0x20(%rsp)
   1800205b2:	00 
   1800205b3:	ff 15 6f 3d 05 00    	call   *0x53d6f(%rip)        # 0x180074328
   1800205b9:	48 8b 57 50          	mov    0x50(%rdi),%rdx
   1800205bd:	48 8d 4f 50          	lea    0x50(%rdi),%rcx
   1800205c1:	8b f0                	mov    %eax,%esi
   1800205c3:	ff 52 10             	call   *0x10(%rdx)
```

## `libusb0.dll!usb_find_busses` (1 Call Sites)

### Line 27206 (Address `0x180074358`)
```assembly
   180018d5f:	cc                   	int3
   180018d60:	48 8b c4             	mov    %rsp,%rax
   180018d63:	57                   	push   %rdi
   180018d64:	41 54                	push   %r12
   180018d66:	41 55                	push   %r13
   180018d68:	41 56                	push   %r14
   180018d6a:	41 57                	push   %r15
   180018d6c:	48 81 ec d0 00 00 00 	sub    $0xd0,%rsp
   180018d73:	48 c7 44 24 40 fe ff 	movq   $0xfffffffffffffffe,0x40(%rsp)
   180018d7a:	ff ff 
   180018d7c:	48 89 58 08          	mov    %rbx,0x8(%rax)
   180018d80:	48 89 68 18          	mov    %rbp,0x18(%rax)
   180018d84:	48 89 70 20          	mov    %rsi,0x20(%rax)
   180018d88:	4c 8b e9             	mov    %rcx,%r13
   180018d8b:	33 db                	xor    %ebx,%ebx
   180018d8d:	ff 15 c5 b5 05 00    	call   *0x5b5c5(%rip)        # 0x180074358
   180018d93:	ff 15 b7 b5 05 00    	call   *0x5b5b7(%rip)        # 0x180074350
   180018d99:	ff 15 71 b5 05 00    	call   *0x5b571(%rip)        # 0x180074310
   180018d9f:	4c 8b c0             	mov    %rax,%r8
   180018da2:	48 85 c0             	test   %rax,%rax
```

## `libusb0.dll!usb_find_devices` (1 Call Sites)

### Line 27207 (Address `0x180074350`)
```assembly
   180018d60:	48 8b c4             	mov    %rsp,%rax
   180018d63:	57                   	push   %rdi
   180018d64:	41 54                	push   %r12
   180018d66:	41 55                	push   %r13
   180018d68:	41 56                	push   %r14
   180018d6a:	41 57                	push   %r15
   180018d6c:	48 81 ec d0 00 00 00 	sub    $0xd0,%rsp
   180018d73:	48 c7 44 24 40 fe ff 	movq   $0xfffffffffffffffe,0x40(%rsp)
   180018d7a:	ff ff 
   180018d7c:	48 89 58 08          	mov    %rbx,0x8(%rax)
   180018d80:	48 89 68 18          	mov    %rbp,0x18(%rax)
   180018d84:	48 89 70 20          	mov    %rsi,0x20(%rax)
   180018d88:	4c 8b e9             	mov    %rcx,%r13
   180018d8b:	33 db                	xor    %ebx,%ebx
   180018d8d:	ff 15 c5 b5 05 00    	call   *0x5b5c5(%rip)        # 0x180074358
   180018d93:	ff 15 b7 b5 05 00    	call   *0x5b5b7(%rip)        # 0x180074350
   180018d99:	ff 15 71 b5 05 00    	call   *0x5b571(%rip)        # 0x180074310
   180018d9f:	4c 8b c0             	mov    %rax,%r8
   180018da2:	48 85 c0             	test   %rax,%rax
   180018da5:	74 78                	je     0x180018e1f
```

## `libusb0.dll!usb_get_busses` (1 Call Sites)

### Line 27208 (Address `0x180074310`)
```assembly
   180018d63:	57                   	push   %rdi
   180018d64:	41 54                	push   %r12
   180018d66:	41 55                	push   %r13
   180018d68:	41 56                	push   %r14
   180018d6a:	41 57                	push   %r15
   180018d6c:	48 81 ec d0 00 00 00 	sub    $0xd0,%rsp
   180018d73:	48 c7 44 24 40 fe ff 	movq   $0xfffffffffffffffe,0x40(%rsp)
   180018d7a:	ff ff 
   180018d7c:	48 89 58 08          	mov    %rbx,0x8(%rax)
   180018d80:	48 89 68 18          	mov    %rbp,0x18(%rax)
   180018d84:	48 89 70 20          	mov    %rsi,0x20(%rax)
   180018d88:	4c 8b e9             	mov    %rcx,%r13
   180018d8b:	33 db                	xor    %ebx,%ebx
   180018d8d:	ff 15 c5 b5 05 00    	call   *0x5b5c5(%rip)        # 0x180074358
   180018d93:	ff 15 b7 b5 05 00    	call   *0x5b5b7(%rip)        # 0x180074350
   180018d99:	ff 15 71 b5 05 00    	call   *0x5b571(%rip)        # 0x180074310
   180018d9f:	4c 8b c0             	mov    %rax,%r8
   180018da2:	48 85 c0             	test   %rax,%rax
   180018da5:	74 78                	je     0x180018e1f
   180018da7:	33 d2                	xor    %edx,%edx
```

## `libusb0.dll!usb_init` (1 Call Sites)

### Line 26694 (Address `0x180074348`)
```assembly
   18001859f:	cc                   	int3
   1800185a0:	41 54                	push   %r12
   1800185a2:	41 56                	push   %r14
   1800185a4:	41 57                	push   %r15
   1800185a6:	48 83 ec 30          	sub    $0x30,%rsp
   1800185aa:	48 c7 44 24 20 fe ff 	movq   $0xfffffffffffffffe,0x20(%rsp)
   1800185b1:	ff ff 
   1800185b3:	48 89 5c 24 50       	mov    %rbx,0x50(%rsp)
   1800185b8:	48 89 6c 24 58       	mov    %rbp,0x58(%rsp)
   1800185bd:	48 89 74 24 60       	mov    %rsi,0x60(%rsp)
   1800185c2:	48 89 7c 24 68       	mov    %rdi,0x68(%rsp)
   1800185c7:	48 8b e9             	mov    %rcx,%rbp
   1800185ca:	48 8d 15 c7 26 08 00 	lea    0x826c7(%rip),%rdx        # 0x18009ac98
   1800185d1:	48 8b 0d 30 00 09 00 	mov    0x90030(%rip),%rcx        # 0x1800a8608
   1800185d8:	e8 b3 dc ff ff       	call   0x180016290
   1800185dd:	ff 15 65 bd 05 00    	call   *0x5bd65(%rip)        # 0x180074348
   1800185e3:	48 8d 15 de 26 08 00 	lea    0x826de(%rip),%rdx        # 0x18009acc8
   1800185ea:	48 8b 0d 17 00 09 00 	mov    0x90017(%rip),%rcx        # 0x1800a8608
   1800185f1:	e8 9a dc ff ff       	call   0x180016290
   1800185f6:	0f b6 45 15          	movzbl 0x15(%rbp),%eax
```

## `libusb0.dll!usb_open` (1 Call Sites)

### Line 29647 (Address `0x180074338`)
```assembly
   18001af4c:	b8 00 02 00 00       	mov    $0x200,%eax
   18001af51:	45 8b cf             	mov    %r15d,%r9d
   18001af54:	66 41 39 86 1a 02 00 	cmp    %ax,0x21a(%r14)
   18001af5b:	00 
   18001af5c:	41 0f 97 c1          	seta   %r9b
   18001af60:	41 83 c1 03          	add    $0x3,%r9d
   18001af64:	44 89 4e 1c          	mov    %r9d,0x1c(%rsi)
   18001af68:	44 8b c3             	mov    %ebx,%r8d
   18001af6b:	48 8d 15 e6 19 08 00 	lea    0x819e6(%rip),%rdx        # 0x18009c958
   18001af72:	48 8b 0d 8f d6 08 00 	mov    0x8d68f(%rip),%rcx        # 0x1800a8608
   18001af79:	e8 62 b3 ff ff       	call   0x1800162e0
   18001af7e:	bd 03 00 00 00       	mov    $0x3,%ebp
   18001af83:	8b dd                	mov    %ebp,%ebx
   18001af85:	ff cb                	dec    %ebx
   18001af87:	49 8b ce             	mov    %r14,%rcx
   18001af8a:	ff 15 a8 93 05 00    	call   *0x593a8(%rip)        # 0x180074338
   18001af90:	48 89 86 90 01 00 00 	mov    %rax,0x190(%rsi)
   18001af97:	48 85 c0             	test   %rax,%rax
   18001af9a:	75 24                	jne    0x18001afc0
   18001af9c:	48 8d 15 e5 19 08 00 	lea    0x819e5(%rip),%rdx        # 0x18009c988
```

## `libusb0.dll!usb_release_interface` (1 Call Sites)

### Line 29844 (Address `0x180074330`)
```assembly
   18001b228:	90                   	nop
   18001b229:	48 8b 05 c8 d3 08 00 	mov    0x8d3c8(%rip),%rax        # 0x1800a85f8
   18001b230:	48 85 c0             	test   %rax,%rax
   18001b233:	74 05                	je     0x18001b23a
   18001b235:	8b cb                	mov    %ebx,%ecx
   18001b237:	ff d0                	call   *%rax
   18001b239:	90                   	nop
   18001b23a:	41 c6 86 a9 05 00 00 	movb   $0x0,0x5a9(%r14)
   18001b241:	00 
   18001b242:	48 8d 15 37 25 08 00 	lea    0x82537(%rip),%rdx        # 0x18009d780
   18001b249:	48 8b 0d b8 d3 08 00 	mov    0x8d3b8(%rip),%rcx        # 0x1800a8608
   18001b250:	e8 3b b0 ff ff       	call   0x180016290
   18001b255:	90                   	nop
   18001b256:	ba 03 00 00 00       	mov    $0x3,%edx
   18001b25b:	49 8b 8e 90 01 00 00 	mov    0x190(%r14),%rcx
   18001b262:	ff 15 c8 90 05 00    	call   *0x590c8(%rip)        # 0x180074330
   18001b268:	90                   	nop
   18001b269:	48 8d 15 40 25 08 00 	lea    0x82540(%rip),%rdx        # 0x18009d7b0
   18001b270:	48 8b 0d 91 d3 08 00 	mov    0x8d391(%rip),%rcx        # 0x1800a8608
   18001b277:	e8 14 b0 ff ff       	call   0x180016290
```

