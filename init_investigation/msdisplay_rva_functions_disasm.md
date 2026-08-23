# MSDISPLAYSDKWRRAPER.dll Native Exports Assembly Disassembly

## `Wrraper_MSDisplayStart` (Address: `0x180014700`)
```assembly
   180014700:	e9 2b 0e 00 00       	jmp    0x180015530
   180014705:	cc                   	int3
   180014706:	cc                   	int3
   180014707:	cc                   	int3
   180014708:	cc                   	int3
   180014709:	cc                   	int3
   18001470a:	cc                   	int3
   18001470b:	cc                   	int3
   18001470c:	cc                   	int3
   18001470d:	cc                   	int3
   18001470e:	cc                   	int3
   18001470f:	cc                   	int3
   180014710:	48 83 ec 28          	sub    $0x28,%rsp
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
   180014764:	ba 01 00 00 00       	mov    $0x1,%edx
   180014769:	ff 10                	call   *(%rax)
   18001476b:	48 c7 05 72 3e 09 00 	movq   $0x0,0x93e72(%rip)        # 0x1800a85e8
   180014772:	00 00 00 00 
   180014776:	48 8b 0d 8b 3e 09 00 	mov    0x93e8b(%rip),%rcx        # 0x1800a8608
   18001477d:	48 8d 15 74 61 08 00 	lea    0x86174(%rip),%rdx        # 0x18009a8f8
   180014784:	e8 57 1b 00 00       	call   0x1800162e0
   180014789:	48 8b 0d 50 3e 09 00 	mov    0x93e50(%rip),%rcx        # 0x1800a85e0
   180014790:	48 85 c9             	test   %rcx,%rcx
   180014793:	74 0b                	je     0x1800147a0
   180014795:	4c 8b 01             	mov    (%rcx),%r8
   180014798:	ba 01 00 00 00       	mov    $0x1,%edx
   18001479d:	41 ff 10             	call   *(%r8)
   1800147a0:	c7 05 56 3e 09 00 02 	movl   $0x2,0x93e56(%rip)        # 0x1800a8600
   1800147a7:	00 00 00 
   1800147aa:	33 c0                	xor    %eax,%eax
   1800147ac:	48 83 c4 28          	add    $0x28,%rsp
   1800147b0:	c3                   	ret
   1800147b1:	cc                   	int3
   1800147b2:	cc                   	int3
   1800147b3:	cc                   	int3
   1800147b4:	cc                   	int3
   1800147b5:	cc                   	int3
   1800147b6:	cc                   	int3
   1800147b7:	cc                   	int3
   1800147b8:	cc                   	int3
   1800147b9:	cc                   	int3
   1800147ba:	cc                   	int3
   1800147bb:	cc                   	int3
   1800147bc:	cc                   	int3
   1800147bd:	cc                   	int3
   1800147be:	cc                   	int3
   1800147bf:	cc                   	int3
   1800147c0:	48 89 0d 29 3e 09 00 	mov    %rcx,0x93e29(%rip)        # 0x1800a85f0
   1800147c7:	48 89 15 2a 3e 09 00 	mov    %rdx,0x93e2a(%rip)        # 0x1800a85f8
   1800147ce:	c3                   	ret
   1800147cf:	cc                   	int3
   1800147d0:	c7 01 03 00 00 00    	movl   $0x3,(%rcx)
   1800147d6:	c7 41 04 02 00 00 00 	movl   $0x2,0x4(%rcx)
   1800147dd:	c7 41 08 07 00 00 00 	movl   $0x7,0x8(%rcx)
   1800147e4:	c7 41 0c 24 00 00 00 	movl   $0x24,0xc(%rcx)
   1800147eb:	c3                   	ret
   1800147ec:	cc                   	int3
   1800147ed:	cc                   	int3
   1800147ee:	cc                   	int3
   1800147ef:	cc                   	int3
   1800147f0:	40 53                	rex push %rbx
   1800147f2:	56                   	push   %rsi
   1800147f3:	57                   	push   %rdi
   1800147f4:	48 81 ec b0 00 00 00 	sub    $0xb0,%rsp
   1800147fb:	48 8b 05 5e 1b 09 00 	mov    0x91b5e(%rip),%rax        # 0x1800a6360
   180014802:	48 33 c4             	xor    %rsp,%rax
   180014805:	48 89 84 24 a0 00 00 	mov    %rax,0xa0(%rsp)
   18001480c:	00 
   18001480d:	83 3d ec 3d 09 00 01 	cmpl   $0x1,0x93dec(%rip)        # 0x1800a8600
   180014814:	49 8b f0             	mov    %r8,%rsi
   180014817:	48 63 da             	movslq %edx,%rbx
   18001481a:	48 8b f9             	mov    %rcx,%rdi
   18001481d:	74 07                	je     0x180014826
   18001481f:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014824:	eb 38                	jmp    0x18001485e
   180014826:	48 8b 0d eb 3d 09 00 	mov    0x93deb(%rip),%rcx        # 0x1800a8618
   18001482d:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014832:	e8 49 4f 00 00       	call   0x180019780
   180014837:	89 06                	mov    %eax,(%rsi)
   180014839:	85 c0                	test   %eax,%eax
   18001483b:	74 1f                	je     0x18001485c
```

## `Wrraper_MSDisplayStop` (Address: `0x180014710`)
```assembly
   180014710:	48 83 ec 28          	sub    $0x28,%rsp
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
   180014764:	ba 01 00 00 00       	mov    $0x1,%edx
   180014769:	ff 10                	call   *(%rax)
   18001476b:	48 c7 05 72 3e 09 00 	movq   $0x0,0x93e72(%rip)        # 0x1800a85e8
   180014772:	00 00 00 00 
   180014776:	48 8b 0d 8b 3e 09 00 	mov    0x93e8b(%rip),%rcx        # 0x1800a8608
   18001477d:	48 8d 15 74 61 08 00 	lea    0x86174(%rip),%rdx        # 0x18009a8f8
   180014784:	e8 57 1b 00 00       	call   0x1800162e0
   180014789:	48 8b 0d 50 3e 09 00 	mov    0x93e50(%rip),%rcx        # 0x1800a85e0
   180014790:	48 85 c9             	test   %rcx,%rcx
   180014793:	74 0b                	je     0x1800147a0
   180014795:	4c 8b 01             	mov    (%rcx),%r8
   180014798:	ba 01 00 00 00       	mov    $0x1,%edx
   18001479d:	41 ff 10             	call   *(%r8)
   1800147a0:	c7 05 56 3e 09 00 02 	movl   $0x2,0x93e56(%rip)        # 0x1800a8600
   1800147a7:	00 00 00 
   1800147aa:	33 c0                	xor    %eax,%eax
   1800147ac:	48 83 c4 28          	add    $0x28,%rsp
   1800147b0:	c3                   	ret
   1800147b1:	cc                   	int3
   1800147b2:	cc                   	int3
   1800147b3:	cc                   	int3
   1800147b4:	cc                   	int3
   1800147b5:	cc                   	int3
   1800147b6:	cc                   	int3
   1800147b7:	cc                   	int3
   1800147b8:	cc                   	int3
   1800147b9:	cc                   	int3
   1800147ba:	cc                   	int3
   1800147bb:	cc                   	int3
   1800147bc:	cc                   	int3
   1800147bd:	cc                   	int3
   1800147be:	cc                   	int3
   1800147bf:	cc                   	int3
   1800147c0:	48 89 0d 29 3e 09 00 	mov    %rcx,0x93e29(%rip)        # 0x1800a85f0
   1800147c7:	48 89 15 2a 3e 09 00 	mov    %rdx,0x93e2a(%rip)        # 0x1800a85f8
   1800147ce:	c3                   	ret
   1800147cf:	cc                   	int3
   1800147d0:	c7 01 03 00 00 00    	movl   $0x3,(%rcx)
   1800147d6:	c7 41 04 02 00 00 00 	movl   $0x2,0x4(%rcx)
   1800147dd:	c7 41 08 07 00 00 00 	movl   $0x7,0x8(%rcx)
   1800147e4:	c7 41 0c 24 00 00 00 	movl   $0x24,0xc(%rcx)
   1800147eb:	c3                   	ret
   1800147ec:	cc                   	int3
   1800147ed:	cc                   	int3
   1800147ee:	cc                   	int3
   1800147ef:	cc                   	int3
   1800147f0:	40 53                	rex push %rbx
   1800147f2:	56                   	push   %rsi
   1800147f3:	57                   	push   %rdi
   1800147f4:	48 81 ec b0 00 00 00 	sub    $0xb0,%rsp
   1800147fb:	48 8b 05 5e 1b 09 00 	mov    0x91b5e(%rip),%rax        # 0x1800a6360
   180014802:	48 33 c4             	xor    %rsp,%rax
   180014805:	48 89 84 24 a0 00 00 	mov    %rax,0xa0(%rsp)
   18001480c:	00 
   18001480d:	83 3d ec 3d 09 00 01 	cmpl   $0x1,0x93dec(%rip)        # 0x1800a8600
   180014814:	49 8b f0             	mov    %r8,%rsi
   180014817:	48 63 da             	movslq %edx,%rbx
   18001481a:	48 8b f9             	mov    %rcx,%rdi
   18001481d:	74 07                	je     0x180014826
   18001481f:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014824:	eb 38                	jmp    0x18001485e
   180014826:	48 8b 0d eb 3d 09 00 	mov    0x93deb(%rip),%rcx        # 0x1800a8618
   18001482d:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014832:	e8 49 4f 00 00       	call   0x180019780
   180014837:	89 06                	mov    %eax,(%rsi)
   180014839:	85 c0                	test   %eax,%eax
   18001483b:	74 1f                	je     0x18001485c
   18001483d:	85 db                	test   %ebx,%ebx
   18001483f:	74 1b                	je     0x18001485c
   180014841:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014846:	48 8b cf             	mov    %rdi,%rcx
   180014849:	4c 8b c3             	mov    %rbx,%r8
   18001484c:	3b d8                	cmp    %eax,%ebx
   18001484e:	7c 03                	jl     0x180014853
   180014850:	4c 63 c0             	movslq %eax,%r8
   180014853:	49 c1 e0 03          	shl    $0x3,%r8
   180014857:	e8 74 21 04 00       	call   0x1800569d0
   18001485c:	33 c0                	xor    %eax,%eax
   18001485e:	48 8b 8c 24 a0 00 00 	mov    0xa0(%rsp),%rcx
```

## `Wrraper_MSDisplayRegisterCallback` (Address: `0x1800147c0`)
```assembly
   1800147c0:	48 89 0d 29 3e 09 00 	mov    %rcx,0x93e29(%rip)        # 0x1800a85f0
   1800147c7:	48 89 15 2a 3e 09 00 	mov    %rdx,0x93e2a(%rip)        # 0x1800a85f8
   1800147ce:	c3                   	ret
   1800147cf:	cc                   	int3
   1800147d0:	c7 01 03 00 00 00    	movl   $0x3,(%rcx)
   1800147d6:	c7 41 04 02 00 00 00 	movl   $0x2,0x4(%rcx)
   1800147dd:	c7 41 08 07 00 00 00 	movl   $0x7,0x8(%rcx)
   1800147e4:	c7 41 0c 24 00 00 00 	movl   $0x24,0xc(%rcx)
   1800147eb:	c3                   	ret
   1800147ec:	cc                   	int3
   1800147ed:	cc                   	int3
   1800147ee:	cc                   	int3
   1800147ef:	cc                   	int3
   1800147f0:	40 53                	rex push %rbx
   1800147f2:	56                   	push   %rsi
   1800147f3:	57                   	push   %rdi
   1800147f4:	48 81 ec b0 00 00 00 	sub    $0xb0,%rsp
   1800147fb:	48 8b 05 5e 1b 09 00 	mov    0x91b5e(%rip),%rax        # 0x1800a6360
   180014802:	48 33 c4             	xor    %rsp,%rax
   180014805:	48 89 84 24 a0 00 00 	mov    %rax,0xa0(%rsp)
   18001480c:	00 
   18001480d:	83 3d ec 3d 09 00 01 	cmpl   $0x1,0x93dec(%rip)        # 0x1800a8600
   180014814:	49 8b f0             	mov    %r8,%rsi
   180014817:	48 63 da             	movslq %edx,%rbx
   18001481a:	48 8b f9             	mov    %rcx,%rdi
   18001481d:	74 07                	je     0x180014826
   18001481f:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014824:	eb 38                	jmp    0x18001485e
   180014826:	48 8b 0d eb 3d 09 00 	mov    0x93deb(%rip),%rcx        # 0x1800a8618
   18001482d:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014832:	e8 49 4f 00 00       	call   0x180019780
   180014837:	89 06                	mov    %eax,(%rsi)
   180014839:	85 c0                	test   %eax,%eax
   18001483b:	74 1f                	je     0x18001485c
   18001483d:	85 db                	test   %ebx,%ebx
   18001483f:	74 1b                	je     0x18001485c
   180014841:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014846:	48 8b cf             	mov    %rdi,%rcx
   180014849:	4c 8b c3             	mov    %rbx,%r8
   18001484c:	3b d8                	cmp    %eax,%ebx
   18001484e:	7c 03                	jl     0x180014853
   180014850:	4c 63 c0             	movslq %eax,%r8
   180014853:	49 c1 e0 03          	shl    $0x3,%r8
   180014857:	e8 74 21 04 00       	call   0x1800569d0
   18001485c:	33 c0                	xor    %eax,%eax
   18001485e:	48 8b 8c 24 a0 00 00 	mov    0xa0(%rsp),%rcx
   180014865:	00 
   180014866:	48 33 cc             	xor    %rsp,%rcx
   180014869:	e8 b2 03 04 00       	call   0x180054c20
   18001486e:	48 81 c4 b0 00 00 00 	add    $0xb0,%rsp
   180014875:	5f                   	pop    %rdi
   180014876:	5e                   	pop    %rsi
   180014877:	5b                   	pop    %rbx
   180014878:	c3                   	ret
   180014879:	cc                   	int3
   18001487a:	cc                   	int3
   18001487b:	cc                   	int3
   18001487c:	cc                   	int3
   18001487d:	cc                   	int3
   18001487e:	cc                   	int3
   18001487f:	cc                   	int3
   180014880:	83 3d 79 3d 09 00 01 	cmpl   $0x1,0x93d79(%rip)        # 0x1800a8600
   180014887:	74 06                	je     0x18001488f
   180014889:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001488e:	c3                   	ret
   18001488f:	4c 8b c2             	mov    %rdx,%r8
   180014892:	8b d1                	mov    %ecx,%edx
   180014894:	48 8b 0d 7d 3d 09 00 	mov    0x93d7d(%rip),%rcx        # 0x1800a8618
   18001489b:	e9 c0 52 00 00       	jmp    0x180019b60
   1800148a0:	40 53                	rex push %rbx
   1800148a2:	48 83 ec 70          	sub    $0x70,%rsp
   1800148a6:	83 3d 53 3d 09 00 01 	cmpl   $0x1,0x93d53(%rip)        # 0x1800a8600
   1800148ad:	8b d9                	mov    %ecx,%ebx
   1800148af:	74 0b                	je     0x1800148bc
   1800148b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800148b6:	48 83 c4 70          	add    $0x70,%rsp
   1800148ba:	5b                   	pop    %rbx
   1800148bb:	c3                   	ret
   1800148bc:	48 89 ac 24 80 00 00 	mov    %rbp,0x80(%rsp)
   1800148c3:	00 
   1800148c4:	8b c3                	mov    %ebx,%eax
   1800148c6:	8b 6a 04             	mov    0x4(%rdx),%ebp
   1800148c9:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800148ce:	48 89 74 24 68       	mov    %rsi,0x68(%rsp)
   1800148d3:	48 8b 35 3e 3d 09 00 	mov    0x93d3e(%rip),%rsi        # 0x1800a8618
   1800148da:	48 89 7c 24 60       	mov    %rdi,0x60(%rsp)
   1800148df:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   1800148e4:	4c 89 7c 24 50       	mov    %r15,0x50(%rsp)
   1800148e9:	44 8b 3a             	mov    (%rdx),%r15d
   1800148ec:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800148f1:	75 25                	jne    0x180014918
   1800148f3:	0f b6 c3             	movzbl %bl,%eax
   1800148f6:	83 f8 06             	cmp    $0x6,%eax
   1800148f9:	0f 83 46 01 00 00    	jae    0x180014a45
   1800148ff:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014903:	80 bc ce 00 04 00 00 	cmpb   $0x0,0x400(%rsi,%rcx,8)
   18001490a:	00 
   18001490b:	0f 84 34 01 00 00    	je     0x180014a45
   180014911:	33 ff                	xor    %edi,%edi
   180014913:	e9 2d 01 00 00       	jmp    0x180014a45
```

