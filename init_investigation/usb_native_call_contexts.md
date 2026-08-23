# Native USB & SetupAPI Call Contexts in MSDISPLAYSDKWRRAPER.dll

## `KERNEL32.dll!CreateFileW` (7 Call Sites)

### Call Site #1 (Line 25184, Address `0x180074100`)
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

### Call Site #2 (Line 27722, Address `0x180074100`)
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

### Call Site #3 (Line 37869, Address `0x180074100`)
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

### Call Site #4 (Line 37930, Address `0x180074100`)
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

### Call Site #5 (Line 38053, Address `0x180074100`)
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

### Call Site #6 (Line 130875, Address `0x180074100`)
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

### Call Site #7 (Line 130924, Address `0x180074100`)
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

## `KERNEL32.dll!DeviceIoControl` (7 Call Sites)

### Call Site #1 (Line 26913, Address `0x180074120`)
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

### Call Site #2 (Line 27424, Address `0x180074120`)
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

### Call Site #3 (Line 27536, Address `0x180074120`)
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

### Call Site #4 (Line 27570, Address `0x180074120`)
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

### Call Site #5 (Line 27754, Address `0x180074120`)
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

### Call Site #6 (Line 36418, Address `0x180074120`)
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

### Call Site #7 (Line 36493, Address `0x180074120`)
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

## `SETUPAPI.dll!SetupDiEnumDeviceInterfaces` (1 Call Sites)

### Call Site #1 (Line 29429, Address `0x1800742d8`)
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

### Call Site #1 (Line 29415, Address `0x1800742e8`)
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

### Call Site #1 (Line 29439, Address `0x1800742f0`)
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

### Call Site #2 (Line 29470, Address `0x1800742f0`)
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

## `libusb0.dll!usb_bulk_write` (2 Call Sites)

### Call Site #1 (Line 32544, Address `0x180074340`)
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

### Call Site #2 (Line 32571, Address `0x180074340`)
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

### Call Site #1 (Line 29949, Address `0x180074318`)
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

## `libusb0.dll!usb_control_msg` (23 Call Sites)

### Call Site #1 (Line 27133, Address `0x180074328`)
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

### Call Site #2 (Line 32791, Address `0x180074328`)
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

### Call Site #3 (Line 32820, Address `0x180074328`)
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

### Call Site #4 (Line 33103, Address `0x180074328`)
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

### Call Site #5 (Line 33132, Address `0x180074328`)
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

### Call Site #6 (Line 33248, Address `0x180074328`)
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

### Call Site #7 (Line 33372, Address `0x180074328`)
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

### Call Site #8 (Line 33401, Address `0x180074328`)
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

### Call Site #9 (Line 33550, Address `0x180074328`)
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

### Call Site #10 (Line 33706, Address `0x180074328`)
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

### Call Site #11 (Line 33735, Address `0x180074328`)
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

### Call Site #12 (Line 33864, Address `0x180074328`)
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

### Call Site #13 (Line 33893, Address `0x180074328`)
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

### Call Site #14 (Line 34029, Address `0x180074328`)
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

### Call Site #15 (Line 34147, Address `0x180074328`)
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

### Call Site #16 (Line 34319, Address `0x180074328`)
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

### Call Site #17 (Line 34447, Address `0x180074328`)
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

### Call Site #18 (Line 34567, Address `0x180074328`)
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

### Call Site #19 (Line 34688, Address `0x180074328`)
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

### Call Site #20 (Line 34874, Address `0x180074328`)
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

### Call Site #21 (Line 35068, Address `0x180074328`)
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

### Call Site #22 (Line 35249, Address `0x180074328`)
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

### Call Site #23 (Line 35423, Address `0x180074328`)
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

## `libusb0.dll!usb_open` (1 Call Sites)

### Call Site #1 (Line 29647, Address `0x180074338`)
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