## `Wrraper_MSDisplayGetSDKVersion` (Address: `0x1800147d0`)
```assembly
   1800147d0:	c7 01 03 00 00 00    	movl   $0x3,(%rcx)
   1800147d6:	c7 41 04 02 00 00 00 	movl   $0x2,0x4(%rcx)
   1800147dd:	c7 41 08 07 00 00 00 	movl   $0x7,0x8(%rcx)
   1800147e4:	c7 41 0c 24 00 00 00 	movl   $0x24,0xc(%rcx)
   1800147eb:	c3                   	ret
   1800147ec:	cc                   	int3
   1800147ed:	cc                   	int3
   1800147ee:	cc                   	int3
   1800147ef:	cc                   	int3
   1800147f0:	40 53                	rex push %rbx
   1800147f2:	56                   	push   %rsi
   1800147f3:	57                   	push   %rdi
   1800147f4:	48 81 ec b0 00 00 00 	sub    $0xb0,%rsp
   1800147fb:	48 8b 05 5e 1b 09 00 	mov    0x91b5e(%rip),%rax        # 0x1800a6360
   180014802:	48 33 c4             	xor    %rsp,%rax
   180014805:	48 89 84 24 a0 00 00 	mov    %rax,0xa0(%rsp)
   18001480c:	00 
   18001480d:	83 3d ec 3d 09 00 01 	cmpl   $0x1,0x93dec(%rip)        # 0x1800a8600
   180014814:	49 8b f0             	mov    %r8,%rsi
   180014817:	48 63 da             	movslq %edx,%rbx
   18001481a:	48 8b f9             	mov    %rcx,%rdi
   18001481d:	74 07                	je     0x180014826
   18001481f:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014824:	eb 38                	jmp    0x18001485e
   180014826:	48 8b 0d eb 3d 09 00 	mov    0x93deb(%rip),%rcx        # 0x1800a8618
   18001482d:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014832:	e8 49 4f 00 00       	call   0x180019780
   180014837:	89 06                	mov    %eax,(%rsi)
   180014839:	85 c0                	test   %eax,%eax
   18001483b:	74 1f                	je     0x18001485c
   18001483d:	85 db                	test   %ebx,%ebx
   18001483f:	74 1b                	je     0x18001485c
   180014841:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014846:	48 8b cf             	mov    %rdi,%rcx
   180014849:	4c 8b c3             	mov    %rbx,%r8
   18001484c:	3b d8                	cmp    %eax,%ebx
   18001484e:	7c 03                	jl     0x180014853
   180014850:	4c 63 c0             	movslq %eax,%r8
   180014853:	49 c1 e0 03          	shl    $0x3,%r8
   180014857:	e8 74 21 04 00       	call   0x1800569d0
   18001485c:	33 c0                	xor    %eax,%eax
   18001485e:	48 8b 8c 24 a0 00 00 	mov    0xa0(%rsp),%rcx
   180014865:	00 
   180014866:	48 33 cc             	xor    %rsp,%rcx
   180014869:	e8 b2 03 04 00       	call   0x180054c20
   18001486e:	48 81 c4 b0 00 00 00 	add    $0xb0,%rsp
   180014875:	5f                   	pop    %rdi
   180014876:	5e                   	pop    %rsi
   180014877:	5b                   	pop    %rbx
   180014878:	c3                   	ret
   180014879:	cc                   	int3
   18001487a:	cc                   	int3
   18001487b:	cc                   	int3
   18001487c:	cc                   	int3
   18001487d:	cc                   	int3
   18001487e:	cc                   	int3
   18001487f:	cc                   	int3
   180014880:	83 3d 79 3d 09 00 01 	cmpl   $0x1,0x93d79(%rip)        # 0x1800a8600
   180014887:	74 06                	je     0x18001488f
   180014889:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001488e:	c3                   	ret
   18001488f:	4c 8b c2             	mov    %rdx,%r8
   180014892:	8b d1                	mov    %ecx,%edx
   180014894:	48 8b 0d 7d 3d 09 00 	mov    0x93d7d(%rip),%rcx        # 0x1800a8618
   18001489b:	e9 c0 52 00 00       	jmp    0x180019b60
   1800148a0:	40 53                	rex push %rbx
   1800148a2:	48 83 ec 70          	sub    $0x70,%rsp
   1800148a6:	83 3d 53 3d 09 00 01 	cmpl   $0x1,0x93d53(%rip)        # 0x1800a8600
   1800148ad:	8b d9                	mov    %ecx,%ebx
   1800148af:	74 0b                	je     0x1800148bc
   1800148b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800148b6:	48 83 c4 70          	add    $0x70,%rsp
   1800148ba:	5b                   	pop    %rbx
   1800148bb:	c3                   	ret
   1800148bc:	48 89 ac 24 80 00 00 	mov    %rbp,0x80(%rsp)
   1800148c3:	00 
   1800148c4:	8b c3                	mov    %ebx,%eax
   1800148c6:	8b 6a 04             	mov    0x4(%rdx),%ebp
   1800148c9:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800148ce:	48 89 74 24 68       	mov    %rsi,0x68(%rsp)
   1800148d3:	48 8b 35 3e 3d 09 00 	mov    0x93d3e(%rip),%rsi        # 0x1800a8618
   1800148da:	48 89 7c 24 60       	mov    %rdi,0x60(%rsp)
   1800148df:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   1800148e4:	4c 89 7c 24 50       	mov    %r15,0x50(%rsp)
   1800148e9:	44 8b 3a             	mov    (%rdx),%r15d
   1800148ec:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800148f1:	75 25                	jne    0x180014918
   1800148f3:	0f b6 c3             	movzbl %bl,%eax
   1800148f6:	83 f8 06             	cmp    $0x6,%eax
   1800148f9:	0f 83 46 01 00 00    	jae    0x180014a45
   1800148ff:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014903:	80 bc ce 00 04 00 00 	cmpb   $0x0,0x400(%rsi,%rcx,8)
   18001490a:	00 
   18001490b:	0f 84 34 01 00 00    	je     0x180014a45
   180014911:	33 ff                	xor    %edi,%edi
   180014913:	e9 2d 01 00 00       	jmp    0x180014a45
   180014918:	48 8b 86 10 02 00 00 	mov    0x210(%rsi),%rax
   18001491f:	48 8d 8e 10 02 00 00 	lea    0x210(%rsi),%rcx
   180014926:	4c 89 74 24 58       	mov    %r14,0x58(%rsp)
   18001492b:	ff 50 08             	call   *0x8(%rax)
```

## `Wrraper_MSDisplayGetDeviceList` (Address: `0x1800147f0`)
```assembly
   1800147f0:	40 53                	rex push %rbx
   1800147f2:	56                   	push   %rsi
   1800147f3:	57                   	push   %rdi
   1800147f4:	48 81 ec b0 00 00 00 	sub    $0xb0,%rsp
   1800147fb:	48 8b 05 5e 1b 09 00 	mov    0x91b5e(%rip),%rax        # 0x1800a6360
   180014802:	48 33 c4             	xor    %rsp,%rax
   180014805:	48 89 84 24 a0 00 00 	mov    %rax,0xa0(%rsp)
   18001480c:	00 
   18001480d:	83 3d ec 3d 09 00 01 	cmpl   $0x1,0x93dec(%rip)        # 0x1800a8600
   180014814:	49 8b f0             	mov    %r8,%rsi
   180014817:	48 63 da             	movslq %edx,%rbx
   18001481a:	48 8b f9             	mov    %rcx,%rdi
   18001481d:	74 07                	je     0x180014826
   18001481f:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014824:	eb 38                	jmp    0x18001485e
   180014826:	48 8b 0d eb 3d 09 00 	mov    0x93deb(%rip),%rcx        # 0x1800a8618
   18001482d:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014832:	e8 49 4f 00 00       	call   0x180019780
   180014837:	89 06                	mov    %eax,(%rsi)
   180014839:	85 c0                	test   %eax,%eax
   18001483b:	74 1f                	je     0x18001485c
   18001483d:	85 db                	test   %ebx,%ebx
   18001483f:	74 1b                	je     0x18001485c
   180014841:	48 8d 54 24 20       	lea    0x20(%rsp),%rdx
   180014846:	48 8b cf             	mov    %rdi,%rcx
   180014849:	4c 8b c3             	mov    %rbx,%r8
   18001484c:	3b d8                	cmp    %eax,%ebx
   18001484e:	7c 03                	jl     0x180014853
   180014850:	4c 63 c0             	movslq %eax,%r8
   180014853:	49 c1 e0 03          	shl    $0x3,%r8
   180014857:	e8 74 21 04 00       	call   0x1800569d0
   18001485c:	33 c0                	xor    %eax,%eax
   18001485e:	48 8b 8c 24 a0 00 00 	mov    0xa0(%rsp),%rcx
   180014865:	00 
   180014866:	48 33 cc             	xor    %rsp,%rcx
   180014869:	e8 b2 03 04 00       	call   0x180054c20
   18001486e:	48 81 c4 b0 00 00 00 	add    $0xb0,%rsp
   180014875:	5f                   	pop    %rdi
   180014876:	5e                   	pop    %rsi
   180014877:	5b                   	pop    %rbx
   180014878:	c3                   	ret
   180014879:	cc                   	int3
   18001487a:	cc                   	int3
   18001487b:	cc                   	int3
   18001487c:	cc                   	int3
   18001487d:	cc                   	int3
   18001487e:	cc                   	int3
   18001487f:	cc                   	int3
   180014880:	83 3d 79 3d 09 00 01 	cmpl   $0x1,0x93d79(%rip)        # 0x1800a8600
   180014887:	74 06                	je     0x18001488f
   180014889:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001488e:	c3                   	ret
   18001488f:	4c 8b c2             	mov    %rdx,%r8
   180014892:	8b d1                	mov    %ecx,%edx
   180014894:	48 8b 0d 7d 3d 09 00 	mov    0x93d7d(%rip),%rcx        # 0x1800a8618
   18001489b:	e9 c0 52 00 00       	jmp    0x180019b60
   1800148a0:	40 53                	rex push %rbx
   1800148a2:	48 83 ec 70          	sub    $0x70,%rsp
   1800148a6:	83 3d 53 3d 09 00 01 	cmpl   $0x1,0x93d53(%rip)        # 0x1800a8600
   1800148ad:	8b d9                	mov    %ecx,%ebx
   1800148af:	74 0b                	je     0x1800148bc
   1800148b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800148b6:	48 83 c4 70          	add    $0x70,%rsp
   1800148ba:	5b                   	pop    %rbx
   1800148bb:	c3                   	ret
   1800148bc:	48 89 ac 24 80 00 00 	mov    %rbp,0x80(%rsp)
   1800148c3:	00 
   1800148c4:	8b c3                	mov    %ebx,%eax
   1800148c6:	8b 6a 04             	mov    0x4(%rdx),%ebp
   1800148c9:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800148ce:	48 89 74 24 68       	mov    %rsi,0x68(%rsp)
   1800148d3:	48 8b 35 3e 3d 09 00 	mov    0x93d3e(%rip),%rsi        # 0x1800a8618
   1800148da:	48 89 7c 24 60       	mov    %rdi,0x60(%rsp)
   1800148df:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   1800148e4:	4c 89 7c 24 50       	mov    %r15,0x50(%rsp)
   1800148e9:	44 8b 3a             	mov    (%rdx),%r15d
   1800148ec:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800148f1:	75 25                	jne    0x180014918
   1800148f3:	0f b6 c3             	movzbl %bl,%eax
   1800148f6:	83 f8 06             	cmp    $0x6,%eax
   1800148f9:	0f 83 46 01 00 00    	jae    0x180014a45
   1800148ff:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014903:	80 bc ce 00 04 00 00 	cmpb   $0x0,0x400(%rsi,%rcx,8)
   18001490a:	00 
   18001490b:	0f 84 34 01 00 00    	je     0x180014a45
   180014911:	33 ff                	xor    %edi,%edi
   180014913:	e9 2d 01 00 00       	jmp    0x180014a45
   180014918:	48 8b 86 10 02 00 00 	mov    0x210(%rsi),%rax
   18001491f:	48 8d 8e 10 02 00 00 	lea    0x210(%rsi),%rcx
   180014926:	4c 89 74 24 58       	mov    %r14,0x58(%rsp)
   18001492b:	ff 50 08             	call   *0x8(%rax)
   18001492e:	33 d2                	xor    %edx,%edx
   180014930:	48 8d 86 88 02 00 00 	lea    0x288(%rsi),%rax
   180014937:	33 c9                	xor    %ecx,%ecx
   180014939:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   180014940:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014944:	74 04                	je     0x18001494a
   180014946:	39 18                	cmp    %ebx,(%rax)
   180014948:	74 14                	je     0x18001495e
   18001494a:	ff c2                	inc    %edx
```

## `Wrraper_MSDisplayGetDeviceInfo` (Address: `0x180014880`)
```assembly
   180014880:	83 3d 79 3d 09 00 01 	cmpl   $0x1,0x93d79(%rip)        # 0x1800a8600
   180014887:	74 06                	je     0x18001488f
   180014889:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001488e:	c3                   	ret
   18001488f:	4c 8b c2             	mov    %rdx,%r8
   180014892:	8b d1                	mov    %ecx,%edx
   180014894:	48 8b 0d 7d 3d 09 00 	mov    0x93d7d(%rip),%rcx        # 0x1800a8618
   18001489b:	e9 c0 52 00 00       	jmp    0x180019b60
   1800148a0:	40 53                	rex push %rbx
   1800148a2:	48 83 ec 70          	sub    $0x70,%rsp
   1800148a6:	83 3d 53 3d 09 00 01 	cmpl   $0x1,0x93d53(%rip)        # 0x1800a8600
   1800148ad:	8b d9                	mov    %ecx,%ebx
   1800148af:	74 0b                	je     0x1800148bc
   1800148b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800148b6:	48 83 c4 70          	add    $0x70,%rsp
   1800148ba:	5b                   	pop    %rbx
   1800148bb:	c3                   	ret
   1800148bc:	48 89 ac 24 80 00 00 	mov    %rbp,0x80(%rsp)
   1800148c3:	00 
   1800148c4:	8b c3                	mov    %ebx,%eax
   1800148c6:	8b 6a 04             	mov    0x4(%rdx),%ebp
   1800148c9:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800148ce:	48 89 74 24 68       	mov    %rsi,0x68(%rsp)
   1800148d3:	48 8b 35 3e 3d 09 00 	mov    0x93d3e(%rip),%rsi        # 0x1800a8618
   1800148da:	48 89 7c 24 60       	mov    %rdi,0x60(%rsp)
   1800148df:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   1800148e4:	4c 89 7c 24 50       	mov    %r15,0x50(%rsp)
   1800148e9:	44 8b 3a             	mov    (%rdx),%r15d
   1800148ec:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800148f1:	75 25                	jne    0x180014918
   1800148f3:	0f b6 c3             	movzbl %bl,%eax
   1800148f6:	83 f8 06             	cmp    $0x6,%eax
   1800148f9:	0f 83 46 01 00 00    	jae    0x180014a45
   1800148ff:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014903:	80 bc ce 00 04 00 00 	cmpb   $0x0,0x400(%rsi,%rcx,8)
   18001490a:	00 
   18001490b:	0f 84 34 01 00 00    	je     0x180014a45
   180014911:	33 ff                	xor    %edi,%edi
   180014913:	e9 2d 01 00 00       	jmp    0x180014a45
   180014918:	48 8b 86 10 02 00 00 	mov    0x210(%rsi),%rax
   18001491f:	48 8d 8e 10 02 00 00 	lea    0x210(%rsi),%rcx
   180014926:	4c 89 74 24 58       	mov    %r14,0x58(%rsp)
   18001492b:	ff 50 08             	call   *0x8(%rax)
   18001492e:	33 d2                	xor    %edx,%edx
   180014930:	48 8d 86 88 02 00 00 	lea    0x288(%rsi),%rax
   180014937:	33 c9                	xor    %ecx,%ecx
   180014939:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   180014940:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014944:	74 04                	je     0x18001494a
   180014946:	39 18                	cmp    %ebx,(%rax)
   180014948:	74 14                	je     0x18001495e
   18001494a:	ff c2                	inc    %edx
   18001494c:	48 ff c1             	inc    %rcx
   18001494f:	48 83 c0 18          	add    $0x18,%rax
   180014953:	48 83 f9 10          	cmp    $0x10,%rcx
   180014957:	7c e7                	jl     0x180014940
   180014959:	e9 d1 00 00 00       	jmp    0x180014a2f
   18001495e:	48 63 c2             	movslq %edx,%rax
   180014961:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014965:	48 8b 9c ce 80 02 00 	mov    0x280(%rsi,%rcx,8),%rbx
   18001496c:	00 
   18001496d:	48 85 db             	test   %rbx,%rbx
   180014970:	0f 84 b9 00 00 00    	je     0x180014a2f
   180014976:	8b 43 18             	mov    0x18(%rbx),%eax
   180014979:	83 e8 02             	sub    $0x2,%eax
   18001497c:	83 f8 01             	cmp    $0x1,%eax
   18001497f:	76 0a                	jbe    0x18001498b
   180014981:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014986:	e9 a4 00 00 00       	jmp    0x180014a2f
   18001498b:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   180014990:	44 8b c5             	mov    %ebp,%r8d
   180014993:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   180014998:	41 8b d7             	mov    %r15d,%edx
   18001499b:	48 8d 84 24 98 00 00 	lea    0x98(%rsp),%rax
   1800149a2:	00 
   1800149a3:	48 8b cb             	mov    %rbx,%rcx
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
   180014a04:	44 8b 83 84 00 00 00 	mov    0x84(%rbx),%r8d
   180014a0b:	48 8d 15 4e 8b 08 00 	lea    0x88b4e(%rip),%rdx        # 0x18009d560
   180014a12:	48 8b 0d ef 3b 09 00 	mov    0x93bef(%rip),%rcx        # 0x1800a8608
   180014a19:	c7 44 24 20 03 00 00 	movl   $0x3,0x20(%rsp)
```

## `Wrraper_MSDisplaySetVideoParam` (Address: `0x1800148a0`)
```assembly
   1800148a0:	40 53                	rex push %rbx
   1800148a2:	48 83 ec 70          	sub    $0x70,%rsp
   1800148a6:	83 3d 53 3d 09 00 01 	cmpl   $0x1,0x93d53(%rip)        # 0x1800a8600
   1800148ad:	8b d9                	mov    %ecx,%ebx
   1800148af:	74 0b                	je     0x1800148bc
   1800148b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800148b6:	48 83 c4 70          	add    $0x70,%rsp
   1800148ba:	5b                   	pop    %rbx
   1800148bb:	c3                   	ret
   1800148bc:	48 89 ac 24 80 00 00 	mov    %rbp,0x80(%rsp)
   1800148c3:	00 
   1800148c4:	8b c3                	mov    %ebx,%eax
   1800148c6:	8b 6a 04             	mov    0x4(%rdx),%ebp
   1800148c9:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800148ce:	48 89 74 24 68       	mov    %rsi,0x68(%rsp)
   1800148d3:	48 8b 35 3e 3d 09 00 	mov    0x93d3e(%rip),%rsi        # 0x1800a8618
   1800148da:	48 89 7c 24 60       	mov    %rdi,0x60(%rsp)
   1800148df:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   1800148e4:	4c 89 7c 24 50       	mov    %r15,0x50(%rsp)
   1800148e9:	44 8b 3a             	mov    (%rdx),%r15d
   1800148ec:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800148f1:	75 25                	jne    0x180014918
   1800148f3:	0f b6 c3             	movzbl %bl,%eax
   1800148f6:	83 f8 06             	cmp    $0x6,%eax
   1800148f9:	0f 83 46 01 00 00    	jae    0x180014a45
   1800148ff:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014903:	80 bc ce 00 04 00 00 	cmpb   $0x0,0x400(%rsi,%rcx,8)
   18001490a:	00 
   18001490b:	0f 84 34 01 00 00    	je     0x180014a45
   180014911:	33 ff                	xor    %edi,%edi
   180014913:	e9 2d 01 00 00       	jmp    0x180014a45
   180014918:	48 8b 86 10 02 00 00 	mov    0x210(%rsi),%rax
   18001491f:	48 8d 8e 10 02 00 00 	lea    0x210(%rsi),%rcx
   180014926:	4c 89 74 24 58       	mov    %r14,0x58(%rsp)
   18001492b:	ff 50 08             	call   *0x8(%rax)
   18001492e:	33 d2                	xor    %edx,%edx
   180014930:	48 8d 86 88 02 00 00 	lea    0x288(%rsi),%rax
   180014937:	33 c9                	xor    %ecx,%ecx
   180014939:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   180014940:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014944:	74 04                	je     0x18001494a
   180014946:	39 18                	cmp    %ebx,(%rax)
   180014948:	74 14                	je     0x18001495e
   18001494a:	ff c2                	inc    %edx
   18001494c:	48 ff c1             	inc    %rcx
   18001494f:	48 83 c0 18          	add    $0x18,%rax
   180014953:	48 83 f9 10          	cmp    $0x10,%rcx
   180014957:	7c e7                	jl     0x180014940
   180014959:	e9 d1 00 00 00       	jmp    0x180014a2f
   18001495e:	48 63 c2             	movslq %edx,%rax
   180014961:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014965:	48 8b 9c ce 80 02 00 	mov    0x280(%rsi,%rcx,8),%rbx
   18001496c:	00 
   18001496d:	48 85 db             	test   %rbx,%rbx
   180014970:	0f 84 b9 00 00 00    	je     0x180014a2f
   180014976:	8b 43 18             	mov    0x18(%rbx),%eax
   180014979:	83 e8 02             	sub    $0x2,%eax
   18001497c:	83 f8 01             	cmp    $0x1,%eax
   18001497f:	76 0a                	jbe    0x18001498b
   180014981:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014986:	e9 a4 00 00 00       	jmp    0x180014a2f
   18001498b:	48 8d 44 24 40       	lea    0x40(%rsp),%rax
   180014990:	44 8b c5             	mov    %ebp,%r8d
   180014993:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
   180014998:	41 8b d7             	mov    %r15d,%edx
   18001499b:	48 8d 84 24 98 00 00 	lea    0x98(%rsp),%rax
   1800149a2:	00 
   1800149a3:	48 8b cb             	mov    %rbx,%rcx
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
   180014a04:	44 8b 83 84 00 00 00 	mov    0x84(%rbx),%r8d
   180014a0b:	48 8d 15 4e 8b 08 00 	lea    0x88b4e(%rip),%rdx        # 0x18009d560
   180014a12:	48 8b 0d ef 3b 09 00 	mov    0x93bef(%rip),%rcx        # 0x1800a8608
   180014a19:	c7 44 24 20 03 00 00 	movl   $0x3,0x20(%rsp)
   180014a20:	00 
   180014a21:	e8 6a 18 00 00       	call   0x180016290
   180014a26:	c7 43 18 03 00 00 00 	movl   $0x3,0x18(%rbx)
   180014a2d:	33 ff                	xor    %edi,%edi
   180014a2f:	48 8b 96 10 02 00 00 	mov    0x210(%rsi),%rdx
   180014a36:	48 8d 8e 10 02 00 00 	lea    0x210(%rsi),%rcx
   180014a3d:	ff 52 10             	call   *0x10(%rdx)
   180014a40:	4c 8b 74 24 58       	mov    0x58(%rsp),%r14
```

## `Wrraper_MSDisplaySendPicture` (Address: `0x180014a70`)
```assembly
   180014a70:	48 83 ec 38          	sub    $0x38,%rsp
   180014a74:	83 3d 85 3b 09 00 01 	cmpl   $0x1,0x93b85(%rip)        # 0x1800a8600
   180014a7b:	74 0a                	je     0x180014a87
   180014a7d:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014a82:	48 83 c4 38          	add    $0x38,%rsp
   180014a86:	c3                   	ret
   180014a87:	8b 42 04             	mov    0x4(%rdx),%eax
   180014a8a:	44 8b 0a             	mov    (%rdx),%r9d
   180014a8d:	44 88 44 24 28       	mov    %r8b,0x28(%rsp)
   180014a92:	4c 8b 42 08          	mov    0x8(%rdx),%r8
   180014a96:	8b d1                	mov    %ecx,%edx
   180014a98:	48 8b 0d 79 3b 09 00 	mov    0x93b79(%rip),%rcx        # 0x1800a8618
   180014a9f:	89 44 24 20          	mov    %eax,0x20(%rsp)
   180014aa3:	e8 78 3d 00 00       	call   0x180018820
   180014aa8:	48 83 c4 38          	add    $0x38,%rsp
   180014aac:	c3                   	ret
   180014aad:	cc                   	int3
   180014aae:	cc                   	int3
   180014aaf:	cc                   	int3
   180014ab0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014ab5:	41 54                	push   %r12
   180014ab7:	41 56                	push   %r14
   180014ab9:	41 57                	push   %r15
   180014abb:	48 83 ec 20          	sub    $0x20,%rsp
   180014abf:	83 3d 3a 3b 09 00 01 	cmpl   $0x1,0x93b3a(%rip)        # 0x1800a8600
   180014ac6:	4d 8b f1             	mov    %r9,%r14
   180014ac9:	45 8b f8             	mov    %r8d,%r15d
   180014acc:	44 8b e2             	mov    %edx,%r12d
   180014acf:	8b d9                	mov    %ecx,%ebx
   180014ad1:	74 15                	je     0x180014ae8
   180014ad3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014ad8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014add:	48 83 c4 20          	add    $0x20,%rsp
   180014ae1:	41 5f                	pop    %r15
   180014ae3:	41 5e                	pop    %r14
   180014ae5:	41 5c                	pop    %r12
   180014ae7:	c3                   	ret
   180014ae8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014aed:	48 8b 2d 24 3b 09 00 	mov    0x93b24(%rip),%rbp        # 0x1800a8618
   180014af4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014af9:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014afe:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   180014b03:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014b0a:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014b11:	ff 50 08             	call   *0x8(%rax)
   180014b14:	33 d2                	xor    %edx,%edx
   180014b16:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014b1d:	8b ca                	mov    %edx,%ecx
   180014b1f:	90                   	nop
   180014b20:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014b24:	74 04                	je     0x180014b2a
   180014b26:	39 18                	cmp    %ebx,(%rax)
   180014b28:	74 11                	je     0x180014b3b
   180014b2a:	ff c2                	inc    %edx
   180014b2c:	48 ff c1             	inc    %rcx
   180014b2f:	48 83 c0 18          	add    $0x18,%rax
   180014b33:	48 83 f9 10          	cmp    $0x10,%rcx
   180014b37:	7c e7                	jl     0x180014b20
   180014b39:	eb 39                	jmp    0x180014b74
   180014b3b:	48 63 c2             	movslq %edx,%rax
   180014b3e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014b42:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014b49:	00 
   180014b4a:	48 85 c9             	test   %rcx,%rcx
   180014b4d:	74 25                	je     0x180014b74
   180014b4f:	83 79 18 01          	cmpl   $0x1,0x18(%rcx)
   180014b53:	7f 07                	jg     0x180014b5c
   180014b55:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014b5a:	eb 18                	jmp    0x180014b74
   180014b5c:	4d 8b ce             	mov    %r14,%r9
   180014b5f:	45 8b c7             	mov    %r15d,%r8d
   180014b62:	41 8b d4             	mov    %r12d,%edx
   180014b65:	e8 76 92 00 00       	call   0x18001dde0
   180014b6a:	85 c0                	test   %eax,%eax
   180014b6c:	bf fd ff ff ff       	mov    $0xfffffffd,%edi
   180014b71:	0f 48 f8             	cmovs  %eax,%edi
   180014b74:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014b7b:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014b82:	ff 52 10             	call   *0x10(%rdx)
   180014b85:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014b8a:	8b c7                	mov    %edi,%eax
   180014b8c:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014b91:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014b96:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014b9b:	48 83 c4 20          	add    $0x20,%rsp
   180014b9f:	41 5f                	pop    %r15
   180014ba1:	41 5e                	pop    %r14
   180014ba3:	41 5c                	pop    %r12
   180014ba5:	c3                   	ret
   180014ba6:	cc                   	int3
   180014ba7:	cc                   	int3
   180014ba8:	cc                   	int3
   180014ba9:	cc                   	int3
   180014baa:	cc                   	int3
   180014bab:	cc                   	int3
   180014bac:	cc                   	int3
   180014bad:	cc                   	int3
   180014bae:	cc                   	int3
   180014baf:	cc                   	int3
   180014bb0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
```

## `Wrraper_MSDisplayReadXdata` (Address: `0x180014ab0`)
```assembly
   180014ab0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014ab5:	41 54                	push   %r12
   180014ab7:	41 56                	push   %r14
   180014ab9:	41 57                	push   %r15
   180014abb:	48 83 ec 20          	sub    $0x20,%rsp
   180014abf:	83 3d 3a 3b 09 00 01 	cmpl   $0x1,0x93b3a(%rip)        # 0x1800a8600
   180014ac6:	4d 8b f1             	mov    %r9,%r14
   180014ac9:	45 8b f8             	mov    %r8d,%r15d
   180014acc:	44 8b e2             	mov    %edx,%r12d
   180014acf:	8b d9                	mov    %ecx,%ebx
   180014ad1:	74 15                	je     0x180014ae8
   180014ad3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014ad8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014add:	48 83 c4 20          	add    $0x20,%rsp
   180014ae1:	41 5f                	pop    %r15
   180014ae3:	41 5e                	pop    %r14
   180014ae5:	41 5c                	pop    %r12
   180014ae7:	c3                   	ret
   180014ae8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014aed:	48 8b 2d 24 3b 09 00 	mov    0x93b24(%rip),%rbp        # 0x1800a8618
   180014af4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014af9:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014afe:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   180014b03:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014b0a:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014b11:	ff 50 08             	call   *0x8(%rax)
   180014b14:	33 d2                	xor    %edx,%edx
   180014b16:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014b1d:	8b ca                	mov    %edx,%ecx
   180014b1f:	90                   	nop
   180014b20:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014b24:	74 04                	je     0x180014b2a
   180014b26:	39 18                	cmp    %ebx,(%rax)
   180014b28:	74 11                	je     0x180014b3b
   180014b2a:	ff c2                	inc    %edx
   180014b2c:	48 ff c1             	inc    %rcx
   180014b2f:	48 83 c0 18          	add    $0x18,%rax
   180014b33:	48 83 f9 10          	cmp    $0x10,%rcx
   180014b37:	7c e7                	jl     0x180014b20
   180014b39:	eb 39                	jmp    0x180014b74
   180014b3b:	48 63 c2             	movslq %edx,%rax
   180014b3e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014b42:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014b49:	00 
   180014b4a:	48 85 c9             	test   %rcx,%rcx
   180014b4d:	74 25                	je     0x180014b74
   180014b4f:	83 79 18 01          	cmpl   $0x1,0x18(%rcx)
   180014b53:	7f 07                	jg     0x180014b5c
   180014b55:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014b5a:	eb 18                	jmp    0x180014b74
   180014b5c:	4d 8b ce             	mov    %r14,%r9
   180014b5f:	45 8b c7             	mov    %r15d,%r8d
   180014b62:	41 8b d4             	mov    %r12d,%edx
   180014b65:	e8 76 92 00 00       	call   0x18001dde0
   180014b6a:	85 c0                	test   %eax,%eax
   180014b6c:	bf fd ff ff ff       	mov    $0xfffffffd,%edi
   180014b71:	0f 48 f8             	cmovs  %eax,%edi
   180014b74:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014b7b:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014b82:	ff 52 10             	call   *0x10(%rdx)
   180014b85:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014b8a:	8b c7                	mov    %edi,%eax
   180014b8c:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014b91:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014b96:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014b9b:	48 83 c4 20          	add    $0x20,%rsp
   180014b9f:	41 5f                	pop    %r15
   180014ba1:	41 5e                	pop    %r14
   180014ba3:	41 5c                	pop    %r12
   180014ba5:	c3                   	ret
   180014ba6:	cc                   	int3
   180014ba7:	cc                   	int3
   180014ba8:	cc                   	int3
   180014ba9:	cc                   	int3
   180014baa:	cc                   	int3
   180014bab:	cc                   	int3
   180014bac:	cc                   	int3
   180014bad:	cc                   	int3
   180014bae:	cc                   	int3
   180014baf:	cc                   	int3
   180014bb0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014bb5:	41 54                	push   %r12
   180014bb7:	41 56                	push   %r14
   180014bb9:	41 57                	push   %r15
   180014bbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014bbf:	83 3d 3a 3a 09 00 01 	cmpl   $0x1,0x93a3a(%rip)        # 0x1800a8600
   180014bc6:	4d 8b f1             	mov    %r9,%r14
   180014bc9:	45 8b f8             	mov    %r8d,%r15d
   180014bcc:	44 8b e2             	mov    %edx,%r12d
   180014bcf:	8b d9                	mov    %ecx,%ebx
   180014bd1:	74 15                	je     0x180014be8
   180014bd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014bd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014bdd:	48 83 c4 20          	add    $0x20,%rsp
   180014be1:	41 5f                	pop    %r15
   180014be3:	41 5e                	pop    %r14
   180014be5:	41 5c                	pop    %r12
   180014be7:	c3                   	ret
   180014be8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014bed:	48 8b 2d 24 3a 09 00 	mov    0x93a24(%rip),%rbp        # 0x1800a8618
```

## `Wrraper_MSDisplayReadFlash` (Address: `0x180014bb0`)
```assembly
   180014bb0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014bb5:	41 54                	push   %r12
   180014bb7:	41 56                	push   %r14
   180014bb9:	41 57                	push   %r15
   180014bbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014bbf:	83 3d 3a 3a 09 00 01 	cmpl   $0x1,0x93a3a(%rip)        # 0x1800a8600
   180014bc6:	4d 8b f1             	mov    %r9,%r14
   180014bc9:	45 8b f8             	mov    %r8d,%r15d
   180014bcc:	44 8b e2             	mov    %edx,%r12d
   180014bcf:	8b d9                	mov    %ecx,%ebx
   180014bd1:	74 15                	je     0x180014be8
   180014bd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014bd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014bdd:	48 83 c4 20          	add    $0x20,%rsp
   180014be1:	41 5f                	pop    %r15
   180014be3:	41 5e                	pop    %r14
   180014be5:	41 5c                	pop    %r12
   180014be7:	c3                   	ret
   180014be8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014bed:	48 8b 2d 24 3a 09 00 	mov    0x93a24(%rip),%rbp        # 0x1800a8618
   180014bf4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014bf9:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014bfe:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   180014c03:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014c0a:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014c11:	ff 50 08             	call   *0x8(%rax)
   180014c14:	33 d2                	xor    %edx,%edx
   180014c16:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014c1d:	8b ca                	mov    %edx,%ecx
   180014c1f:	90                   	nop
   180014c20:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014c24:	74 04                	je     0x180014c2a
   180014c26:	39 18                	cmp    %ebx,(%rax)
   180014c28:	74 11                	je     0x180014c3b
   180014c2a:	ff c2                	inc    %edx
   180014c2c:	48 ff c1             	inc    %rcx
   180014c2f:	48 83 c0 18          	add    $0x18,%rax
   180014c33:	48 83 f9 10          	cmp    $0x10,%rcx
   180014c37:	7c e7                	jl     0x180014c20
   180014c39:	eb 39                	jmp    0x180014c74
   180014c3b:	48 63 c2             	movslq %edx,%rax
   180014c3e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014c42:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014c49:	00 
   180014c4a:	48 85 c9             	test   %rcx,%rcx
   180014c4d:	74 25                	je     0x180014c74
   180014c4f:	83 79 18 01          	cmpl   $0x1,0x18(%rcx)
   180014c53:	7f 07                	jg     0x180014c5c
   180014c55:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014c5a:	eb 18                	jmp    0x180014c74
   180014c5c:	4d 8b ce             	mov    %r14,%r9
   180014c5f:	45 8b c7             	mov    %r15d,%r8d
   180014c62:	41 8b d4             	mov    %r12d,%edx
   180014c65:	e8 e6 a0 00 00       	call   0x18001ed50
   180014c6a:	85 c0                	test   %eax,%eax
   180014c6c:	bf fd ff ff ff       	mov    $0xfffffffd,%edi
   180014c71:	0f 48 f8             	cmovs  %eax,%edi
   180014c74:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014c7b:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014c82:	ff 52 10             	call   *0x10(%rdx)
   180014c85:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014c8a:	8b c7                	mov    %edi,%eax
   180014c8c:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014c91:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014c96:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014c9b:	48 83 c4 20          	add    $0x20,%rsp
   180014c9f:	41 5f                	pop    %r15
   180014ca1:	41 5e                	pop    %r14
   180014ca3:	41 5c                	pop    %r12
   180014ca5:	c3                   	ret
   180014ca6:	cc                   	int3
   180014ca7:	cc                   	int3
   180014ca8:	cc                   	int3
   180014ca9:	cc                   	int3
   180014caa:	cc                   	int3
   180014cab:	cc                   	int3
   180014cac:	cc                   	int3
   180014cad:	cc                   	int3
   180014cae:	cc                   	int3
   180014caf:	cc                   	int3
   180014cb0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014cb5:	41 54                	push   %r12
   180014cb7:	41 56                	push   %r14
   180014cb9:	41 57                	push   %r15
   180014cbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014cbf:	83 3d 3a 39 09 00 01 	cmpl   $0x1,0x9393a(%rip)        # 0x1800a8600
   180014cc6:	4d 8b f1             	mov    %r9,%r14
   180014cc9:	45 8b f8             	mov    %r8d,%r15d
   180014ccc:	44 8b e2             	mov    %edx,%r12d
   180014ccf:	8b d9                	mov    %ecx,%ebx
   180014cd1:	74 15                	je     0x180014ce8
   180014cd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014cd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014cdd:	48 83 c4 20          	add    $0x20,%rsp
   180014ce1:	41 5f                	pop    %r15
   180014ce3:	41 5e                	pop    %r14
   180014ce5:	41 5c                	pop    %r12
   180014ce7:	c3                   	ret
   180014ce8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014ced:	48 8b 2d 24 39 09 00 	mov    0x93924(%rip),%rbp        # 0x1800a8618
```

## `Wrraper_MSDisplayReadEEPROM` (Address: `0x180014cb0`)
```assembly
   180014cb0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014cb5:	41 54                	push   %r12
   180014cb7:	41 56                	push   %r14
   180014cb9:	41 57                	push   %r15
   180014cbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014cbf:	83 3d 3a 39 09 00 01 	cmpl   $0x1,0x9393a(%rip)        # 0x1800a8600
   180014cc6:	4d 8b f1             	mov    %r9,%r14
   180014cc9:	45 8b f8             	mov    %r8d,%r15d
   180014ccc:	44 8b e2             	mov    %edx,%r12d
   180014ccf:	8b d9                	mov    %ecx,%ebx
   180014cd1:	74 15                	je     0x180014ce8
   180014cd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014cd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014cdd:	48 83 c4 20          	add    $0x20,%rsp
   180014ce1:	41 5f                	pop    %r15
   180014ce3:	41 5e                	pop    %r14
   180014ce5:	41 5c                	pop    %r12
   180014ce7:	c3                   	ret
   180014ce8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014ced:	48 8b 2d 24 39 09 00 	mov    0x93924(%rip),%rbp        # 0x1800a8618
   180014cf4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014cf9:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014cfe:	bf fa ff ff ff       	mov    $0xfffffffa,%edi
   180014d03:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014d0a:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014d11:	ff 50 08             	call   *0x8(%rax)
   180014d14:	33 d2                	xor    %edx,%edx
   180014d16:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014d1d:	8b ca                	mov    %edx,%ecx
   180014d1f:	90                   	nop
   180014d20:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014d24:	74 04                	je     0x180014d2a
   180014d26:	39 18                	cmp    %ebx,(%rax)
   180014d28:	74 11                	je     0x180014d3b
   180014d2a:	ff c2                	inc    %edx
   180014d2c:	48 ff c1             	inc    %rcx
   180014d2f:	48 83 c0 18          	add    $0x18,%rax
   180014d33:	48 83 f9 10          	cmp    $0x10,%rcx
   180014d37:	7c e7                	jl     0x180014d20
   180014d39:	eb 39                	jmp    0x180014d74
   180014d3b:	48 63 c2             	movslq %edx,%rax
   180014d3e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014d42:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014d49:	00 
   180014d4a:	48 85 c9             	test   %rcx,%rcx
   180014d4d:	74 25                	je     0x180014d74
   180014d4f:	83 79 18 01          	cmpl   $0x1,0x18(%rcx)
   180014d53:	7f 07                	jg     0x180014d5c
   180014d55:	bf fc ff ff ff       	mov    $0xfffffffc,%edi
   180014d5a:	eb 18                	jmp    0x180014d74
   180014d5c:	4d 8b ce             	mov    %r14,%r9
   180014d5f:	45 8b c7             	mov    %r15d,%r8d
   180014d62:	41 8b d4             	mov    %r12d,%edx
   180014d65:	e8 d6 98 00 00       	call   0x18001e640
   180014d6a:	85 c0                	test   %eax,%eax
   180014d6c:	bf fd ff ff ff       	mov    $0xfffffffd,%edi
   180014d71:	0f 48 f8             	cmovs  %eax,%edi
   180014d74:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014d7b:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014d82:	ff 52 10             	call   *0x10(%rdx)
   180014d85:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014d8a:	8b c7                	mov    %edi,%eax
   180014d8c:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014d91:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014d96:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014d9b:	48 83 c4 20          	add    $0x20,%rsp
   180014d9f:	41 5f                	pop    %r15
   180014da1:	41 5e                	pop    %r14
   180014da3:	41 5c                	pop    %r12
   180014da5:	c3                   	ret
   180014da6:	cc                   	int3
   180014da7:	cc                   	int3
   180014da8:	cc                   	int3
   180014da9:	cc                   	int3
   180014daa:	cc                   	int3
   180014dab:	cc                   	int3
   180014dac:	cc                   	int3
   180014dad:	cc                   	int3
   180014dae:	cc                   	int3
   180014daf:	cc                   	int3
   180014db0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014db5:	41 54                	push   %r12
   180014db7:	41 56                	push   %r14
   180014db9:	41 57                	push   %r15
   180014dbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014dbf:	83 3d 3a 38 09 00 01 	cmpl   $0x1,0x9383a(%rip)        # 0x1800a8600
   180014dc6:	4d 8b f1             	mov    %r9,%r14
   180014dc9:	45 8b f8             	mov    %r8d,%r15d
   180014dcc:	44 8b e2             	mov    %edx,%r12d
   180014dcf:	8b d9                	mov    %ecx,%ebx
   180014dd1:	74 15                	je     0x180014de8
   180014dd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014dd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014ddd:	48 83 c4 20          	add    $0x20,%rsp
   180014de1:	41 5f                	pop    %r15
   180014de3:	41 5e                	pop    %r14
   180014de5:	41 5c                	pop    %r12
   180014de7:	c3                   	ret
   180014de8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014ded:	48 8b 2d 24 38 09 00 	mov    0x93824(%rip),%rbp        # 0x1800a8618
```

## `Wrraper_MSDisplayWriteXdata` (Address: `0x180014db0`)
```assembly
   180014db0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014db5:	41 54                	push   %r12
   180014db7:	41 56                	push   %r14
   180014db9:	41 57                	push   %r15
   180014dbb:	48 83 ec 20          	sub    $0x20,%rsp
   180014dbf:	83 3d 3a 38 09 00 01 	cmpl   $0x1,0x9383a(%rip)        # 0x1800a8600
   180014dc6:	4d 8b f1             	mov    %r9,%r14
   180014dc9:	45 8b f8             	mov    %r8d,%r15d
   180014dcc:	44 8b e2             	mov    %edx,%r12d
   180014dcf:	8b d9                	mov    %ecx,%ebx
   180014dd1:	74 15                	je     0x180014de8
   180014dd3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014dd8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014ddd:	48 83 c4 20          	add    $0x20,%rsp
   180014de1:	41 5f                	pop    %r15
   180014de3:	41 5e                	pop    %r14
   180014de5:	41 5c                	pop    %r12
   180014de7:	c3                   	ret
   180014de8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014ded:	48 8b 2d 24 38 09 00 	mov    0x93824(%rip),%rbp        # 0x1800a8618
   180014df4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014df9:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   180014dfe:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014e03:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014e0a:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014e11:	ff 50 08             	call   *0x8(%rax)
   180014e14:	33 d2                	xor    %edx,%edx
   180014e16:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014e1d:	8b ca                	mov    %edx,%ecx
   180014e1f:	90                   	nop
   180014e20:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014e24:	74 04                	je     0x180014e2a
   180014e26:	39 18                	cmp    %ebx,(%rax)
   180014e28:	74 11                	je     0x180014e3b
   180014e2a:	ff c2                	inc    %edx
   180014e2c:	48 ff c1             	inc    %rcx
   180014e2f:	48 83 c0 18          	add    $0x18,%rax
   180014e33:	48 83 f9 10          	cmp    $0x10,%rcx
   180014e37:	7c e7                	jl     0x180014e20
   180014e39:	eb 2c                	jmp    0x180014e67
   180014e3b:	48 63 c2             	movslq %edx,%rax
   180014e3e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014e42:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014e49:	00 
   180014e4a:	48 85 c9             	test   %rcx,%rcx
   180014e4d:	74 18                	je     0x180014e67
   180014e4f:	4d 8b ce             	mov    %r14,%r9
   180014e52:	45 8b c7             	mov    %r15d,%r8d
   180014e55:	41 8b d4             	mov    %r12d,%edx
   180014e58:	e8 33 a3 00 00       	call   0x18001f190
   180014e5d:	85 c0                	test   %eax,%eax
   180014e5f:	be fd ff ff ff       	mov    $0xfffffffd,%esi
   180014e64:	0f 48 f0             	cmovs  %eax,%esi
   180014e67:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014e6e:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014e75:	ff 52 10             	call   *0x10(%rdx)
   180014e78:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014e7d:	8b c6                	mov    %esi,%eax
   180014e7f:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014e84:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014e89:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014e8e:	48 83 c4 20          	add    $0x20,%rsp
   180014e92:	41 5f                	pop    %r15
   180014e94:	41 5e                	pop    %r14
   180014e96:	41 5c                	pop    %r12
   180014e98:	c3                   	ret
   180014e99:	cc                   	int3
   180014e9a:	cc                   	int3
   180014e9b:	cc                   	int3
   180014e9c:	cc                   	int3
   180014e9d:	cc                   	int3
   180014e9e:	cc                   	int3
   180014e9f:	cc                   	int3
   180014ea0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014ea5:	41 54                	push   %r12
   180014ea7:	41 56                	push   %r14
   180014ea9:	41 57                	push   %r15
   180014eab:	48 83 ec 20          	sub    $0x20,%rsp
   180014eaf:	83 3d 4a 37 09 00 01 	cmpl   $0x1,0x9374a(%rip)        # 0x1800a8600
   180014eb6:	4d 8b f1             	mov    %r9,%r14
   180014eb9:	45 8b f8             	mov    %r8d,%r15d
   180014ebc:	44 8b e2             	mov    %edx,%r12d
   180014ebf:	8b d9                	mov    %ecx,%ebx
   180014ec1:	74 15                	je     0x180014ed8
   180014ec3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014ec8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014ecd:	48 83 c4 20          	add    $0x20,%rsp
   180014ed1:	41 5f                	pop    %r15
   180014ed3:	41 5e                	pop    %r14
   180014ed5:	41 5c                	pop    %r12
   180014ed7:	c3                   	ret
   180014ed8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014edd:	48 8b 2d 34 37 09 00 	mov    0x93734(%rip),%rbp        # 0x1800a8618
   180014ee4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014ee9:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   180014eee:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014ef3:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014efa:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014f01:	ff 50 08             	call   *0x8(%rax)
   180014f04:	33 d2                	xor    %edx,%edx
```

## `Wrraper_MSDisplayWriteFlash` (Address: `0x180014ea0`)
```assembly
   180014ea0:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014ea5:	41 54                	push   %r12
   180014ea7:	41 56                	push   %r14
   180014ea9:	41 57                	push   %r15
   180014eab:	48 83 ec 20          	sub    $0x20,%rsp
   180014eaf:	83 3d 4a 37 09 00 01 	cmpl   $0x1,0x9374a(%rip)        # 0x1800a8600
   180014eb6:	4d 8b f1             	mov    %r9,%r14
   180014eb9:	45 8b f8             	mov    %r8d,%r15d
   180014ebc:	44 8b e2             	mov    %edx,%r12d
   180014ebf:	8b d9                	mov    %ecx,%ebx
   180014ec1:	74 15                	je     0x180014ed8
   180014ec3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014ec8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014ecd:	48 83 c4 20          	add    $0x20,%rsp
   180014ed1:	41 5f                	pop    %r15
   180014ed3:	41 5e                	pop    %r14
   180014ed5:	41 5c                	pop    %r12
   180014ed7:	c3                   	ret
   180014ed8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014edd:	48 8b 2d 34 37 09 00 	mov    0x93734(%rip),%rbp        # 0x1800a8618
   180014ee4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014ee9:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   180014eee:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014ef3:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014efa:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014f01:	ff 50 08             	call   *0x8(%rax)
   180014f04:	33 d2                	xor    %edx,%edx
   180014f06:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014f0d:	8b ca                	mov    %edx,%ecx
   180014f0f:	90                   	nop
   180014f10:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180014f14:	74 04                	je     0x180014f1a
   180014f16:	39 18                	cmp    %ebx,(%rax)
   180014f18:	74 11                	je     0x180014f2b
   180014f1a:	ff c2                	inc    %edx
   180014f1c:	48 ff c1             	inc    %rcx
   180014f1f:	48 83 c0 18          	add    $0x18,%rax
   180014f23:	48 83 f9 10          	cmp    $0x10,%rcx
   180014f27:	7c e7                	jl     0x180014f10
   180014f29:	eb 2c                	jmp    0x180014f57
   180014f2b:	48 63 c2             	movslq %edx,%rax
   180014f2e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180014f32:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180014f39:	00 
   180014f3a:	48 85 c9             	test   %rcx,%rcx
   180014f3d:	74 18                	je     0x180014f57
   180014f3f:	4d 8b ce             	mov    %r14,%r9
   180014f42:	45 8b c7             	mov    %r15d,%r8d
   180014f45:	41 8b d4             	mov    %r12d,%edx
   180014f48:	e8 53 a4 00 00       	call   0x18001f3a0
   180014f4d:	85 c0                	test   %eax,%eax
   180014f4f:	be fd ff ff ff       	mov    $0xfffffffd,%esi
   180014f54:	0f 48 f0             	cmovs  %eax,%esi
   180014f57:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180014f5e:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014f65:	ff 52 10             	call   *0x10(%rdx)
   180014f68:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   180014f6d:	8b c6                	mov    %esi,%eax
   180014f6f:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180014f74:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180014f79:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014f7e:	48 83 c4 20          	add    $0x20,%rsp
   180014f82:	41 5f                	pop    %r15
   180014f84:	41 5e                	pop    %r14
   180014f86:	41 5c                	pop    %r12
   180014f88:	c3                   	ret
   180014f89:	cc                   	int3
   180014f8a:	cc                   	int3
   180014f8b:	cc                   	int3
   180014f8c:	cc                   	int3
   180014f8d:	cc                   	int3
   180014f8e:	cc                   	int3
   180014f8f:	cc                   	int3
   180014f90:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014f95:	41 54                	push   %r12
   180014f97:	41 56                	push   %r14
   180014f99:	41 57                	push   %r15
   180014f9b:	48 83 ec 20          	sub    $0x20,%rsp
   180014f9f:	83 3d 5a 36 09 00 01 	cmpl   $0x1,0x9365a(%rip)        # 0x1800a8600
   180014fa6:	4d 8b f1             	mov    %r9,%r14
   180014fa9:	45 8b f8             	mov    %r8d,%r15d
   180014fac:	44 8b e2             	mov    %edx,%r12d
   180014faf:	8b d9                	mov    %ecx,%ebx
   180014fb1:	74 15                	je     0x180014fc8
   180014fb3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014fb8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014fbd:	48 83 c4 20          	add    $0x20,%rsp
   180014fc1:	41 5f                	pop    %r15
   180014fc3:	41 5e                	pop    %r14
   180014fc5:	41 5c                	pop    %r12
   180014fc7:	c3                   	ret
   180014fc8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014fcd:	48 8b 2d 44 36 09 00 	mov    0x93644(%rip),%rbp        # 0x1800a8618
   180014fd4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014fd9:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   180014fde:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014fe3:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014fea:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014ff1:	ff 50 08             	call   *0x8(%rax)
   180014ff4:	33 d2                	xor    %edx,%edx
```

## `Wrraper_MSDisplayWriteEEPROM` (Address: `0x180014f90`)
```assembly
   180014f90:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
   180014f95:	41 54                	push   %r12
   180014f97:	41 56                	push   %r14
   180014f99:	41 57                	push   %r15
   180014f9b:	48 83 ec 20          	sub    $0x20,%rsp
   180014f9f:	83 3d 5a 36 09 00 01 	cmpl   $0x1,0x9365a(%rip)        # 0x1800a8600
   180014fa6:	4d 8b f1             	mov    %r9,%r14
   180014fa9:	45 8b f8             	mov    %r8d,%r15d
   180014fac:	44 8b e2             	mov    %edx,%r12d
   180014faf:	8b d9                	mov    %ecx,%ebx
   180014fb1:	74 15                	je     0x180014fc8
   180014fb3:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180014fb8:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   180014fbd:	48 83 c4 20          	add    $0x20,%rsp
   180014fc1:	41 5f                	pop    %r15
   180014fc3:	41 5e                	pop    %r14
   180014fc5:	41 5c                	pop    %r12
   180014fc7:	c3                   	ret
   180014fc8:	48 89 6c 24 40       	mov    %rbp,0x40(%rsp)
   180014fcd:	48 8b 2d 44 36 09 00 	mov    0x93644(%rip),%rbp        # 0x1800a8618
   180014fd4:	48 89 74 24 48       	mov    %rsi,0x48(%rsp)
   180014fd9:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   180014fde:	48 89 7c 24 50       	mov    %rdi,0x50(%rsp)
   180014fe3:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   180014fea:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180014ff1:	ff 50 08             	call   *0x8(%rax)
   180014ff4:	33 d2                	xor    %edx,%edx
   180014ff6:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   180014ffd:	8b ca                	mov    %edx,%ecx
   180014fff:	90                   	nop
   180015000:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   180015004:	74 04                	je     0x18001500a
   180015006:	39 18                	cmp    %ebx,(%rax)
   180015008:	74 11                	je     0x18001501b
   18001500a:	ff c2                	inc    %edx
   18001500c:	48 ff c1             	inc    %rcx
   18001500f:	48 83 c0 18          	add    $0x18,%rax
   180015013:	48 83 f9 10          	cmp    $0x10,%rcx
   180015017:	7c e7                	jl     0x180015000
   180015019:	eb 2c                	jmp    0x180015047
   18001501b:	48 63 c2             	movslq %edx,%rax
   18001501e:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180015022:	48 8b 8c cd 80 02 00 	mov    0x280(%rbp,%rcx,8),%rcx
   180015029:	00 
   18001502a:	48 85 c9             	test   %rcx,%rcx
   18001502d:	74 18                	je     0x180015047
   18001502f:	4d 8b ce             	mov    %r14,%r9
   180015032:	45 8b c7             	mov    %r15d,%r8d
   180015035:	41 8b d4             	mov    %r12d,%edx
   180015038:	e8 a3 98 00 00       	call   0x18001e8e0
   18001503d:	85 c0                	test   %eax,%eax
   18001503f:	be fd ff ff ff       	mov    $0xfffffffd,%esi
   180015044:	0f 48 f0             	cmovs  %eax,%esi
   180015047:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   18001504e:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180015055:	ff 52 10             	call   *0x10(%rdx)
   180015058:	48 8b 7c 24 50       	mov    0x50(%rsp),%rdi
   18001505d:	8b c6                	mov    %esi,%eax
   18001505f:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
   180015064:	48 8b 6c 24 40       	mov    0x40(%rsp),%rbp
   180015069:	48 8b 5c 24 58       	mov    0x58(%rsp),%rbx
   18001506e:	48 83 c4 20          	add    $0x20,%rsp
   180015072:	41 5f                	pop    %r15
   180015074:	41 5e                	pop    %r14
   180015076:	41 5c                	pop    %r12
   180015078:	c3                   	ret
   180015079:	cc                   	int3
   18001507a:	cc                   	int3
   18001507b:	cc                   	int3
   18001507c:	cc                   	int3
   18001507d:	cc                   	int3
   18001507e:	cc                   	int3
   18001507f:	cc                   	int3
   180015080:	83 3d 79 35 09 00 01 	cmpl   $0x1,0x93579(%rip)        # 0x1800a8600
   180015087:	74 06                	je     0x18001508f
   180015089:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001508e:	c3                   	ret
   18001508f:	44 8b c2             	mov    %edx,%r8d
   180015092:	8b d1                	mov    %ecx,%edx
   180015094:	48 8b 0d 7d 35 09 00 	mov    0x9357d(%rip),%rcx        # 0x1800a8618
   18001509b:	e9 c0 3a 00 00       	jmp    0x180018b60
   1800150a0:	40 53                	rex push %rbx
   1800150a2:	48 83 ec 20          	sub    $0x20,%rsp
   1800150a6:	83 3d 53 35 09 00 01 	cmpl   $0x1,0x93553(%rip)        # 0x1800a8600
   1800150ad:	8b d9                	mov    %ecx,%ebx
   1800150af:	74 0b                	je     0x1800150bc
   1800150b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800150b6:	48 83 c4 20          	add    $0x20,%rsp
   1800150ba:	5b                   	pop    %rbx
   1800150bb:	c3                   	ret
   1800150bc:	48 89 6c 24 30       	mov    %rbp,0x30(%rsp)
   1800150c1:	48 8b 2d 50 35 09 00 	mov    0x93550(%rip),%rbp        # 0x1800a8618
   1800150c8:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800150cd:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   1800150d2:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
   1800150d7:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   1800150de:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   1800150e5:	ff 50 08             	call   *0x8(%rax)
   1800150e8:	33 d2                	xor    %edx,%edx
   1800150ea:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
```

## `Wrraper_MSDisplayFlashErase` (Address: `0x180015080`)
```assembly
   180015080:	83 3d 79 35 09 00 01 	cmpl   $0x1,0x93579(%rip)        # 0x1800a8600
   180015087:	74 06                	je     0x18001508f
   180015089:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001508e:	c3                   	ret
   18001508f:	44 8b c2             	mov    %edx,%r8d
   180015092:	8b d1                	mov    %ecx,%edx
   180015094:	48 8b 0d 7d 35 09 00 	mov    0x9357d(%rip),%rcx        # 0x1800a8618
   18001509b:	e9 c0 3a 00 00       	jmp    0x180018b60
   1800150a0:	40 53                	rex push %rbx
   1800150a2:	48 83 ec 20          	sub    $0x20,%rsp
   1800150a6:	83 3d 53 35 09 00 01 	cmpl   $0x1,0x93553(%rip)        # 0x1800a8600
   1800150ad:	8b d9                	mov    %ecx,%ebx
   1800150af:	74 0b                	je     0x1800150bc
   1800150b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800150b6:	48 83 c4 20          	add    $0x20,%rsp
   1800150ba:	5b                   	pop    %rbx
   1800150bb:	c3                   	ret
   1800150bc:	48 89 6c 24 30       	mov    %rbp,0x30(%rsp)
   1800150c1:	48 8b 2d 50 35 09 00 	mov    0x93550(%rip),%rbp        # 0x1800a8618
   1800150c8:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800150cd:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   1800150d2:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
   1800150d7:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   1800150de:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   1800150e5:	ff 50 08             	call   *0x8(%rax)
   1800150e8:	33 d2                	xor    %edx,%edx
   1800150ea:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   1800150f1:	8b ca                	mov    %edx,%ecx
   1800150f3:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   1800150f7:	74 04                	je     0x1800150fd
   1800150f9:	39 18                	cmp    %ebx,(%rax)
   1800150fb:	74 11                	je     0x18001510e
   1800150fd:	ff c2                	inc    %edx
   1800150ff:	48 ff c1             	inc    %rcx
   180015102:	48 83 c0 18          	add    $0x18,%rax
   180015106:	48 83 f9 10          	cmp    $0x10,%rcx
   18001510a:	7c e7                	jl     0x1800150f3
   18001510c:	eb 1b                	jmp    0x180015129
   18001510e:	48 63 c2             	movslq %edx,%rax
   180015111:	48 8d 14 40          	lea    (%rax,%rax,2),%rdx
   180015115:	48 8b 8c d5 80 02 00 	mov    0x280(%rbp,%rdx,8),%rcx
   18001511c:	00 
   18001511d:	48 85 c9             	test   %rcx,%rcx
   180015120:	74 07                	je     0x180015129
   180015122:	e8 49 8f 00 00       	call   0x18001e070
   180015127:	8b f0                	mov    %eax,%esi
   180015129:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180015130:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180015137:	ff 52 10             	call   *0x10(%rdx)
   18001513a:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
   18001513f:	8b c6                	mov    %esi,%eax
   180015141:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   180015146:	48 8b 6c 24 30       	mov    0x30(%rsp),%rbp
   18001514b:	48 83 c4 20          	add    $0x20,%rsp
   18001514f:	5b                   	pop    %rbx
   180015150:	c3                   	ret
   180015151:	cc                   	int3
   180015152:	cc                   	int3
   180015153:	cc                   	int3
   180015154:	cc                   	int3
   180015155:	cc                   	int3
   180015156:	cc                   	int3
   180015157:	cc                   	int3
   180015158:	cc                   	int3
   180015159:	cc                   	int3
   18001515a:	cc                   	int3
   18001515b:	cc                   	int3
   18001515c:	cc                   	int3
   18001515d:	cc                   	int3
   18001515e:	cc                   	int3
   18001515f:	cc                   	int3
   180015160:	48 89 6c 24 20       	mov    %rbp,0x20(%rsp)
   180015165:	57                   	push   %rdi
   180015166:	48 83 ec 20          	sub    $0x20,%rsp
   18001516a:	83 3d 8f 34 09 00 01 	cmpl   $0x1,0x9348f(%rip)        # 0x1800a8600
   180015171:	48 8b ea             	mov    %rdx,%rbp
   180015174:	8b f9                	mov    %ecx,%edi
   180015176:	74 10                	je     0x180015188
   180015178:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001517d:	48 8b 6c 24 48       	mov    0x48(%rsp),%rbp
   180015182:	48 83 c4 20          	add    $0x20,%rsp
   180015186:	5f                   	pop    %rdi
   180015187:	c3                   	ret
   180015188:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   18001518d:	8b c7                	mov    %edi,%eax
   18001518f:	25 00 ff ff ff       	and    $0xffffff00,%eax
   180015194:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   180015199:	4c 89 74 24 40       	mov    %r14,0x40(%rsp)
   18001519e:	bb fa ff ff ff       	mov    $0xfffffffa,%ebx
   1800151a3:	4c 8b 35 6e 34 09 00 	mov    0x9346e(%rip),%r14        # 0x1800a8618
   1800151aa:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800151af:	75 7a                	jne    0x18001522b
   1800151b1:	49 8b 86 40 02 00 00 	mov    0x240(%r14),%rax
   1800151b8:	49 8d 8e 40 02 00 00 	lea    0x240(%r14),%rcx
   1800151bf:	ff 50 08             	call   *0x8(%rax)
   1800151c2:	40 0f b6 c7          	movzbl %dil,%eax
   1800151c6:	83 f8 06             	cmp    $0x6,%eax
   1800151c9:	73 4a                	jae    0x180015215
   1800151cb:	8b c8                	mov    %eax,%ecx
   1800151cd:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
```

## `Wrraper_MSDisplayInitFlashGpio` (Address: `0x1800150a0`)
```assembly
   1800150a0:	40 53                	rex push %rbx
   1800150a2:	48 83 ec 20          	sub    $0x20,%rsp
   1800150a6:	83 3d 53 35 09 00 01 	cmpl   $0x1,0x93553(%rip)        # 0x1800a8600
   1800150ad:	8b d9                	mov    %ecx,%ebx
   1800150af:	74 0b                	je     0x1800150bc
   1800150b1:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800150b6:	48 83 c4 20          	add    $0x20,%rsp
   1800150ba:	5b                   	pop    %rbx
   1800150bb:	c3                   	ret
   1800150bc:	48 89 6c 24 30       	mov    %rbp,0x30(%rsp)
   1800150c1:	48 8b 2d 50 35 09 00 	mov    0x93550(%rip),%rbp        # 0x1800a8618
   1800150c8:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800150cd:	be fa ff ff ff       	mov    $0xfffffffa,%esi
   1800150d2:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
   1800150d7:	48 8b 85 10 02 00 00 	mov    0x210(%rbp),%rax
   1800150de:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   1800150e5:	ff 50 08             	call   *0x8(%rax)
   1800150e8:	33 d2                	xor    %edx,%edx
   1800150ea:	48 8d 85 88 02 00 00 	lea    0x288(%rbp),%rax
   1800150f1:	8b ca                	mov    %edx,%ecx
   1800150f3:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   1800150f7:	74 04                	je     0x1800150fd
   1800150f9:	39 18                	cmp    %ebx,(%rax)
   1800150fb:	74 11                	je     0x18001510e
   1800150fd:	ff c2                	inc    %edx
   1800150ff:	48 ff c1             	inc    %rcx
   180015102:	48 83 c0 18          	add    $0x18,%rax
   180015106:	48 83 f9 10          	cmp    $0x10,%rcx
   18001510a:	7c e7                	jl     0x1800150f3
   18001510c:	eb 1b                	jmp    0x180015129
   18001510e:	48 63 c2             	movslq %edx,%rax
   180015111:	48 8d 14 40          	lea    (%rax,%rax,2),%rdx
   180015115:	48 8b 8c d5 80 02 00 	mov    0x280(%rbp,%rdx,8),%rcx
   18001511c:	00 
   18001511d:	48 85 c9             	test   %rcx,%rcx
   180015120:	74 07                	je     0x180015129
   180015122:	e8 49 8f 00 00       	call   0x18001e070
   180015127:	8b f0                	mov    %eax,%esi
   180015129:	48 8b 95 10 02 00 00 	mov    0x210(%rbp),%rdx
   180015130:	48 8d 8d 10 02 00 00 	lea    0x210(%rbp),%rcx
   180015137:	ff 52 10             	call   *0x10(%rdx)
   18001513a:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
   18001513f:	8b c6                	mov    %esi,%eax
   180015141:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   180015146:	48 8b 6c 24 30       	mov    0x30(%rsp),%rbp
   18001514b:	48 83 c4 20          	add    $0x20,%rsp
   18001514f:	5b                   	pop    %rbx
   180015150:	c3                   	ret
   180015151:	cc                   	int3
   180015152:	cc                   	int3
   180015153:	cc                   	int3
   180015154:	cc                   	int3
   180015155:	cc                   	int3
   180015156:	cc                   	int3
   180015157:	cc                   	int3
   180015158:	cc                   	int3
   180015159:	cc                   	int3
   18001515a:	cc                   	int3
   18001515b:	cc                   	int3
   18001515c:	cc                   	int3
   18001515d:	cc                   	int3
   18001515e:	cc                   	int3
   18001515f:	cc                   	int3
   180015160:	48 89 6c 24 20       	mov    %rbp,0x20(%rsp)
   180015165:	57                   	push   %rdi
   180015166:	48 83 ec 20          	sub    $0x20,%rsp
   18001516a:	83 3d 8f 34 09 00 01 	cmpl   $0x1,0x9348f(%rip)        # 0x1800a8600
   180015171:	48 8b ea             	mov    %rdx,%rbp
   180015174:	8b f9                	mov    %ecx,%edi
   180015176:	74 10                	je     0x180015188
   180015178:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001517d:	48 8b 6c 24 48       	mov    0x48(%rsp),%rbp
   180015182:	48 83 c4 20          	add    $0x20,%rsp
   180015186:	5f                   	pop    %rdi
   180015187:	c3                   	ret
   180015188:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   18001518d:	8b c7                	mov    %edi,%eax
   18001518f:	25 00 ff ff ff       	and    $0xffffff00,%eax
   180015194:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   180015199:	4c 89 74 24 40       	mov    %r14,0x40(%rsp)
   18001519e:	bb fa ff ff ff       	mov    $0xfffffffa,%ebx
   1800151a3:	4c 8b 35 6e 34 09 00 	mov    0x9346e(%rip),%r14        # 0x1800a8618
   1800151aa:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800151af:	75 7a                	jne    0x18001522b
   1800151b1:	49 8b 86 40 02 00 00 	mov    0x240(%r14),%rax
   1800151b8:	49 8d 8e 40 02 00 00 	lea    0x240(%r14),%rcx
   1800151bf:	ff 50 08             	call   *0x8(%rax)
   1800151c2:	40 0f b6 c7          	movzbl %dil,%eax
   1800151c6:	83 f8 06             	cmp    $0x6,%eax
   1800151c9:	73 4a                	jae    0x180015215
   1800151cb:	8b c8                	mov    %eax,%ecx
   1800151cd:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
   1800151d1:	41 80 bc c6 00 04 00 	cmpb   $0x0,0x400(%r14,%rax,8)
   1800151d8:	00 00 
   1800151da:	74 39                	je     0x180015215
   1800151dc:	48 8d 04 49          	lea    (%rcx,%rcx,2),%rax
   1800151e0:	49 8b 8c c6 08 04 00 	mov    0x408(%r14,%rax,8),%rcx
   1800151e7:	00 
   1800151e8:	83 39 00             	cmpl   $0x0,(%rcx)
   1800151eb:	7f 07                	jg     0x1800151f4
```

## `Wrraper_MSDisplayReadSN` (Address: `0x180015160`)
```assembly
   180015160:	48 89 6c 24 20       	mov    %rbp,0x20(%rsp)
   180015165:	57                   	push   %rdi
   180015166:	48 83 ec 20          	sub    $0x20,%rsp
   18001516a:	83 3d 8f 34 09 00 01 	cmpl   $0x1,0x9348f(%rip)        # 0x1800a8600
   180015171:	48 8b ea             	mov    %rdx,%rbp
   180015174:	8b f9                	mov    %ecx,%edi
   180015176:	74 10                	je     0x180015188
   180015178:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001517d:	48 8b 6c 24 48       	mov    0x48(%rsp),%rbp
   180015182:	48 83 c4 20          	add    $0x20,%rsp
   180015186:	5f                   	pop    %rdi
   180015187:	c3                   	ret
   180015188:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   18001518d:	8b c7                	mov    %edi,%eax
   18001518f:	25 00 ff ff ff       	and    $0xffffff00,%eax
   180015194:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   180015199:	4c 89 74 24 40       	mov    %r14,0x40(%rsp)
   18001519e:	bb fa ff ff ff       	mov    $0xfffffffa,%ebx
   1800151a3:	4c 8b 35 6e 34 09 00 	mov    0x9346e(%rip),%r14        # 0x1800a8618
   1800151aa:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800151af:	75 7a                	jne    0x18001522b
   1800151b1:	49 8b 86 40 02 00 00 	mov    0x240(%r14),%rax
   1800151b8:	49 8d 8e 40 02 00 00 	lea    0x240(%r14),%rcx
   1800151bf:	ff 50 08             	call   *0x8(%rax)
   1800151c2:	40 0f b6 c7          	movzbl %dil,%eax
   1800151c6:	83 f8 06             	cmp    $0x6,%eax
   1800151c9:	73 4a                	jae    0x180015215
   1800151cb:	8b c8                	mov    %eax,%ecx
   1800151cd:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
   1800151d1:	41 80 bc c6 00 04 00 	cmpb   $0x0,0x400(%r14,%rax,8)
   1800151d8:	00 00 
   1800151da:	74 39                	je     0x180015215
   1800151dc:	48 8d 04 49          	lea    (%rcx,%rcx,2),%rax
   1800151e0:	49 8b 8c c6 08 04 00 	mov    0x408(%r14,%rax,8),%rcx
   1800151e7:	00 
   1800151e8:	83 39 00             	cmpl   $0x0,(%rcx)
   1800151eb:	7f 07                	jg     0x1800151f4
   1800151ed:	bb fc ff ff ff       	mov    $0xfffffffc,%ebx
   1800151f2:	eb 21                	jmp    0x180015215
   1800151f4:	8b 41 14             	mov    0x14(%rcx),%eax
   1800151f7:	ff c8                	dec    %eax
   1800151f9:	83 f8 1d             	cmp    $0x1d,%eax
   1800151fc:	77 15                	ja     0x180015213
   1800151fe:	0f 10 41 18          	movups 0x18(%rcx),%xmm0
   180015202:	0f 11 45 00          	movups %xmm0,0x0(%rbp)
   180015206:	0f 10 49 28          	movups 0x28(%rcx),%xmm1
   18001520a:	0f 11 4d 10          	movups %xmm1,0x10(%rbp)
   18001520e:	8b 59 14             	mov    0x14(%rcx),%ebx
   180015211:	eb 02                	jmp    0x180015215
   180015213:	33 db                	xor    %ebx,%ebx
   180015215:	49 8b 86 40 02 00 00 	mov    0x240(%r14),%rax
   18001521c:	49 8d 8e 40 02 00 00 	lea    0x240(%r14),%rcx
   180015223:	ff 50 10             	call   *0x10(%rax)
   180015226:	e9 8a 00 00 00       	jmp    0x1800152b5
   18001522b:	49 8b 86 10 02 00 00 	mov    0x210(%r14),%rax
   180015232:	49 8d 8e 10 02 00 00 	lea    0x210(%r14),%rcx
   180015239:	ff 50 08             	call   *0x8(%rax)
   18001523c:	33 d2                	xor    %edx,%edx
   18001523e:	49 8d 86 88 02 00 00 	lea    0x288(%r14),%rax
   180015245:	33 c9                	xor    %ecx,%ecx
   180015247:	80 78 f0 00          	cmpb   $0x0,-0x10(%rax)
   18001524b:	74 04                	je     0x180015251
   18001524d:	39 38                	cmp    %edi,(%rax)
   18001524f:	74 11                	je     0x180015262
   180015251:	ff c2                	inc    %edx
   180015253:	48 ff c1             	inc    %rcx
   180015256:	48 83 c0 18          	add    $0x18,%rax
   18001525a:	48 83 f9 10          	cmp    $0x10,%rcx
   18001525e:	7c e7                	jl     0x180015247
   180015260:	eb 42                	jmp    0x1800152a4
   180015262:	48 63 c2             	movslq %edx,%rax
   180015265:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   180015269:	49 8b 94 ce 80 02 00 	mov    0x280(%r14,%rcx,8),%rdx
   180015270:	00 
   180015271:	48 85 d2             	test   %rdx,%rdx
   180015274:	74 2e                	je     0x1800152a4
   180015276:	83 7a 18 00          	cmpl   $0x0,0x18(%rdx)
   18001527a:	7f 07                	jg     0x180015283
   18001527c:	bb fc ff ff ff       	mov    $0xfffffffc,%ebx
   180015281:	eb 21                	jmp    0x1800152a4
   180015283:	8b 42 2c             	mov    0x2c(%rdx),%eax
   180015286:	ff c8                	dec    %eax
   180015288:	83 f8 1d             	cmp    $0x1d,%eax
   18001528b:	77 15                	ja     0x1800152a2
   18001528d:	0f 10 42 30          	movups 0x30(%rdx),%xmm0
   180015291:	0f 11 45 00          	movups %xmm0,0x0(%rbp)
   180015295:	0f 10 4a 40          	movups 0x40(%rdx),%xmm1
   180015299:	0f 11 4d 10          	movups %xmm1,0x10(%rbp)
   18001529d:	8b 5a 2c             	mov    0x2c(%rdx),%ebx
   1800152a0:	eb 02                	jmp    0x1800152a4
   1800152a2:	33 db                	xor    %ebx,%ebx
   1800152a4:	49 8b 96 10 02 00 00 	mov    0x210(%r14),%rdx
   1800152ab:	49 8d 8e 10 02 00 00 	lea    0x210(%r14),%rcx
   1800152b2:	ff 52 10             	call   *0x10(%rdx)
   1800152b5:	4c 8b 74 24 40       	mov    0x40(%rsp),%r14
   1800152ba:	8b c3                	mov    %ebx,%eax
   1800152bc:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   1800152c1:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   1800152c6:	48 8b 6c 24 48       	mov    0x48(%rsp),%rbp
   1800152cb:	48 83 c4 20          	add    $0x20,%rsp
```

## `Wrraper_MSDisplayPause` (Address: `0x1800152e0`)
```assembly
   1800152e0:	48 83 ec 28          	sub    $0x28,%rsp
   1800152e4:	83 3d 15 33 09 00 01 	cmpl   $0x1,0x93315(%rip)        # 0x1800a8600
   1800152eb:	74 0a                	je     0x1800152f7
   1800152ed:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800152f2:	48 83 c4 28          	add    $0x28,%rsp
   1800152f6:	c3                   	ret
   1800152f7:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   1800152fc:	48 8b 1d 15 33 09 00 	mov    0x93315(%rip),%rbx        # 0x1800a8618
   180015303:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   180015308:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
   18001530d:	4c 8d b3 10 02 00 00 	lea    0x210(%rbx),%r14
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
   180015367:	48 83 ee 01          	sub    $0x1,%rsi
   18001536b:	75 c3                	jne    0x180015330
   18001536d:	49 8b 06             	mov    (%r14),%rax
   180015370:	49 8b ce             	mov    %r14,%rcx
   180015373:	ff 50 10             	call   *0x10(%rax)
   180015376:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
   18001537b:	33 c0                	xor    %eax,%eax
   18001537d:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
   180015382:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   180015387:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18001538c:	48 83 c4 28          	add    $0x28,%rsp
   180015390:	c3                   	ret
   180015391:	cc                   	int3
   180015392:	cc                   	int3
   180015393:	cc                   	int3
   180015394:	cc                   	int3
   180015395:	cc                   	int3
   180015396:	cc                   	int3
   180015397:	cc                   	int3
   180015398:	cc                   	int3
   180015399:	cc                   	int3
   18001539a:	cc                   	int3
   18001539b:	cc                   	int3
   18001539c:	cc                   	int3
   18001539d:	cc                   	int3
   18001539e:	cc                   	int3
   18001539f:	cc                   	int3
   1800153a0:	48 83 ec 28          	sub    $0x28,%rsp
   1800153a4:	83 3d 55 32 09 00 01 	cmpl   $0x1,0x93255(%rip)        # 0x1800a8600
   1800153ab:	74 0a                	je     0x1800153b7
   1800153ad:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800153b2:	48 83 c4 28          	add    $0x28,%rsp
   1800153b6:	c3                   	ret
   1800153b7:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   1800153bc:	48 8b 1d 55 32 09 00 	mov    0x93255(%rip),%rbx        # 0x1800a8618
   1800153c3:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800153c8:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
   1800153cd:	4c 8d b3 10 02 00 00 	lea    0x210(%rbx),%r14
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
   180015427:	48 83 ee 01          	sub    $0x1,%rsi
   18001542b:	75 c3                	jne    0x1800153f0
   18001542d:	49 8b 06             	mov    (%r14),%rax
   180015430:	49 8b ce             	mov    %r14,%rcx
   180015433:	ff 50 10             	call   *0x10(%rax)
   180015436:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
   18001543b:	33 c0                	xor    %eax,%eax
   18001543d:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
   180015442:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   180015447:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18001544c:	48 83 c4 28          	add    $0x28,%rsp
```

## `Wrraper_MSDisplayResume` (Address: `0x1800153a0`)
```assembly
   1800153a0:	48 83 ec 28          	sub    $0x28,%rsp
   1800153a4:	83 3d 55 32 09 00 01 	cmpl   $0x1,0x93255(%rip)        # 0x1800a8600
   1800153ab:	74 0a                	je     0x1800153b7
   1800153ad:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   1800153b2:	48 83 c4 28          	add    $0x28,%rsp
   1800153b6:	c3                   	ret
   1800153b7:	48 89 5c 24 30       	mov    %rbx,0x30(%rsp)
   1800153bc:	48 8b 1d 55 32 09 00 	mov    0x93255(%rip),%rbx        # 0x1800a8618
   1800153c3:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
   1800153c8:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
   1800153cd:	4c 8d b3 10 02 00 00 	lea    0x210(%rbx),%r14
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
   180015427:	48 83 ee 01          	sub    $0x1,%rsi
   18001542b:	75 c3                	jne    0x1800153f0
   18001542d:	49 8b 06             	mov    (%r14),%rax
   180015430:	49 8b ce             	mov    %r14,%rcx
   180015433:	ff 50 10             	call   *0x10(%rax)
   180015436:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
   18001543b:	33 c0                	xor    %eax,%eax
   18001543d:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
   180015442:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
   180015447:	48 8b 5c 24 30       	mov    0x30(%rsp),%rbx
   18001544c:	48 83 c4 28          	add    $0x28,%rsp
   180015450:	c3                   	ret
   180015451:	cc                   	int3
   180015452:	cc                   	int3
   180015453:	cc                   	int3
   180015454:	cc                   	int3
   180015455:	cc                   	int3
   180015456:	cc                   	int3
   180015457:	cc                   	int3
   180015458:	cc                   	int3
   180015459:	cc                   	int3
   18001545a:	cc                   	int3
   18001545b:	cc                   	int3
   18001545c:	cc                   	int3
   18001545d:	cc                   	int3
   18001545e:	cc                   	int3
   18001545f:	cc                   	int3
   180015460:	83 3d 99 31 09 00 01 	cmpl   $0x1,0x93199(%rip)        # 0x1800a8600
   180015467:	74 06                	je     0x18001546f
   180015469:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001546e:	c3                   	ret
   18001546f:	48 8b 05 a2 31 09 00 	mov    0x931a2(%rip),%rax        # 0x1800a8618
   180015476:	88 88 f8 03 00 00    	mov    %cl,0x3f8(%rax)
   18001547c:	33 c0                	xor    %eax,%eax
   18001547e:	c3                   	ret
   18001547f:	cc                   	int3
   180015480:	83 3d 79 31 09 00 01 	cmpl   $0x1,0x93179(%rip)        # 0x1800a8600
   180015487:	74 06                	je     0x18001548f
   180015489:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001548e:	c3                   	ret
   18001548f:	4c 8b 05 82 31 09 00 	mov    0x93182(%rip),%r8        # 0x1800a8618
   180015496:	c6 02 00             	movb   $0x0,(%rdx)
   180015499:	41 80 b8 f8 03 00 00 	cmpb   $0x0,0x3f8(%r8)
   1800154a0:	00 
   1800154a1:	75 06                	jne    0x1800154a9
   1800154a3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154a8:	c3                   	ret
   1800154a9:	8b c1                	mov    %ecx,%eax
   1800154ab:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800154b0:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800154b5:	75 1a                	jne    0x1800154d1
   1800154b7:	0f b6 c1             	movzbl %cl,%eax
   1800154ba:	83 f8 06             	cmp    $0x6,%eax
   1800154bd:	73 15                	jae    0x1800154d4
   1800154bf:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   1800154c3:	41 80 bc c8 00 04 00 	cmpb   $0x0,0x400(%r8,%rcx,8)
   1800154ca:	00 00 
   1800154cc:	74 06                	je     0x1800154d4
   1800154ce:	c6 02 01             	movb   $0x1,(%rdx)
   1800154d1:	33 c0                	xor    %eax,%eax
   1800154d3:	c3                   	ret
   1800154d4:	b8 fa ff ff ff       	mov    $0xfffffffa,%eax
   1800154d9:	c3                   	ret
   1800154da:	cc                   	int3
   1800154db:	cc                   	int3
   1800154dc:	cc                   	int3
   1800154dd:	cc                   	int3
   1800154de:	cc                   	int3
   1800154df:	cc                   	int3
```

## `Wrraper_MSDisplayEnableSDKScreenProcessor` (Address: `0x180015460`)
```assembly
   180015460:	83 3d 99 31 09 00 01 	cmpl   $0x1,0x93199(%rip)        # 0x1800a8600
   180015467:	74 06                	je     0x18001546f
   180015469:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001546e:	c3                   	ret
   18001546f:	48 8b 05 a2 31 09 00 	mov    0x931a2(%rip),%rax        # 0x1800a8618
   180015476:	88 88 f8 03 00 00    	mov    %cl,0x3f8(%rax)
   18001547c:	33 c0                	xor    %eax,%eax
   18001547e:	c3                   	ret
   18001547f:	cc                   	int3
   180015480:	83 3d 79 31 09 00 01 	cmpl   $0x1,0x93179(%rip)        # 0x1800a8600
   180015487:	74 06                	je     0x18001548f
   180015489:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001548e:	c3                   	ret
   18001548f:	4c 8b 05 82 31 09 00 	mov    0x93182(%rip),%r8        # 0x1800a8618
   180015496:	c6 02 00             	movb   $0x0,(%rdx)
   180015499:	41 80 b8 f8 03 00 00 	cmpb   $0x0,0x3f8(%r8)
   1800154a0:	00 
   1800154a1:	75 06                	jne    0x1800154a9
   1800154a3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154a8:	c3                   	ret
   1800154a9:	8b c1                	mov    %ecx,%eax
   1800154ab:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800154b0:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800154b5:	75 1a                	jne    0x1800154d1
   1800154b7:	0f b6 c1             	movzbl %cl,%eax
   1800154ba:	83 f8 06             	cmp    $0x6,%eax
   1800154bd:	73 15                	jae    0x1800154d4
   1800154bf:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   1800154c3:	41 80 bc c8 00 04 00 	cmpb   $0x0,0x400(%r8,%rcx,8)
   1800154ca:	00 00 
   1800154cc:	74 06                	je     0x1800154d4
   1800154ce:	c6 02 01             	movb   $0x1,(%rdx)
   1800154d1:	33 c0                	xor    %eax,%eax
   1800154d3:	c3                   	ret
   1800154d4:	b8 fa ff ff ff       	mov    $0xfffffffa,%eax
   1800154d9:	c3                   	ret
   1800154da:	cc                   	int3
   1800154db:	cc                   	int3
   1800154dc:	cc                   	int3
   1800154dd:	cc                   	int3
   1800154de:	cc                   	int3
   1800154df:	cc                   	int3
   1800154e0:	48 8b 15 31 31 09 00 	mov    0x93131(%rip),%rdx        # 0x1800a8618
   1800154e7:	48 8b c1             	mov    %rcx,%rax
   1800154ea:	80 ba f9 03 00 00 00 	cmpb   $0x0,0x3f9(%rdx)
   1800154f1:	75 06                	jne    0x1800154f9
   1800154f3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154f8:	c3                   	ret
   1800154f9:	48 8b 92 90 04 00 00 	mov    0x490(%rdx),%rdx
   180015500:	0f b7 ca             	movzwl %dx,%ecx
   180015503:	89 08                	mov    %ecx,(%rax)
   180015505:	48 8b ca             	mov    %rdx,%rcx
   180015508:	48 c1 e9 10          	shr    $0x10,%rcx
   18001550c:	0f b7 c9             	movzwl %cx,%ecx
   18001550f:	89 48 04             	mov    %ecx,0x4(%rax)
   180015512:	48 8b ca             	mov    %rdx,%rcx
   180015515:	48 c1 e9 20          	shr    $0x20,%rcx
   180015519:	0f b7 c9             	movzwl %cx,%ecx
   18001551c:	89 48 08             	mov    %ecx,0x8(%rax)
   18001551f:	48 c1 ea 30          	shr    $0x30,%rdx
   180015523:	89 50 0c             	mov    %edx,0xc(%rax)
   180015526:	33 c0                	xor    %eax,%eax
   180015528:	c3                   	ret
   180015529:	cc                   	int3
   18001552a:	cc                   	int3
   18001552b:	cc                   	int3
   18001552c:	cc                   	int3
   18001552d:	cc                   	int3
   18001552e:	cc                   	int3
   18001552f:	cc                   	int3
   180015530:	40 55                	rex push %rbp
   180015532:	53                   	push   %rbx
   180015533:	56                   	push   %rsi
   180015534:	48 8d ac 24 80 fe ff 	lea    -0x180(%rsp),%rbp
   18001553b:	ff 
   18001553c:	48 81 ec 80 02 00 00 	sub    $0x280,%rsp
   180015543:	48 8b 05 16 0e 09 00 	mov    0x90e16(%rip),%rax        # 0x1800a6360
   18001554a:	48 33 c4             	xor    %rsp,%rax
   18001554d:	48 89 85 60 01 00 00 	mov    %rax,0x160(%rbp)
   180015554:	8b 05 a6 30 09 00    	mov    0x930a6(%rip),%eax        # 0x1800a8600
   18001555a:	48 8b f2             	mov    %rdx,%rsi
   18001555d:	8b d9                	mov    %ecx,%ebx
   18001555f:	83 f8 01             	cmp    $0x1,%eax
   180015562:	75 0a                	jne    0x18001556e
   180015564:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180015569:	e9 0d 06 00 00       	jmp    0x180015b7b
   18001556e:	48 89 bc 24 a0 02 00 	mov    %rdi,0x2a0(%rsp)
   180015575:	00 
   180015576:	4c 89 a4 24 a8 02 00 	mov    %r12,0x2a8(%rsp)
   18001557d:	00 
   18001557e:	4c 89 b4 24 78 02 00 	mov    %r14,0x278(%rsp)
   180015585:	00 
   180015586:	45 33 f6             	xor    %r14d,%r14d
   180015589:	4c 89 bc 24 70 02 00 	mov    %r15,0x270(%rsp)
   180015590:	00 
   180015591:	4c 8d 3d b0 5b 08 00 	lea    0x85bb0(%rip),%r15        # 0x18009b148
   180015598:	85 c0                	test   %eax,%eax
   18001559a:	0f 85 10 01 00 00    	jne    0x1800156b0
   1800155a0:	8d 48 70             	lea    0x70(%rax),%ecx
   1800155a3:	e8 0c fa 03 00       	call   0x180054fb4
```

## `Wrraper_MSDisplayCheckDeviceScreenCapability` (Address: `0x180015480`)
```assembly
   180015480:	83 3d 79 31 09 00 01 	cmpl   $0x1,0x93179(%rip)        # 0x1800a8600
   180015487:	74 06                	je     0x18001548f
   180015489:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   18001548e:	c3                   	ret
   18001548f:	4c 8b 05 82 31 09 00 	mov    0x93182(%rip),%r8        # 0x1800a8618
   180015496:	c6 02 00             	movb   $0x0,(%rdx)
   180015499:	41 80 b8 f8 03 00 00 	cmpb   $0x0,0x3f8(%r8)
   1800154a0:	00 
   1800154a1:	75 06                	jne    0x1800154a9
   1800154a3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154a8:	c3                   	ret
   1800154a9:	8b c1                	mov    %ecx,%eax
   1800154ab:	25 00 ff ff ff       	and    $0xffffff00,%eax
   1800154b0:	3d 00 55 73 6d       	cmp    $0x6d735500,%eax
   1800154b5:	75 1a                	jne    0x1800154d1
   1800154b7:	0f b6 c1             	movzbl %cl,%eax
   1800154ba:	83 f8 06             	cmp    $0x6,%eax
   1800154bd:	73 15                	jae    0x1800154d4
   1800154bf:	48 8d 0c 40          	lea    (%rax,%rax,2),%rcx
   1800154c3:	41 80 bc c8 00 04 00 	cmpb   $0x0,0x400(%r8,%rcx,8)
   1800154ca:	00 00 
   1800154cc:	74 06                	je     0x1800154d4
   1800154ce:	c6 02 01             	movb   $0x1,(%rdx)
   1800154d1:	33 c0                	xor    %eax,%eax
   1800154d3:	c3                   	ret
   1800154d4:	b8 fa ff ff ff       	mov    $0xfffffffa,%eax
   1800154d9:	c3                   	ret
   1800154da:	cc                   	int3
   1800154db:	cc                   	int3
   1800154dc:	cc                   	int3
   1800154dd:	cc                   	int3
   1800154de:	cc                   	int3
   1800154df:	cc                   	int3
   1800154e0:	48 8b 15 31 31 09 00 	mov    0x93131(%rip),%rdx        # 0x1800a8618
   1800154e7:	48 8b c1             	mov    %rcx,%rax
   1800154ea:	80 ba f9 03 00 00 00 	cmpb   $0x0,0x3f9(%rdx)
   1800154f1:	75 06                	jne    0x1800154f9
   1800154f3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154f8:	c3                   	ret
   1800154f9:	48 8b 92 90 04 00 00 	mov    0x490(%rdx),%rdx
   180015500:	0f b7 ca             	movzwl %dx,%ecx
   180015503:	89 08                	mov    %ecx,(%rax)
   180015505:	48 8b ca             	mov    %rdx,%rcx
   180015508:	48 c1 e9 10          	shr    $0x10,%rcx
   18001550c:	0f b7 c9             	movzwl %cx,%ecx
   18001550f:	89 48 04             	mov    %ecx,0x4(%rax)
   180015512:	48 8b ca             	mov    %rdx,%rcx
   180015515:	48 c1 e9 20          	shr    $0x20,%rcx
   180015519:	0f b7 c9             	movzwl %cx,%ecx
   18001551c:	89 48 08             	mov    %ecx,0x8(%rax)
   18001551f:	48 c1 ea 30          	shr    $0x30,%rdx
   180015523:	89 50 0c             	mov    %edx,0xc(%rax)
   180015526:	33 c0                	xor    %eax,%eax
   180015528:	c3                   	ret
   180015529:	cc                   	int3
   18001552a:	cc                   	int3
   18001552b:	cc                   	int3
   18001552c:	cc                   	int3
   18001552d:	cc                   	int3
   18001552e:	cc                   	int3
   18001552f:	cc                   	int3
   180015530:	40 55                	rex push %rbp
   180015532:	53                   	push   %rbx
   180015533:	56                   	push   %rsi
   180015534:	48 8d ac 24 80 fe ff 	lea    -0x180(%rsp),%rbp
   18001553b:	ff 
   18001553c:	48 81 ec 80 02 00 00 	sub    $0x280,%rsp
   180015543:	48 8b 05 16 0e 09 00 	mov    0x90e16(%rip),%rax        # 0x1800a6360
   18001554a:	48 33 c4             	xor    %rsp,%rax
   18001554d:	48 89 85 60 01 00 00 	mov    %rax,0x160(%rbp)
   180015554:	8b 05 a6 30 09 00    	mov    0x930a6(%rip),%eax        # 0x1800a8600
   18001555a:	48 8b f2             	mov    %rdx,%rsi
   18001555d:	8b d9                	mov    %ecx,%ebx
   18001555f:	83 f8 01             	cmp    $0x1,%eax
   180015562:	75 0a                	jne    0x18001556e
   180015564:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180015569:	e9 0d 06 00 00       	jmp    0x180015b7b
   18001556e:	48 89 bc 24 a0 02 00 	mov    %rdi,0x2a0(%rsp)
   180015575:	00 
   180015576:	4c 89 a4 24 a8 02 00 	mov    %r12,0x2a8(%rsp)
   18001557d:	00 
   18001557e:	4c 89 b4 24 78 02 00 	mov    %r14,0x278(%rsp)
   180015585:	00 
   180015586:	45 33 f6             	xor    %r14d,%r14d
   180015589:	4c 89 bc 24 70 02 00 	mov    %r15,0x270(%rsp)
   180015590:	00 
   180015591:	4c 8d 3d b0 5b 08 00 	lea    0x85bb0(%rip),%r15        # 0x18009b148
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
```

## `Wrraper_MSDisplayGetDriverVersion` (Address: `0x1800154e0`)
```assembly
   1800154e0:	48 8b 15 31 31 09 00 	mov    0x93131(%rip),%rdx        # 0x1800a8618
   1800154e7:	48 8b c1             	mov    %rcx,%rax
   1800154ea:	80 ba f9 03 00 00 00 	cmpb   $0x0,0x3f9(%rdx)
   1800154f1:	75 06                	jne    0x1800154f9
   1800154f3:	b8 f9 ff ff ff       	mov    $0xfffffff9,%eax
   1800154f8:	c3                   	ret
   1800154f9:	48 8b 92 90 04 00 00 	mov    0x490(%rdx),%rdx
   180015500:	0f b7 ca             	movzwl %dx,%ecx
   180015503:	89 08                	mov    %ecx,(%rax)
   180015505:	48 8b ca             	mov    %rdx,%rcx
   180015508:	48 c1 e9 10          	shr    $0x10,%rcx
   18001550c:	0f b7 c9             	movzwl %cx,%ecx
   18001550f:	89 48 04             	mov    %ecx,0x4(%rax)
   180015512:	48 8b ca             	mov    %rdx,%rcx
   180015515:	48 c1 e9 20          	shr    $0x20,%rcx
   180015519:	0f b7 c9             	movzwl %cx,%ecx
   18001551c:	89 48 08             	mov    %ecx,0x8(%rax)
   18001551f:	48 c1 ea 30          	shr    $0x30,%rdx
   180015523:	89 50 0c             	mov    %edx,0xc(%rax)
   180015526:	33 c0                	xor    %eax,%eax
   180015528:	c3                   	ret
   180015529:	cc                   	int3
   18001552a:	cc                   	int3
   18001552b:	cc                   	int3
   18001552c:	cc                   	int3
   18001552d:	cc                   	int3
   18001552e:	cc                   	int3
   18001552f:	cc                   	int3
   180015530:	40 55                	rex push %rbp
   180015532:	53                   	push   %rbx
   180015533:	56                   	push   %rsi
   180015534:	48 8d ac 24 80 fe ff 	lea    -0x180(%rsp),%rbp
   18001553b:	ff 
   18001553c:	48 81 ec 80 02 00 00 	sub    $0x280,%rsp
   180015543:	48 8b 05 16 0e 09 00 	mov    0x90e16(%rip),%rax        # 0x1800a6360
   18001554a:	48 33 c4             	xor    %rsp,%rax
   18001554d:	48 89 85 60 01 00 00 	mov    %rax,0x160(%rbp)
   180015554:	8b 05 a6 30 09 00    	mov    0x930a6(%rip),%eax        # 0x1800a8600
   18001555a:	48 8b f2             	mov    %rdx,%rsi
   18001555d:	8b d9                	mov    %ecx,%ebx
   18001555f:	83 f8 01             	cmp    $0x1,%eax
   180015562:	75 0a                	jne    0x18001556e
   180015564:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
   180015569:	e9 0d 06 00 00       	jmp    0x180015b7b
   18001556e:	48 89 bc 24 a0 02 00 	mov    %rdi,0x2a0(%rsp)
   180015575:	00 
   180015576:	4c 89 a4 24 a8 02 00 	mov    %r12,0x2a8(%rsp)
   18001557d:	00 
   18001557e:	4c 89 b4 24 78 02 00 	mov    %r14,0x278(%rsp)
   180015585:	00 
   180015586:	45 33 f6             	xor    %r14d,%r14d
   180015589:	4c 89 bc 24 70 02 00 	mov    %r15,0x270(%rsp)
   180015590:	00 
   180015591:	4c 8d 3d b0 5b 08 00 	lea    0x85bb0(%rip),%r15        # 0x18009b148
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
   180015631:	48 8d 4c 24 48       	lea    0x48(%rsp),%rcx
   180015636:	4c 89 73 58          	mov    %r14,0x58(%rbx)
   18001563a:	48 b8 00 00 00 00 00 	movabs $0x4014000000000000,%rax
   180015641:	00 14 40 
   180015644:	48 89 43 60          	mov    %rax,0x60(%rbx)
   180015648:	33 c0                	xor    %eax,%eax
   18001564a:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
   18001564f:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
```

