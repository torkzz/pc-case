.assembly extern mscorlib
{
  .ver 4:0:0:0
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) // .z\V.4..
}
.assembly extern System
{
  .ver 4:0:0:0
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) // .z\V.4..
}
.assembly extern System.Core
{
  .ver 4:0:0:0
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) // .z\V.4..
}
.assembly 'DeviceCommunicationLibrary'
{
  .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilationRelaxationsAttribute::'.ctor'(int32) =  (01 00 08 00 00 00 00 00 ) // ........

  .custom instance void class [mscorlib]System.Runtime.CompilerServices.RuntimeCompatibilityAttribute::'.ctor'() =  (
		01 00 01 00 54 02 16 57 72 61 70 4E 6F 6E 45 78   // ....T..WrapNonEx
		63 65 70 74 69 6F 6E 54 68 72 6F 77 73 01       ) // ceptionThrows.

  .custom instance void class [mscorlib]System.Diagnostics.DebuggableAttribute::'.ctor'(valuetype [mscorlib]System.Diagnostics.DebuggableAttribute/DebuggingModes) =  (01 00 02 00 00 00 00 00 ) // ........

  .custom instance void class [mscorlib]System.Reflection.AssemblyTitleAttribute::'.ctor'(string) =  (
		01 00 1A 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ...DeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 00 00    ) // cationLibrary..

  .custom instance void class [mscorlib]System.Reflection.AssemblyDescriptionAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Reflection.AssemblyConfigurationAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Reflection.AssemblyCompanyAttribute::'.ctor'(string) =  (
		01 00 0C E5 BE AE E8 BD AF E4 B8 AD E5 9B BD 00   // ................
		00                                              ) // .

  .custom instance void class [mscorlib]System.Reflection.AssemblyProductAttribute::'.ctor'(string) =  (
		01 00 1A 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ...DeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 00 00    ) // cationLibrary..

  .custom instance void class [mscorlib]System.Reflection.AssemblyCopyrightAttribute::'.ctor'(string) =  (
		01 00 1E 43 6F 70 79 72 69 67 68 74 20 C2 A9 20   // ...Copyright .. 
		E5 BE AE E8 BD AF E4 B8 AD E5 9B BD 20 32 30 32   // ............ 202
		35 00 00                                        ) // 5..

  .custom instance void class [mscorlib]System.Reflection.AssemblyTrademarkAttribute::'.ctor'(string) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Runtime.InteropServices.ComVisibleAttribute::'.ctor'(bool) =  (01 00 00 00 00 ) // .....

  .custom instance void class [mscorlib]System.Runtime.InteropServices.GuidAttribute::'.ctor'(string) =  (
		01 00 24 62 39 37 62 33 38 36 31 2D 65 30 34 63   // ..$b97b3861-e04c
		2D 34 30 35 62 2D 61 35 63 30 2D 65 37 35 31 34   // -405b-a5c0-e7514
		66 37 34 39 37 39 35 00 00                      ) // f749795..

  .custom instance void class [mscorlib]System.Reflection.AssemblyFileVersionAttribute::'.ctor'(string) =  (01 00 07 31 2E 30 2E 30 2E 30 00 00 ) // ...1.0.0.0..

  .custom instance void class [mscorlib]System.Runtime.Versioning.TargetFrameworkAttribute::'.ctor'(string) =  (
		01 00 1A 2E 4E 45 54 46 72 61 6D 65 77 6F 72 6B   // ....NETFramework
		2C 56 65 72 73 69 6F 6E 3D 76 34 2E 38 01 00 54   // ,Version=v4.8..T
		0E 14 46 72 61 6D 65 77 6F 72 6B 44 69 73 70 6C   // ..FrameworkDispl
		61 79 4E 61 6D 65 12 2E 4E 45 54 20 46 72 61 6D   // ayName..NET Fram
		65 77 6F 72 6B 20 34 2E 38                      ) // ework 4.8

  .hash algorithm 0x00008004
  .ver  1:0:0:0
}
.module DeviceCommunicationLibrary.dll // GUID = {8CE2E8B4-3EB4-4C70-9CD7-88543849E75C}


.namespace DeviceCommunicationLibrary
{
  .class public auto ansi abstract beforefieldinit BaseFrame
  	extends [mscorlib]System.Object
  {
    .field  private  unsigned int16 '<CTRL>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int16 '<CMD>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8[] '<Content>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int16 '<CRC>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 1
    .method family hidebysig 
           instance default unsigned int8[] GetBigEndianBytes (unsigned int16 'value')  cil managed 
    {
        // Method begins at RVA 0x2050
	// Code size 22 (0x16)
	.maxstack 1
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  ldarg.1 
	IL_0001:  call unsigned int8[] class [mscorlib]System.BitConverter::GetBytes(unsigned int16)
	IL_0006:  stloc.0 
	IL_0007:  ldsfld bool [mscorlib]System.BitConverter::IsLittleEndian
	IL_000c:  brfalse.s IL_0014

	IL_000e:  ldloc.0 
	IL_000f:  call void class [mscorlib]System.Array::Reverse(class [mscorlib]System.Array)
	IL_0014:  ldloc.0 
	IL_0015:  ret 
    } // end of method BaseFrame::GetBigEndianBytes

    // method line 2
    .method family hidebysig 
           instance default unsigned int8[] GetBigEndianBytes (unsigned int32 'value')  cil managed 
    {
        // Method begins at RVA 0x2074
	// Code size 22 (0x16)
	.maxstack 1
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  ldarg.1 
	IL_0001:  call unsigned int8[] class [mscorlib]System.BitConverter::GetBytes(unsigned int32)
	IL_0006:  stloc.0 
	IL_0007:  ldsfld bool [mscorlib]System.BitConverter::IsLittleEndian
	IL_000c:  brfalse.s IL_0014

	IL_000e:  ldloc.0 
	IL_000f:  call void class [mscorlib]System.Array::Reverse(class [mscorlib]System.Array)
	IL_0014:  ldloc.0 
	IL_0015:  ret 
    } // end of method BaseFrame::GetBigEndianBytes

    // method line 3
    .method family hidebysig 
           instance default unsigned int16 FromBigEndian (unsigned int8[] data, int32 startIndex)  cil managed 
    {
        // Method begins at RVA 0x2098
	// Code size 38 (0x26)
	.maxstack 5
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  ldc.i4.2 
	IL_0001:  newarr [mscorlib]System.Byte
	IL_0006:  stloc.0 
	IL_0007:  ldarg.1 
	IL_0008:  ldarg.2 
	IL_0009:  ldloc.0 
	IL_000a:  ldc.i4.0 
	IL_000b:  ldc.i4.2 
	IL_000c:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_0011:  ldsfld bool [mscorlib]System.BitConverter::IsLittleEndian
	IL_0016:  brfalse.s IL_001e

	IL_0018:  ldloc.0 
	IL_0019:  call void class [mscorlib]System.Array::Reverse(class [mscorlib]System.Array)
	IL_001e:  ldloc.0 
	IL_001f:  ldc.i4.0 
	IL_0020:  call unsigned int16 class [mscorlib]System.BitConverter::ToUInt16(unsigned int8[], int32)
	IL_0025:  ret 
    } // end of method BaseFrame::FromBigEndian

    // method line 4
    .method family hidebysig 
           instance default unsigned int32 FromBigEndianUInt32 (unsigned int8[] data, int32 startIndex)  cil managed 
    {
        // Method begins at RVA 0x20cc
	// Code size 38 (0x26)
	.maxstack 5
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  ldc.i4.4 
	IL_0001:  newarr [mscorlib]System.Byte
	IL_0006:  stloc.0 
	IL_0007:  ldarg.1 
	IL_0008:  ldarg.2 
	IL_0009:  ldloc.0 
	IL_000a:  ldc.i4.0 
	IL_000b:  ldc.i4.4 
	IL_000c:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_0011:  ldsfld bool [mscorlib]System.BitConverter::IsLittleEndian
	IL_0016:  brfalse.s IL_001e

	IL_0018:  ldloc.0 
	IL_0019:  call void class [mscorlib]System.Array::Reverse(class [mscorlib]System.Array)
	IL_001e:  ldloc.0 
	IL_001f:  ldc.i4.0 
	IL_0020:  call unsigned int32 class [mscorlib]System.BitConverter::ToUInt32(unsigned int8[], int32)
	IL_0025:  ret 
    } // end of method BaseFrame::FromBigEndianUInt32

    // method line 5
    .method public static hidebysig 
           default unsigned int16 ExtractCmdFromBytes (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x20fe
	// Code size 35 (0x23)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldlen 
	IL_0002:  conv.i4 
	IL_0003:  ldc.i4.6 
	IL_0004:  bge.s IL_0008

	IL_0006:  ldc.i4.0 
	IL_0007:  ret 
	IL_0008:  ldarg.0 
	IL_0009:  ldc.i4.0 
	IL_000a:  ldelem.u1 
	IL_000b:  ldc.i4.s 0x41
	IL_000d:  bne.un.s IL_0016

	IL_000f:  ldarg.0 
	IL_0010:  ldc.i4.1 
	IL_0011:  ldelem.u1 
	IL_0012:  ldc.i4.s 0x48
	IL_0014:  beq.s IL_0018

	IL_0016:  ldc.i4.0 
	IL_0017:  ret 
	IL_0018:  ldarg.0 
	IL_0019:  ldc.i4.4 
	IL_001a:  ldelem.u1 
	IL_001b:  ldc.i4.8 
	IL_001c:  shl 
	IL_001d:  ldarg.0 
	IL_001e:  ldc.i4.5 
	IL_001f:  ldelem.u1 
	IL_0020:  or 
	IL_0021:  conv.u2 
	IL_0022:  ret 
    } // end of method BaseFrame::ExtractCmdFromBytes

    // method line 6
    .method public hidebysig specialname 
           instance default unsigned int16 get_CTRL ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2122
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CTRL>k__BackingField'
	IL_0006:  ret 
    } // end of method BaseFrame::get_CTRL

    // method line 7
    .method family hidebysig specialname 
           instance default void set_CTRL (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x212a
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CTRL>k__BackingField'
	IL_0007:  ret 
    } // end of method BaseFrame::set_CTRL

    // method line 8
    .method public hidebysig specialname 
           instance default unsigned int16 get_CMD ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2133
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CMD>k__BackingField'
	IL_0006:  ret 
    } // end of method BaseFrame::get_CMD

    // method line 9
    .method family hidebysig specialname 
           instance default void set_CMD (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x213b
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CMD>k__BackingField'
	IL_0007:  ret 
    } // end of method BaseFrame::set_CMD

    // method line 10
    .method public hidebysig specialname 
           instance default unsigned int8[] get_Content ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2144
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8[] DeviceCommunicationLibrary.BaseFrame::'<Content>k__BackingField'
	IL_0006:  ret 
    } // end of method BaseFrame::get_Content

    // method line 11
    .method family hidebysig specialname 
           instance default void set_Content (unsigned int8[] 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x214c
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8[] DeviceCommunicationLibrary.BaseFrame::'<Content>k__BackingField'
	IL_0007:  ret 
    } // end of method BaseFrame::set_Content

    // method line 12
    .method public hidebysig specialname 
           instance default unsigned int16 get_CRC ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2155
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CRC>k__BackingField'
	IL_0006:  ret 
    } // end of method BaseFrame::get_CRC

    // method line 13
    .method family hidebysig specialname 
           instance default void set_CRC (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x215d
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.BaseFrame::'<CRC>k__BackingField'
	IL_0007:  ret 
    } // end of method BaseFrame::set_CRC

    // method line 14
    .method family hidebysig specialname 
           instance default bool get_IsCRCEnabled ()  cil managed 
    {
        // Method begins at RVA 0x2166
	// Code size 2 (0x2)
	.maxstack 8
	IL_0000:  ldc.i4.0 
	IL_0001:  ret 
    } // end of method BaseFrame::get_IsCRCEnabled

    // method line 15
    .method family virtual hidebysig newslot 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x2169
	// Code size 19 (0x13)
	.maxstack 8
	IL_0000:  ldc.i4.2 
	IL_0001:  ldarg.0 
	IL_0002:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0007:  dup 
	IL_0008:  brtrue.s IL_000e

	IL_000a:  pop 
	IL_000b:  ldc.i4.0 
	IL_000c:  br.s IL_0010

	IL_000e:  ldlen 
	IL_000f:  conv.i4 
	IL_0010:  add 
	IL_0011:  conv.u2 
	IL_0012:  ret 
    } // end of method BaseFrame::CalculateContentLength

    // method line 16
    .method family virtual hidebysig newslot 
           instance default void BuildCTRL ()  cil managed 
    {
        // Method begins at RVA 0x2180
	// Code size 18 (0x12)
	.maxstack 3
	.locals init (
		unsigned int16	V_0)
	IL_0000:  ldarg.0 
	IL_0001:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::CalculateContentLength()
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldc.i4.0 
	IL_0009:  ldloc.0 
	IL_000a:  or 
	IL_000b:  conv.u2 
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CTRL(unsigned int16)
	IL_0011:  ret 
    } // end of method BaseFrame::BuildCTRL

    // method line 17
    .method family virtual hidebysig newslot 
           instance default unsigned int16 CalculateCRC (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x219e
	// Code size 2 (0x2)
	.maxstack 8
	IL_0000:  ldc.i4.0 
	IL_0001:  ret 
    } // end of method BaseFrame::CalculateCRC

    // method line 18
    .method public virtual hidebysig newslot 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x21a4
	// Code size 199 (0xc7)
	.maxstack 3
	.locals init (
		class [mscorlib]System.Collections.Generic.List`1<unsigned int8>	V_0,
		unsigned int8[]	V_1)
	IL_0000:  ldarg.0 
	IL_0001:  callvirt instance void class DeviceCommunicationLibrary.BaseFrame::BuildCTRL()
	IL_0006:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::'.ctor'()
	IL_000b:  stloc.0 
	IL_000c:  ldloc.0 
	IL_000d:  ldc.i4.s 0x41
	IL_000f:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_0014:  ldloc.0 
	IL_0015:  ldc.i4.s 0x48
	IL_0017:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_001c:  ldloc.0 
	IL_001d:  ldarg.0 
	IL_001e:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CTRL()
	IL_0023:  ldc.i4.8 
	IL_0024:  shr 
	IL_0025:  conv.u1 
	IL_0026:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_002b:  ldloc.0 
	IL_002c:  ldarg.0 
	IL_002d:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CTRL()
	IL_0032:  ldc.i4 255
	IL_0037:  and 
	IL_0038:  conv.u1 
	IL_0039:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_003e:  ldloc.0 
	IL_003f:  ldarg.0 
	IL_0040:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	IL_0045:  ldc.i4.8 
	IL_0046:  shr 
	IL_0047:  conv.u1 
	IL_0048:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_004d:  ldloc.0 
	IL_004e:  ldarg.0 
	IL_004f:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	IL_0054:  ldc.i4 255
	IL_0059:  and 
	IL_005a:  conv.u1 
	IL_005b:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_0060:  ldarg.0 
	IL_0061:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0066:  brfalse.s IL_0074

	IL_0068:  ldloc.0 
	IL_0069:  ldarg.0 
	IL_006a:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_006f:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0074:  ldloc.0 
	IL_0075:  ldc.i4.2 
	IL_0076:  call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> class [System.Core]System.Linq.Enumerable::Skip<unsigned int8> (class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, int32)
	IL_007b:  call !!0[] class [System.Core]System.Linq.Enumerable::ToArray<unsigned int8> (class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
	IL_0080:  stloc.1 
	IL_0081:  ldarg.0 
	IL_0082:  ldarg.0 
	IL_0083:  ldloc.1 
	IL_0084:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::CalculateCRC(unsigned int8[])
	IL_0089:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CRC(unsigned int16)
	IL_008e:  ldloc.0 
	IL_008f:  ldarg.0 
	IL_0090:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CRC()
	IL_0095:  ldc.i4.8 
	IL_0096:  shr 
	IL_0097:  conv.u1 
	IL_0098:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_009d:  ldloc.0 
	IL_009e:  ldarg.0 
	IL_009f:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CRC()
	IL_00a4:  ldc.i4 255
	IL_00a9:  and 
	IL_00aa:  conv.u1 
	IL_00ab:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_00b0:  ldloc.0 
	IL_00b1:  ldc.i4.s 0x4d
	IL_00b3:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_00b8:  ldloc.0 
	IL_00b9:  ldc.i4.s 0x49
	IL_00bb:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_00c0:  ldloc.0 
	IL_00c1:  callvirt instance !0[] class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::ToArray()
	IL_00c6:  ret 
    } // end of method BaseFrame::ToBytes

    // method line 19
    .method public virtual hidebysig newslot 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x2278
	// Code size 299 (0x12b)
	.maxstack 5
	.locals init (
		int32	V_0,
		unsigned int16	V_1,
		unsigned int16	V_2,
		int32	V_3,
		unsigned int8[]	V_4,
		unsigned int16	V_5)
	IL_0000:  ldarg.1 
	IL_0001:  ldlen 
	IL_0002:  conv.i4 
	IL_0003:  ldc.i4.s 0x0a
	IL_0005:  bge.s IL_0009

	IL_0007:  ldc.i4.0 
	IL_0008:  ret 
	IL_0009:  ldarg.1 
	IL_000a:  ldc.i4.0 
	IL_000b:  ldelem.u1 
	IL_000c:  ldc.i4.s 0x41
	IL_000e:  bne.un.s IL_0017

	IL_0010:  ldarg.1 
	IL_0011:  ldc.i4.1 
	IL_0012:  ldelem.u1 
	IL_0013:  ldc.i4.s 0x48
	IL_0015:  beq.s IL_0019

	IL_0017:  ldc.i4.0 
	IL_0018:  ret 
	IL_0019:  ldarg.1 
	IL_001a:  ldarg.1 
	IL_001b:  ldlen 
	IL_001c:  conv.i4 
	IL_001d:  ldc.i4.2 
	IL_001e:  sub 
	IL_001f:  ldelem.u1 
	IL_0020:  ldc.i4.s 0x4d
	IL_0022:  bne.un.s IL_002f

	IL_0024:  ldarg.1 
	IL_0025:  ldarg.1 
	IL_0026:  ldlen 
	IL_0027:  conv.i4 
	IL_0028:  ldc.i4.1 
	IL_0029:  sub 
	IL_002a:  ldelem.u1 
	IL_002b:  ldc.i4.s 0x49
	IL_002d:  beq.s IL_0031

	IL_002f:  ldc.i4.0 
	IL_0030:  ret 
	IL_0031:  ldarg.0 
	IL_0032:  ldarg.1 
	IL_0033:  ldc.i4.2 
	IL_0034:  ldelem.u1 
	IL_0035:  ldc.i4.8 
	IL_0036:  shl 
	IL_0037:  ldarg.1 
	IL_0038:  ldc.i4.3 
	IL_0039:  ldelem.u1 
	IL_003a:  or 
	IL_003b:  conv.u2 
	IL_003c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CTRL(unsigned int16)
	IL_0041:  ldarg.0 
	IL_0042:  ldarg.1 
	IL_0043:  ldc.i4.4 
	IL_0044:  ldelem.u1 
	IL_0045:  ldc.i4.8 
	IL_0046:  shl 
	IL_0047:  ldarg.1 
	IL_0048:  ldc.i4.5 
	IL_0049:  ldelem.u1 
	IL_004a:  or 
	IL_004b:  conv.u2 
	IL_004c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0051:  ldarg.0 
	IL_0052:  ldarg.1 
	IL_0053:  ldarg.1 
	IL_0054:  ldlen 
	IL_0055:  conv.i4 
	IL_0056:  ldc.i4.4 
	IL_0057:  sub 
	IL_0058:  ldelem.u1 
	IL_0059:  ldc.i4.8 
	IL_005a:  shl 
	IL_005b:  ldarg.1 
	IL_005c:  ldarg.1 
	IL_005d:  ldlen 
	IL_005e:  conv.i4 
	IL_005f:  ldc.i4.3 
	IL_0060:  sub 
	IL_0061:  ldelem.u1 
	IL_0062:  or 
	IL_0063:  conv.u2 
	IL_0064:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CRC(unsigned int16)
	IL_0069:  ldarg.1 
	IL_006a:  ldlen 
	IL_006b:  conv.i4 
	IL_006c:  ldc.i4.s 0x0a
	IL_006e:  sub 
	IL_006f:  stloc.0 
	IL_0070:  ldloc.0 
	IL_0071:  ldc.i4.0 
	IL_0072:  ble.s IL_0091

	IL_0074:  ldarg.0 
	IL_0075:  ldloc.0 
	IL_0076:  newarr [mscorlib]System.Byte
	IL_007b:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_0080:  ldarg.1 
	IL_0081:  ldc.i4.6 
	IL_0082:  ldarg.0 
	IL_0083:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0088:  ldc.i4.0 
	IL_0089:  ldloc.0 
	IL_008a:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_008f:  br.s IL_009d

	IL_0091:  ldarg.0 
	IL_0092:  ldc.i4.0 
	IL_0093:  newarr [mscorlib]System.Byte
	IL_0098:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_009d:  ldarg.0 
	IL_009e:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CTRL()
	IL_00a3:  ldc.i4 4095
	IL_00a8:  and 
	IL_00a9:  conv.u2 
	IL_00aa:  stloc.1 
	IL_00ab:  ldc.i4.2 
	IL_00ac:  ldloc.0 
	IL_00ad:  add 
	IL_00ae:  conv.u2 
	IL_00af:  stloc.2 
	IL_00b0:  ldloc.1 
	IL_00b1:  ldloc.2 
	IL_00b2:  beq.s IL_00d1

	IL_00b4:  ldstr bytearray (
	70 65 6e 63 7f 95 a6 5e 0d 4e 39 53 4d 91 3a 00  // penc...^.N9SM.:.
	20 00 1f 67 1b 67 3d 00 7b 00 30 00 7d 00 2c 00  //  ..g.g=.{.0.}.,.
	20 00 9e 5b 45 96 3d 00 7b 00 31 00 7d 00 01 )   //  ..[E.=.{.1.}..
	
	IL_00b9:  ldloc.1 
	IL_00ba:  box [mscorlib]System.UInt16
	IL_00bf:  ldloc.2 
	IL_00c0:  box [mscorlib]System.UInt16
	IL_00c5:  call string string::Format(string, object, object)
	IL_00ca:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_00cf:  ldc.i4.0 
	IL_00d0:  ret 
	IL_00d1:  ldarg.0 
	IL_00d2:  call instance bool class DeviceCommunicationLibrary.BaseFrame::get_IsCRCEnabled()
	IL_00d7:  brfalse.s IL_0129

	IL_00d9:  ldarg.1 
	IL_00da:  ldlen 
	IL_00db:  conv.i4 
	IL_00dc:  ldc.i4.4 
	IL_00dd:  sub 
	IL_00de:  stloc.3 
	IL_00df:  ldloc.3 
	IL_00e0:  newarr [mscorlib]System.Byte
	IL_00e5:  stloc.s 4
	IL_00e7:  ldarg.1 
	IL_00e8:  ldc.i4.2 
	IL_00e9:  ldloc.s 4
	IL_00eb:  ldc.i4.0 
	IL_00ec:  ldloc.3 
	IL_00ed:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_00f2:  ldarg.0 
	IL_00f3:  ldloc.s 4
	IL_00f5:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::CalculateCRC(unsigned int8[])
	IL_00fa:  stloc.s 5
	IL_00fc:  ldloc.s 5
	IL_00fe:  ldarg.0 
	IL_00ff:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CRC()
	IL_0104:  beq.s IL_0129

	IL_0106:  ldstr bytearray (
	43 00 52 00 43 00 21 68 8c 9a 31 59 25 8d 3a 00  // C.R.C.!h..1Y%.:.
	20 00 a1 8b 97 7b 3c 50 3d 00 30 00 78 00 7b 00  //  ....{<P=.0.x.{.
	30 00 3a 00 58 00 34 00 7d 00 2c 00 20 00 a5 63  // 0.:.X.4.}.,. ..c
	36 65 3c 50 3d 00 30 00 78 00 7b 00 31 00 3a 00  // 6e<P=.0.x.{.1.:.
	58 00 34 00 7d 00 01 )                           // X.4.}..
	
	IL_010b:  ldloc.s 5
	IL_010d:  box [mscorlib]System.UInt16
	IL_0112:  ldarg.0 
	IL_0113:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CRC()
	IL_0118:  box [mscorlib]System.UInt16
	IL_011d:  call string string::Format(string, object, object)
	IL_0122:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0127:  ldc.i4.0 
	IL_0128:  ret 
	IL_0129:  ldc.i4.1 
	IL_012a:  ret 
    } // end of method BaseFrame::Parse

    // method line 20
    .method family hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x23af
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  ret 
    } // end of method BaseFrame::.ctor

	.property instance unsigned int16 CTRL ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.BaseFrame::get_CTRL () 
		.set instance default void DeviceCommunicationLibrary.BaseFrame::set_CTRL (unsigned int16 'value') 
	}
	.property instance unsigned int16 CMD ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.BaseFrame::get_CMD () 
		.set instance default void DeviceCommunicationLibrary.BaseFrame::set_CMD (unsigned int16 'value') 
	}
	.property instance unsigned int8[] Content ()
	{
		.get instance default unsigned int8[] DeviceCommunicationLibrary.BaseFrame::get_Content () 
		.set instance default void DeviceCommunicationLibrary.BaseFrame::set_Content (unsigned int8[] 'value') 
	}
	.property instance unsigned int16 CRC ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.BaseFrame::get_CRC () 
		.set instance default void DeviceCommunicationLibrary.BaseFrame::set_CRC (unsigned int16 'value') 
	}
	.property instance bool IsCRCEnabled ()
	{
		.get instance default bool DeviceCommunicationLibrary.BaseFrame::get_IsCRCEnabled () 
	}
  } // end of class DeviceCommunicationLibrary.BaseFrame
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit DeviceCommunicator
  	extends [mscorlib]System.Object
  	implements [mscorlib]System.IDisposable  {
    .field  private  class [System]System.IO.Ports.SerialPort _serialPort
    .field  private initonly  object _serialLock
    .field  private initonly  object _bufferLock
    .field  private initonly  object _eventLock
    .field  private  bool _disposed
    .field  private  unsigned int8[] _receiveBuffer
    .field  private initonly  class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16,class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>> _pendingRequests
    .field  private  class [mscorlib]System.EventHandler`1<unsigned int8[]> DataReceived
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  class [mscorlib]System.EventHandler`1<string> ErrorOccurred
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 21
    .method public hidebysig specialname 
           instance default bool get_IsConnected ()  cil managed 
    {
        // Method begins at RVA 0x23b8
	// Code size 50 (0x32)
	.maxstack 2
	.locals init (
		object	V_0,
		bool	V_1,
		bool	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 0
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_0017:  dup 
	  IL_0018:  brtrue.s IL_001e

	  IL_001a:  pop 
	  IL_001b:  ldc.i4.0 
	  IL_001c:  br.s IL_0023

	  IL_001e:  call instance bool class [System]System.IO.Ports.SerialPort::get_IsOpen()
	  IL_0023:  stloc.2 
	  IL_0024:  leave.s IL_0030

	} // end .try 0
	finally  { // 0
	  IL_0026:  ldloc.1 
	  IL_0027:  brfalse.s IL_002f

	  IL_0029:  ldloc.0 
	  IL_002a:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_002f:  endfinally 
	} // end handler 0
	IL_0030:  ldloc.2 
	IL_0031:  ret 
    } // end of method DeviceCommunicator::get_IsConnected

    // method line 22
    .method public hidebysig 
           instance default void EnableDebugLogging ()  cil managed 
    {
        // Method begins at RVA 0x2408
	// Code size 75 (0x4b)
	.maxstack 3
	IL_0000:  ldarg.0 
	IL_0001:  ldsfld class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__9_0'
	IL_0006:  dup 
	IL_0007:  brtrue.s IL_0020

	IL_0009:  pop 
	IL_000a:  ldsfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c' DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9'
	IL_000f:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<EnableDebugLogging>b__9_0'(object, unsigned int8[])
	IL_0015:  newobj instance void class [mscorlib]System.EventHandler`1<unsigned int8[]>::'.ctor'(object, native int)
	IL_001a:  dup 
	IL_001b:  stsfld class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__9_0'
	IL_0020:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::add_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	IL_0025:  ldarg.0 
	IL_0026:  ldsfld class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__9_1'
	IL_002b:  dup 
	IL_002c:  brtrue.s IL_0045

	IL_002e:  pop 
	IL_002f:  ldsfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c' DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9'
	IL_0034:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<EnableDebugLogging>b__9_1'(object, string)
	IL_003a:  newobj instance void class [mscorlib]System.EventHandler`1<string>::'.ctor'(object, native int)
	IL_003f:  dup 
	IL_0040:  stsfld class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__9_1'
	IL_0045:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::add_ErrorOccurred(class [mscorlib]System.EventHandler`1<string>)
	IL_004a:  ret 
    } // end of method DeviceCommunicator::EnableDebugLogging

    // method line 23
    .method public hidebysig specialname 
           instance default void add_DataReceived (class [mscorlib]System.EventHandler`1<unsigned int8[]> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2460
	// Code size 41 (0x29)
	.maxstack 3
	.locals init (
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_0,
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_1,
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator::DataReceived
	IL_0006:  stloc.0 
	IL_0007:  ldloc.0 
	IL_0008:  stloc.1 
	IL_0009:  ldloc.1 
	IL_000a:  ldarg.1 
	IL_000b:  call class [mscorlib]System.Delegate class [mscorlib]System.Delegate::Combine(class [mscorlib]System.Delegate, class [mscorlib]System.Delegate)
	IL_0010:  castclass class [mscorlib]System.EventHandler`1<unsigned int8[]>
	IL_0015:  stloc.2 
	IL_0016:  ldarg.0 
	IL_0017:  ldflda class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator::DataReceived
	IL_001c:  ldloc.2 
	IL_001d:  ldloc.1 
	IL_001e:  call !!0 class [mscorlib]System.Threading.Interlocked::CompareExchange<class [mscorlib]System.EventHandler`1<unsigned int8[]>> ([out] !!0&, !!0, !!0)
	IL_0023:  stloc.0 
	IL_0024:  ldloc.0 
	IL_0025:  ldloc.1 
	IL_0026:  bne.un.s IL_0007

	IL_0028:  ret 
    } // end of method DeviceCommunicator::add_DataReceived

    // method line 24
    .method public hidebysig specialname 
           instance default void remove_DataReceived (class [mscorlib]System.EventHandler`1<unsigned int8[]> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2498
	// Code size 41 (0x29)
	.maxstack 3
	.locals init (
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_0,
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_1,
		class [mscorlib]System.EventHandler`1<unsigned int8[]>	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator::DataReceived
	IL_0006:  stloc.0 
	IL_0007:  ldloc.0 
	IL_0008:  stloc.1 
	IL_0009:  ldloc.1 
	IL_000a:  ldarg.1 
	IL_000b:  call class [mscorlib]System.Delegate class [mscorlib]System.Delegate::Remove(class [mscorlib]System.Delegate, class [mscorlib]System.Delegate)
	IL_0010:  castclass class [mscorlib]System.EventHandler`1<unsigned int8[]>
	IL_0015:  stloc.2 
	IL_0016:  ldarg.0 
	IL_0017:  ldflda class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator::DataReceived
	IL_001c:  ldloc.2 
	IL_001d:  ldloc.1 
	IL_001e:  call !!0 class [mscorlib]System.Threading.Interlocked::CompareExchange<class [mscorlib]System.EventHandler`1<unsigned int8[]>> ([out] !!0&, !!0, !!0)
	IL_0023:  stloc.0 
	IL_0024:  ldloc.0 
	IL_0025:  ldloc.1 
	IL_0026:  bne.un.s IL_0007

	IL_0028:  ret 
    } // end of method DeviceCommunicator::remove_DataReceived

    // method line 25
    .method public hidebysig specialname 
           instance default void add_ErrorOccurred (class [mscorlib]System.EventHandler`1<string> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x24d0
	// Code size 41 (0x29)
	.maxstack 3
	.locals init (
		class [mscorlib]System.EventHandler`1<string>	V_0,
		class [mscorlib]System.EventHandler`1<string>	V_1,
		class [mscorlib]System.EventHandler`1<string>	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator::ErrorOccurred
	IL_0006:  stloc.0 
	IL_0007:  ldloc.0 
	IL_0008:  stloc.1 
	IL_0009:  ldloc.1 
	IL_000a:  ldarg.1 
	IL_000b:  call class [mscorlib]System.Delegate class [mscorlib]System.Delegate::Combine(class [mscorlib]System.Delegate, class [mscorlib]System.Delegate)
	IL_0010:  castclass class [mscorlib]System.EventHandler`1<string>
	IL_0015:  stloc.2 
	IL_0016:  ldarg.0 
	IL_0017:  ldflda class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator::ErrorOccurred
	IL_001c:  ldloc.2 
	IL_001d:  ldloc.1 
	IL_001e:  call !!0 class [mscorlib]System.Threading.Interlocked::CompareExchange<class [mscorlib]System.EventHandler`1<string>> ([out] !!0&, !!0, !!0)
	IL_0023:  stloc.0 
	IL_0024:  ldloc.0 
	IL_0025:  ldloc.1 
	IL_0026:  bne.un.s IL_0007

	IL_0028:  ret 
    } // end of method DeviceCommunicator::add_ErrorOccurred

    // method line 26
    .method public hidebysig specialname 
           instance default void remove_ErrorOccurred (class [mscorlib]System.EventHandler`1<string> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x2508
	// Code size 41 (0x29)
	.maxstack 3
	.locals init (
		class [mscorlib]System.EventHandler`1<string>	V_0,
		class [mscorlib]System.EventHandler`1<string>	V_1,
		class [mscorlib]System.EventHandler`1<string>	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator::ErrorOccurred
	IL_0006:  stloc.0 
	IL_0007:  ldloc.0 
	IL_0008:  stloc.1 
	IL_0009:  ldloc.1 
	IL_000a:  ldarg.1 
	IL_000b:  call class [mscorlib]System.Delegate class [mscorlib]System.Delegate::Remove(class [mscorlib]System.Delegate, class [mscorlib]System.Delegate)
	IL_0010:  castclass class [mscorlib]System.EventHandler`1<string>
	IL_0015:  stloc.2 
	IL_0016:  ldarg.0 
	IL_0017:  ldflda class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator::ErrorOccurred
	IL_001c:  ldloc.2 
	IL_001d:  ldloc.1 
	IL_001e:  call !!0 class [mscorlib]System.Threading.Interlocked::CompareExchange<class [mscorlib]System.EventHandler`1<string>> ([out] !!0&, !!0, !!0)
	IL_0023:  stloc.0 
	IL_0024:  ldloc.0 
	IL_0025:  ldloc.1 
	IL_0026:  bne.un.s IL_0007

	IL_0028:  ret 
    } // end of method DeviceCommunicator::remove_ErrorOccurred

    // method line 27
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x253d
	// Code size 63 (0x3f)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  newobj instance void object::'.ctor'()
	IL_0006:  stfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	IL_000b:  ldarg.0 
	IL_000c:  newobj instance void object::'.ctor'()
	IL_0011:  stfld object DeviceCommunicationLibrary.DeviceCommunicator::_bufferLock
	IL_0016:  ldarg.0 
	IL_0017:  newobj instance void object::'.ctor'()
	IL_001c:  stfld object DeviceCommunicationLibrary.DeviceCommunicator::_eventLock
	IL_0021:  ldarg.0 
	IL_0022:  ldc.i4.0 
	IL_0023:  newarr [mscorlib]System.Byte
	IL_0028:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_002d:  ldarg.0 
	IL_002e:  newobj instance void class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>>::'.ctor'()
	IL_0033:  stfld class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16,class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>> DeviceCommunicationLibrary.DeviceCommunicator::_pendingRequests
	IL_0038:  ldarg.0 
	IL_0039:  call instance void object::'.ctor'()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::.ctor

    // method line 28
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> GetDownloadStatusAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4B 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..KDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 47 65 74 44 6F 77 6E 6C 6F 61 64 53 74 61   // +<GetDownloadSta
		74 75 73 41 73 79 6E 63 3E 64 5F 5F 31 37 00 00 ) // tusAsync>d__17..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x2580
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::GetDownloadStatusAsync

    // method line 29
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.RequestDownloadResponse> RequestDownloadAsync (unsigned int32 address, unsigned int32 fileSize, unsigned int8[] fileId, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 49 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..IDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 52 65 71 75 65 73 74 44 6F 77 6E 6C 6F 61   // +<RequestDownloa
		64 41 73 79 6E 63 3E 64 5F 5F 31 38 00 00       ) // dAsync>d__18..

	.param [4] = int32(0x00001388)
        // Method begins at RVA 0x25cc
	// Code size 88 (0x58)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::address
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::fileSize
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::fileId
	IL_002c:  ldloca.s 0
	IL_002e:  ldarg.s 4
	IL_0030:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::timeoutMs
	IL_0035:  ldloca.s 0
	IL_0037:  ldc.i4.m1 
	IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	IL_003d:  ldloca.s 0
	IL_003f:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	IL_0044:  ldloca.s 0
	IL_0046:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'> ([out] !!0&)
	IL_004b:  ldloca.s 0
	IL_004d:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	IL_0052:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::get_Task()
	IL_0057:  ret 
    } // end of method DeviceCommunicator::RequestDownloadAsync

    // method line 30
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.DownloadDataResponse> DownloadDataAsync (unsigned int32 offset, unsigned int8[] data, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 46 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..FDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 44 6F 77 6E 6C 6F 61 64 44 61 74 61 41 73   // +<DownloadDataAs
		79 6E 63 3E 64 5F 5F 31 39 00 00                ) // ync>d__19..

	.param [3] = int32(0x00001388)
        // Method begins at RVA 0x2630
	// Code size 79 (0x4f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::offset
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::data
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::timeoutMs
	IL_002c:  ldloca.s 0
	IL_002e:  ldc.i4.m1 
	IL_002f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	IL_0034:  ldloca.s 0
	IL_0036:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	IL_003b:  ldloca.s 0
	IL_003d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'> ([out] !!0&)
	IL_0042:  ldloca.s 0
	IL_0044:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	IL_0049:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::get_Task()
	IL_004e:  ret 
    } // end of method DeviceCommunicator::DownloadDataAsync

    // method line 31
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DownloadCompleteAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4A 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..JDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 44 6F 77 6E 6C 6F 61 64 43 6F 6D 70 6C 65   // +<DownloadComple
		74 65 41 73 79 6E 63 3E 64 5F 5F 32 30 00 00    ) // teAsync>d__20..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x268c
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::DownloadCompleteAsync

    // method line 32
    .method public hidebysig 
           instance default bool Connect (string portName, [opt] int32 baudRate)  cil managed 
    {
	.param [2] = int32(0x0001c200)
        // Method begins at RVA 0x26d8
	// Code size 159 (0x9f)
	.maxstack 6
	.locals init (
		object	V_0,
		bool	V_1,
		bool	V_2,
		class [mscorlib]System.Exception	V_3)
	.try { // 1
	  IL_0000:  ldarg.0 
	  IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	  IL_0006:  stloc.0 
	  IL_0007:  ldc.i4.0 
	  IL_0008:  stloc.1 
	  .try { // 0
	    IL_0009:  ldloc.0 
	    IL_000a:  ldloca.s 1
	    IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	    IL_0011:  ldarg.0 
	    IL_0012:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_0017:  dup 
	    IL_0018:  brtrue.s IL_001e

	    IL_001a:  pop 
	    IL_001b:  ldc.i4.0 
	    IL_001c:  br.s IL_0023

	    IL_001e:  call instance bool class [System]System.IO.Ports.SerialPort::get_IsOpen()
	    IL_0023:  brfalse.s IL_002b

	    IL_0025:  ldarg.0 
	    IL_0026:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::Disconnect()
	    IL_002b:  ldarg.0 
	    IL_002c:  ldarg.1 
	    IL_002d:  ldarg.2 
	    IL_002e:  ldc.i4.0 
	    IL_002f:  ldc.i4.8 
	    IL_0030:  ldc.i4.1 
	    IL_0031:  newobj instance void class [System]System.IO.Ports.SerialPort::'.ctor'(string, int32, valuetype [System]System.IO.Ports.Parity, int32, valuetype [System]System.IO.Ports.StopBits)
	    IL_0036:  stfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_003b:  ldarg.0 
	    IL_003c:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_0041:  ldarg.0 
	    IL_0042:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator::SerialPort_DataReceived(object, class [System]System.IO.Ports.SerialDataReceivedEventArgs)
	    IL_0048:  newobj instance void class [System]System.IO.Ports.SerialDataReceivedEventHandler::'.ctor'(object, native int)
	    IL_004d:  callvirt instance void class [System]System.IO.Ports.SerialPort::add_DataReceived(class [System]System.IO.Ports.SerialDataReceivedEventHandler)
	    IL_0052:  ldarg.0 
	    IL_0053:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_0058:  ldarg.0 
	    IL_0059:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator::SerialPort_ErrorReceived(object, class [System]System.IO.Ports.SerialErrorReceivedEventArgs)
	    IL_005f:  newobj instance void class [System]System.IO.Ports.SerialErrorReceivedEventHandler::'.ctor'(object, native int)
	    IL_0064:  callvirt instance void class [System]System.IO.Ports.SerialPort::add_ErrorReceived(class [System]System.IO.Ports.SerialErrorReceivedEventHandler)
	    IL_0069:  ldarg.0 
	    IL_006a:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_006f:  callvirt instance void class [System]System.IO.Ports.SerialPort::Open()
	    IL_0074:  ldc.i4.1 
	    IL_0075:  stloc.2 
	    IL_0076:  leave.s IL_009d

	  } // end .try 0
	  finally  { // 0
	    IL_0078:  ldloc.1 
	    IL_0079:  brfalse.s IL_0081

	    IL_007b:  ldloc.0 
	    IL_007c:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	    IL_0081:  endfinally 
	  } // end handler 0
	} // end .try 1
	catch class [mscorlib]System.Exception { // 1
	  IL_0082:  stloc.3 
	  IL_0083:  ldarg.0 
	  IL_0084:  ldstr bytearray (
	de 8f a5 63 31 59 25 8d 3a 00 20 00 01 )         // ...c1Y%.:. ..
	
	  IL_0089:  ldloc.3 
	  IL_008a:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	  IL_008f:  call string string::Concat(string, string)
	  IL_0094:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	  IL_0099:  ldc.i4.0 
	  IL_009a:  stloc.2 
	  IL_009b:  leave.s IL_009d

	} // end handler 1
	IL_009d:  ldloc.2 
	IL_009e:  ret 
    } // end of method DeviceCommunicator::Connect

    // method line 33
    .method public hidebysig 
           instance default void Disconnect ()  cil managed 
    {
        // Method begins at RVA 0x27a0
	// Code size 119 (0x77)
	.maxstack 3
	.locals init (
		object	V_0,
		bool	V_1)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 0
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_0017:  brfalse.s IL_0064

	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_001f:  ldarg.0 
	  IL_0020:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator::SerialPort_DataReceived(object, class [System]System.IO.Ports.SerialDataReceivedEventArgs)
	  IL_0026:  newobj instance void class [System]System.IO.Ports.SerialDataReceivedEventHandler::'.ctor'(object, native int)
	  IL_002b:  callvirt instance void class [System]System.IO.Ports.SerialPort::remove_DataReceived(class [System]System.IO.Ports.SerialDataReceivedEventHandler)
	  IL_0030:  ldarg.0 
	  IL_0031:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_0036:  ldarg.0 
	  IL_0037:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator::SerialPort_ErrorReceived(object, class [System]System.IO.Ports.SerialErrorReceivedEventArgs)
	  IL_003d:  newobj instance void class [System]System.IO.Ports.SerialErrorReceivedEventHandler::'.ctor'(object, native int)
	  IL_0042:  callvirt instance void class [System]System.IO.Ports.SerialPort::remove_ErrorReceived(class [System]System.IO.Ports.SerialErrorReceivedEventHandler)
	  IL_0047:  ldarg.0 
	  IL_0048:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_004d:  callvirt instance void class [System]System.IO.Ports.SerialPort::Close()
	  IL_0052:  ldarg.0 
	  IL_0053:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_0058:  callvirt instance void class [System]System.ComponentModel.Component::Dispose()
	  IL_005d:  ldarg.0 
	  IL_005e:  ldnull 
	  IL_005f:  stfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	  IL_0064:  leave.s IL_0070

	} // end .try 0
	finally  { // 0
	  IL_0066:  ldloc.1 
	  IL_0067:  brfalse.s IL_006f

	  IL_0069:  ldloc.0 
	  IL_006a:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_006f:  endfinally 
	} // end handler 0
	IL_0070:  ldarg.0 
	IL_0071:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::CancelAllPendingRequests()
	IL_0076:  ret 
    } // end of method DeviceCommunicator::Disconnect

    // method line 34
    .method private hidebysig 
           instance default void SerialPort_DataReceived (object sender, class [System]System.IO.Ports.SerialDataReceivedEventArgs e)  cil managed 
    {
        // Method begins at RVA 0x2834
	// Code size 128 (0x80)
	.maxstack 4
	.locals init (
		object	V_0,
		bool	V_1,
		unsigned int8[]	V_2,
		int32	V_3,
		class [mscorlib]System.Exception	V_4)
	.try { // 1
	  IL_0000:  ldarg.0 
	  IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	  IL_0006:  stloc.0 
	  IL_0007:  ldc.i4.0 
	  IL_0008:  stloc.1 
	  .try { // 0
	    IL_0009:  ldloc.0 
	    IL_000a:  ldloca.s 1
	    IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	    IL_0011:  ldarg.0 
	    IL_0012:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_0017:  dup 
	    IL_0018:  brtrue.s IL_001e

	    IL_001a:  pop 
	    IL_001b:  ldc.i4.0 
	    IL_001c:  br.s IL_0026

	    IL_001e:  call instance int32 class [System]System.IO.Ports.SerialPort::get_BytesToRead()
	    IL_0023:  ldc.i4.0 
	    IL_0024:  cgt 
	    IL_0026:  brfalse.s IL_0056

	    IL_0028:  ldarg.0 
	    IL_0029:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_002e:  callvirt instance int32 class [System]System.IO.Ports.SerialPort::get_BytesToRead()
	    IL_0033:  newarr [mscorlib]System.Byte
	    IL_0038:  stloc.2 
	    IL_0039:  ldarg.0 
	    IL_003a:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_003f:  ldloc.2 
	    IL_0040:  ldc.i4.0 
	    IL_0041:  ldloc.2 
	    IL_0042:  ldlen 
	    IL_0043:  conv.i4 
	    IL_0044:  callvirt instance int32 class [System]System.IO.Ports.SerialPort::Read(unsigned int8[], int32, int32)
	    IL_0049:  stloc.3 
	    IL_004a:  ldloc.3 
	    IL_004b:  ldc.i4.0 
	    IL_004c:  ble.s IL_0056

	    IL_004e:  ldarg.0 
	    IL_004f:  ldloc.2 
	    IL_0050:  ldloc.3 
	    IL_0051:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::ProcessReceivedData(unsigned int8[], int32)
	    IL_0056:  leave.s IL_0062

	  } // end .try 0
	  finally  { // 0
	    IL_0058:  ldloc.1 
	    IL_0059:  brfalse.s IL_0061

	    IL_005b:  ldloc.0 
	    IL_005c:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	    IL_0061:  endfinally 
	  } // end handler 0
	  IL_0062:  leave.s IL_007f

	} // end .try 1
	catch class [mscorlib]System.Exception { // 1
	  IL_0064:  stloc.s 4
	  IL_0066:  ldarg.0 
	  IL_0067:  ldstr bytearray (
	70 65 6e 63 a5 63 36 65 19 95 ef 8b 3a 00 20 00  // penc.c6e....:. .
	01 )                                             // .
	
	  IL_006c:  ldloc.s 4
	  IL_006e:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	  IL_0073:  call string string::Concat(string, string)
	  IL_0078:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	  IL_007d:  leave.s IL_007f

	} // end handler 1
	IL_007f:  ret 
    } // end of method DeviceCommunicator::SerialPort_DataReceived

    // method line 35
    .method private hidebysig 
           instance default void ProcessReceivedData (unsigned int8[] newData, int32 bytesRead)  cil managed 
    {
        // Method begins at RVA 0x28dc
	// Code size 98 (0x62)
	.maxstack 5
	.locals init (
		object	V_0,
		bool	V_1,
		unsigned int8[]	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_bufferLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 0
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	  IL_0017:  ldlen 
	  IL_0018:  conv.i4 
	  IL_0019:  ldarg.2 
	  IL_001a:  add 
	  IL_001b:  newarr [mscorlib]System.Byte
	  IL_0020:  stloc.2 
	  IL_0021:  ldarg.0 
	  IL_0022:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	  IL_0027:  ldc.i4.0 
	  IL_0028:  ldloc.2 
	  IL_0029:  ldc.i4.0 
	  IL_002a:  ldarg.0 
	  IL_002b:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	  IL_0030:  ldlen 
	  IL_0031:  conv.i4 
	  IL_0032:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	  IL_0037:  ldarg.1 
	  IL_0038:  ldc.i4.0 
	  IL_0039:  ldloc.2 
	  IL_003a:  ldarg.0 
	  IL_003b:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	  IL_0040:  ldlen 
	  IL_0041:  conv.i4 
	  IL_0042:  ldarg.2 
	  IL_0043:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	  IL_0048:  ldarg.0 
	  IL_0049:  ldloc.2 
	  IL_004a:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	  IL_004f:  ldarg.0 
	  IL_0050:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::ProcessReceiveBuffer()
	  IL_0055:  leave.s IL_0061

	} // end .try 0
	finally  { // 0
	  IL_0057:  ldloc.1 
	  IL_0058:  brfalse.s IL_0060

	  IL_005a:  ldloc.0 
	  IL_005b:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_0060:  endfinally 
	} // end handler 0
	IL_0061:  ret 
    } // end of method DeviceCommunicator::ProcessReceivedData

    // method line 36
    .method private hidebysig 
           instance default void ProcessReceiveBuffer ()  cil managed 
    {
        // Method begins at RVA 0x295c
	// Code size 169 (0xa9)
	.maxstack 5
	.locals init (
		bool	V_0,
		int32	V_1,
		int32	V_2,
		class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'	V_3,
		int32	V_4,
		unsigned int8[]	V_5)
	IL_0000:  ldc.i4.0 
	IL_0001:  stloc.0 
	IL_0002:  ldarg.0 
	IL_0003:  ldarg.0 
	IL_0004:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_0009:  call instance int32 class DeviceCommunicationLibrary.DeviceCommunicator::FindFrameStart(unsigned int8[])
	IL_000e:  stloc.1 
	IL_000f:  ldloc.1 
	IL_0010:  ldc.i4.0 
	IL_0011:  blt IL_00a2

	IL_0016:  ldarg.0 
	IL_0017:  ldarg.0 
	IL_0018:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_001d:  ldloc.1 
	IL_001e:  call instance int32 class DeviceCommunicationLibrary.DeviceCommunicator::FindFrameEnd(unsigned int8[], int32)
	IL_0023:  stloc.2 
	IL_0024:  ldloc.2 
	IL_0025:  ldc.i4.0 
	IL_0026:  blt.s IL_00a2

	IL_0028:  newobj instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::'.ctor'()
	IL_002d:  stloc.3 
	IL_002e:  ldloc.3 
	IL_002f:  ldarg.0 
	IL_0030:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::'<>4__this'
	IL_0035:  ldloc.2 
	IL_0036:  ldloc.1 
	IL_0037:  sub 
	IL_0038:  ldc.i4.2 
	IL_0039:  add 
	IL_003a:  stloc.s 4
	IL_003c:  ldloc.3 
	IL_003d:  ldloc.s 4
	IL_003f:  newarr [mscorlib]System.Byte
	IL_0044:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::frameData
	IL_0049:  ldarg.0 
	IL_004a:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_004f:  ldloc.1 
	IL_0050:  ldloc.3 
	IL_0051:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::frameData
	IL_0056:  ldc.i4.0 
	IL_0057:  ldloc.s 4
	IL_0059:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_005e:  ldloc.3 
	IL_005f:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::'<ProcessReceiveBuffer>b__0'()
	IL_0065:  newobj instance void class [mscorlib]System.Action::'.ctor'(object, native int)
	IL_006a:  call class [mscorlib]System.Threading.Tasks.Task class [mscorlib]System.Threading.Tasks.Task::Run(class [mscorlib]System.Action)
	IL_006f:  pop 
	IL_0070:  ldarg.0 
	IL_0071:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_0076:  ldlen 
	IL_0077:  conv.i4 
	IL_0078:  ldloc.2 
	IL_0079:  ldc.i4.2 
	IL_007a:  add 
	IL_007b:  sub 
	IL_007c:  newarr [mscorlib]System.Byte
	IL_0081:  stloc.s 5
	IL_0083:  ldarg.0 
	IL_0084:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_0089:  ldloc.2 
	IL_008a:  ldc.i4.2 
	IL_008b:  add 
	IL_008c:  ldloc.s 5
	IL_008e:  ldc.i4.0 
	IL_008f:  ldloc.s 5
	IL_0091:  ldlen 
	IL_0092:  conv.i4 
	IL_0093:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_0098:  ldarg.0 
	IL_0099:  ldloc.s 5
	IL_009b:  stfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator::_receiveBuffer
	IL_00a0:  ldc.i4.1 
	IL_00a1:  stloc.0 
	IL_00a2:  ldloc.0 
	IL_00a3:  brtrue IL_0000

	IL_00a8:  ret 
    } // end of method DeviceCommunicator::ProcessReceiveBuffer

    // method line 37
    .method private hidebysig 
           instance default void ProcessCompleteFrame (unsigned int8[] frameData)  cil managed 
    {
        // Method begins at RVA 0x2a14
	// Code size 114 (0x72)
	.maxstack 4
	.locals init (
		unsigned int16	V_0,
		class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>	V_1,
		class [mscorlib]System.Exception	V_2)
	.try { // 0
	  IL_0000:  ldarg.0 
	  IL_0001:  ldarg.1 
	  IL_0002:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnDataReceived(unsigned int8[])
	  IL_0007:  ldarg.1 
	  IL_0008:  call unsigned int16 class DeviceCommunicationLibrary.BaseFrame::ExtractCmdFromBytes(unsigned int8[])
	  IL_000d:  stloc.0 
	  IL_000e:  ldloc.0 
	  IL_000f:  brtrue.s IL_001e

	  IL_0011:  ldarg.0 
	  IL_0012:  ldstr bytearray (
	e0 65 d5 6c ce 4e 27 5e 70 65 6e 63 2d 4e d0 63  // .e.l.N'^penc-N.c
	d6 53 7d 54 e4 4e 01 )                           // .S}T.N.
	
	  IL_0017:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	  IL_001c:  leave.s IL_0071

	  IL_001e:  ldarg.0 
	  IL_001f:  ldfld class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16,class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>> DeviceCommunicationLibrary.DeviceCommunicator::_pendingRequests
	  IL_0024:  ldloc.0 
	  IL_0025:  ldloca.s 1
	  IL_0027:  callvirt instance bool class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>>::TryRemove(!0, [out] !1&)
	  IL_002c:  brfalse.s IL_0039

	  IL_002e:  ldarg.0 
	  IL_002f:  ldarg.1 
	  IL_0030:  ldloc.0 
	  IL_0031:  ldloc.1 
	  IL_0032:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::ProcessResponseFrame(unsigned int8[], unsigned int16, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>)
	  IL_0037:  br.s IL_0056

	  IL_0039:  ldstr bytearray (
	36 65 30 52 2a 67 f7 8b 42 6c 84 76 27 5e 3a 00  // 6e0R*g..Bl.v'^:.
	20 00 43 00 4d 00 44 00 3d 00 30 00 78 00 7b 00  //  .C.M.D.=.0.x.{.
	30 00 3a 00 58 00 34 00 7d 00 2c 00 20 00 70 65  // 0.:.X.4.}.,. .pe
	6e 63 7f 95 a6 5e 3a 00 20 00 7b 00 31 00 7d 00  // nc...^:. .{.1.}.
	01 )                                             // .
	
	  IL_003e:  ldloc.0 
	  IL_003f:  box [mscorlib]System.UInt16
	  IL_0044:  ldarg.1 
	  IL_0045:  ldlen 
	  IL_0046:  conv.i4 
	  IL_0047:  box [mscorlib]System.Int32
	  IL_004c:  call string string::Format(string, object, object)
	  IL_0051:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0056:  leave.s IL_0071

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_0058:  stloc.2 
	  IL_0059:  ldarg.0 
	  IL_005a:  ldstr bytearray (
	04 59 06 74 8c 5b 74 65 27 5e f6 65 d1 53 1f 75  // .Y.t.[te'^.e.S.u
	19 95 ef 8b 3a 00 20 00 01 )                     // ....:. ..
	
	  IL_005f:  ldloc.2 
	  IL_0060:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	  IL_0065:  call string string::Concat(string, string)
	  IL_006a:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	  IL_006f:  leave.s IL_0071

	} // end handler 0
	IL_0071:  ret 
    } // end of method DeviceCommunicator::ProcessCompleteFrame

    // method line 38
    .method private hidebysig 
           instance default void ProcessResponseFrame (unsigned int8[] frameData, unsigned int16 cmd, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame> tcs)  cil managed 
    {
        // Method begins at RVA 0x2aa4
	// Code size 129 (0x81)
	.maxstack 4
	.locals init (
		class DeviceCommunicationLibrary.BaseFrame	V_0,
		class [mscorlib]System.Exception	V_1)
	.try { // 0
	  IL_0000:  ldarg.0 
	  IL_0001:  ldarg.2 
	  IL_0002:  call instance class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator::CreateResponseByCmd(unsigned int16)
	  IL_0007:  stloc.0 
	  IL_0008:  ldloc.0 
	  IL_0009:  brtrue.s IL_0029

	  IL_000b:  ldarg.3 
	  IL_000c:  ldstr bytearray (
	e0 65 d5 6c 1b 52 fa 5e cd 54 94 5e f9 5b 61 8c  // .e.l.R.^.T.^.[a.
	20 00 28 00 43 00 4d 00 44 00 3d 00 30 00 78 00  //  .(.C.M.D.=.0.x.
	7b 00 30 00 3a 00 58 00 34 00 7d 00 29 00 01 )   // {.0.:.X.4.}.)..
	
	  IL_0011:  ldarg.2 
	  IL_0012:  box [mscorlib]System.UInt16
	  IL_0017:  call string string::Format(string, object)
	  IL_001c:  newobj instance void class [mscorlib]System.InvalidOperationException::'.ctor'(string)
	  IL_0021:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>::TrySetException(class [mscorlib]System.Exception)
	  IL_0026:  pop 
	  IL_0027:  leave.s IL_0080

	  IL_0029:  ldloc.0 
	  IL_002a:  ldarg.1 
	  IL_002b:  callvirt instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	  IL_0030:  brfalse.s IL_003c

	  IL_0032:  ldarg.3 
	  IL_0033:  ldloc.0 
	  IL_0034:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>::TrySetResult(!0)
	  IL_0039:  pop 
	  IL_003a:  br.s IL_0058

	  IL_003c:  ldarg.3 
	  IL_003d:  ldstr bytearray (
	cd 54 94 5e 27 5e e3 89 90 67 31 59 25 8d 20 00  // .T.^'^...g1Y%. .
	28 00 43 00 4d 00 44 00 3d 00 30 00 78 00 7b 00  // (.C.M.D.=.0.x.{.
	30 00 3a 00 58 00 34 00 7d 00 29 00 01 )         // 0.:.X.4.}.)..
	
	  IL_0042:  ldarg.2 
	  IL_0043:  box [mscorlib]System.UInt16
	  IL_0048:  call string string::Format(string, object)
	  IL_004d:  newobj instance void class [mscorlib]System.InvalidOperationException::'.ctor'(string)
	  IL_0052:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>::TrySetException(class [mscorlib]System.Exception)
	  IL_0057:  pop 
	  IL_0058:  leave.s IL_0080

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_005a:  stloc.1 
	  IL_005b:  ldarg.3 
	  IL_005c:  ldstr bytearray (
	04 59 06 74 cd 54 94 5e 27 5e f6 65 d1 53 1f 75  // .Y.t.T.^'^.e.S.u
	19 95 ef 8b 20 00 28 00 43 00 4d 00 44 00 3d 00  // .... .(.C.M.D.=.
	30 00 78 00 7b 00 30 00 3a 00 58 00 34 00 7d 00  // 0.x.{.0.:.X.4.}.
	29 00 3a 00 20 00 7b 00 31 00 7d 00 01 )         // ).:. .{.1.}..
	
	  IL_0061:  ldarg.2 
	  IL_0062:  box [mscorlib]System.UInt16
	  IL_0067:  ldloc.1 
	  IL_0068:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	  IL_006d:  call string string::Format(string, object, object)
	  IL_0072:  ldloc.1 
	  IL_0073:  newobj instance void class [mscorlib]System.InvalidOperationException::'.ctor'(string, class [mscorlib]System.Exception)
	  IL_0078:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>::TrySetException(class [mscorlib]System.Exception)
	  IL_007d:  pop 
	  IL_007e:  leave.s IL_0080

	} // end handler 0
	IL_0080:  ret 
    } // end of method DeviceCommunicator::ProcessResponseFrame

    // method line 39
    .method private hidebysig 
           instance default class DeviceCommunicationLibrary.BaseFrame CreateResponseByCmd (unsigned int16 cmd)  cil managed 
    {
        // Method begins at RVA 0x2b44
	// Code size 182 (0xb6)
	.maxstack 2
	IL_0000:  ldarg.1 
	IL_0001:  ldc.i4 178
	IL_0006:  bgt.un.s IL_0038

	IL_0008:  ldarg.1 
	IL_0009:  ldc.i4 161
	IL_000e:  beq IL_009e

	IL_0013:  ldarg.1 
	IL_0014:  ldc.i4 162
	IL_0019:  beq IL_00a4

	IL_001e:  ldarg.1 
	IL_001f:  ldc.i4 176
	IL_0024:  sub 
	IL_0025:  switch (
	  IL_0098,
	  IL_0092,
	  IL_0074)
	IL_0036:  br.s IL_00b0

	IL_0038:  ldarg.1 
	IL_0039:  ldc.i4 192
	IL_003e:  sub 
	IL_003f:  switch (
	  IL_006e,
	  IL_0080,
	  IL_0086,
	  IL_00b0,
	  IL_00b0,
	  IL_007a)
	IL_005c:  ldarg.1 
	IL_005d:  ldc.i4 207
	IL_0062:  beq.s IL_008c

	IL_0064:  ldarg.1 
	IL_0065:  ldc.i4 208
	IL_006a:  beq.s IL_00aa

	IL_006c:  br.s IL_00b0

	IL_006e:  newobj instance void class DeviceCommunicationLibrary.HandshakeResponse::'.ctor'()
	IL_0073:  ret 
	IL_0074:  newobj instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::'.ctor'()
	IL_0079:  ret 
	IL_007a:  newobj instance void class DeviceCommunicationLibrary.GetDownloadStatusResponse::'.ctor'()
	IL_007f:  ret 
	IL_0080:  newobj instance void class DeviceCommunicationLibrary.RequestDownloadResponse::'.ctor'()
	IL_0085:  ret 
	IL_0086:  newobj instance void class DeviceCommunicationLibrary.DownloadDataResponse::'.ctor'()
	IL_008b:  ret 
	IL_008c:  newobj instance void class DeviceCommunicationLibrary.DownloadCompleteResponse::'.ctor'()
	IL_0091:  ret 
	IL_0092:  newobj instance void class DeviceCommunicationLibrary.ChangeStatusResponse::'.ctor'()
	IL_0097:  ret 
	IL_0098:  newobj instance void class DeviceCommunicationLibrary.RestartResponse::'.ctor'()
	IL_009d:  ret 
	IL_009e:  newobj instance void class DeviceCommunicationLibrary.GetGifInfoResponse::'.ctor'()
	IL_00a3:  ret 
	IL_00a4:  newobj instance void class DeviceCommunicationLibrary.GetFlashInfoResponse::'.ctor'()
	IL_00a9:  ret 
	IL_00aa:  newobj instance void class DeviceCommunicationLibrary.BaseRegisterResponse::'.ctor'()
	IL_00af:  ret 
	IL_00b0:  newobj instance void class DeviceCommunicationLibrary.GenericFrameResponse::'.ctor'()
	IL_00b5:  ret 
    } // end of method DeviceCommunicator::CreateResponseByCmd

    // method line 40
    .method private hidebysig 
           instance default class [mscorlib]System.Type GetResponseType (unsigned int16 cmd)  cil managed 
    {
        // Method begins at RVA 0x2c08
	// Code size 217 (0xd9)
	.maxstack 2
	IL_0000:  ldarg.1 
	IL_0001:  ldc.i4 162
	IL_0006:  bgt.un.s IL_0023

	IL_0008:  ldarg.1 
	IL_0009:  ldc.i4 161
	IL_000e:  beq IL_00c1

	IL_0013:  ldarg.1 
	IL_0014:  ldc.i4 162
	IL_0019:  beq IL_00cc

	IL_001e:  br IL_00d7

	IL_0023:  ldarg.1 
	IL_0024:  ldc.i4 176
	IL_0029:  sub 
	IL_002a:  switch (
	  IL_00b6,
	  IL_00ab,
	  IL_0074)
	IL_003b:  ldarg.1 
	IL_003c:  ldc.i4 192
	IL_0041:  sub 
	IL_0042:  switch (
	  IL_0069,
	  IL_008a,
	  IL_0095,
	  IL_00d7,
	  IL_00d7,
	  IL_007f)
	IL_005f:  ldarg.1 
	IL_0060:  ldc.i4 207
	IL_0065:  beq.s IL_00a0

	IL_0067:  br.s IL_00d7

	IL_0069:  ldtoken DeviceCommunicationLibrary.HandshakeResponse
	IL_006e:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_0073:  ret 
	IL_0074:  ldtoken DeviceCommunicationLibrary.GetHardwareInfoResponse
	IL_0079:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_007e:  ret 
	IL_007f:  ldtoken DeviceCommunicationLibrary.GetDownloadStatusResponse
	IL_0084:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_0089:  ret 
	IL_008a:  ldtoken DeviceCommunicationLibrary.RequestDownloadResponse
	IL_008f:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_0094:  ret 
	IL_0095:  ldtoken DeviceCommunicationLibrary.DownloadDataResponse
	IL_009a:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_009f:  ret 
	IL_00a0:  ldtoken DeviceCommunicationLibrary.DownloadCompleteResponse
	IL_00a5:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_00aa:  ret 
	IL_00ab:  ldtoken DeviceCommunicationLibrary.ChangeStatusResponse
	IL_00b0:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_00b5:  ret 
	IL_00b6:  ldtoken DeviceCommunicationLibrary.RestartResponse
	IL_00bb:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_00c0:  ret 
	IL_00c1:  ldtoken DeviceCommunicationLibrary.GetGifInfoResponse
	IL_00c6:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_00cb:  ret 
	IL_00cc:  ldtoken DeviceCommunicationLibrary.GetFlashInfoResponse
	IL_00d1:  call class [mscorlib]System.Type class [mscorlib]System.Type::GetTypeFromHandle(valuetype [mscorlib]System.RuntimeTypeHandle)
	IL_00d6:  ret 
	IL_00d7:  ldnull 
	IL_00d8:  ret 
    } // end of method DeviceCommunicator::GetResponseType

    // method line 41
    .method private hidebysig 
           instance default int32 FindFrameStart (unsigned int8[] buffer)  cil managed 
    {
        // Method begins at RVA 0x2cf0
	// Code size 36 (0x24)
	.maxstack 3
	.locals init (
		int32	V_0)
	IL_0000:  ldc.i4.0 
	IL_0001:  stloc.0 
	IL_0002:  br.s IL_001a

	IL_0004:  ldarg.1 
	IL_0005:  ldloc.0 
	IL_0006:  ldelem.u1 
	IL_0007:  ldc.i4.s 0x41
	IL_0009:  bne.un.s IL_0016

	IL_000b:  ldarg.1 
	IL_000c:  ldloc.0 
	IL_000d:  ldc.i4.1 
	IL_000e:  add 
	IL_000f:  ldelem.u1 
	IL_0010:  ldc.i4.s 0x48
	IL_0012:  bne.un.s IL_0016

	IL_0014:  ldloc.0 
	IL_0015:  ret 
	IL_0016:  ldloc.0 
	IL_0017:  ldc.i4.1 
	IL_0018:  add 
	IL_0019:  stloc.0 
	IL_001a:  ldloc.0 
	IL_001b:  ldarg.1 
	IL_001c:  ldlen 
	IL_001d:  conv.i4 
	IL_001e:  ldc.i4.1 
	IL_001f:  sub 
	IL_0020:  blt.s IL_0004

	IL_0022:  ldc.i4.m1 
	IL_0023:  ret 
    } // end of method DeviceCommunicator::FindFrameStart

    // method line 42
    .method private hidebysig 
           instance default int32 FindFrameEnd (unsigned int8[] buffer, int32 startIndex)  cil managed 
    {
        // Method begins at RVA 0x2d20
	// Code size 38 (0x26)
	.maxstack 3
	.locals init (
		int32	V_0)
	IL_0000:  ldarg.2 
	IL_0001:  ldc.i4.4 
	IL_0002:  add 
	IL_0003:  stloc.0 
	IL_0004:  br.s IL_001c

	IL_0006:  ldarg.1 
	IL_0007:  ldloc.0 
	IL_0008:  ldelem.u1 
	IL_0009:  ldc.i4.s 0x4d
	IL_000b:  bne.un.s IL_0018

	IL_000d:  ldarg.1 
	IL_000e:  ldloc.0 
	IL_000f:  ldc.i4.1 
	IL_0010:  add 
	IL_0011:  ldelem.u1 
	IL_0012:  ldc.i4.s 0x49
	IL_0014:  bne.un.s IL_0018

	IL_0016:  ldloc.0 
	IL_0017:  ret 
	IL_0018:  ldloc.0 
	IL_0019:  ldc.i4.1 
	IL_001a:  add 
	IL_001b:  stloc.0 
	IL_001c:  ldloc.0 
	IL_001d:  ldarg.1 
	IL_001e:  ldlen 
	IL_001f:  conv.i4 
	IL_0020:  ldc.i4.1 
	IL_0021:  sub 
	IL_0022:  blt.s IL_0006

	IL_0024:  ldc.i4.m1 
	IL_0025:  ret 
    } // end of method DeviceCommunicator::FindFrameEnd

    // method line 43
    .method private hidebysig 
           instance default void SerialPort_ErrorReceived (object sender, class [System]System.IO.Ports.SerialErrorReceivedEventArgs e)  cil managed 
    {
        // Method begins at RVA 0x2d52
	// Code size 28 (0x1c)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldstr bytearray (
	32 4e e3 53 19 95 ef 8b 3a 00 20 00 7b 00 30 00  // 2N.S....:. .{.0.
	7d 00 01 )                                       // }..
	
	IL_0006:  ldarg.2 
	IL_0007:  callvirt instance valuetype [System]System.IO.Ports.SerialError class [System]System.IO.Ports.SerialErrorReceivedEventArgs::get_EventType()
	IL_000c:  box [System]System.IO.Ports.SerialError
	IL_0011:  call string string::Format(string, object)
	IL_0016:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	IL_001b:  ret 
    } // end of method DeviceCommunicator::SerialPort_ErrorReceived

    // method line 44
    .method public hidebysig 
           instance default bool SendFrame (class DeviceCommunicationLibrary.BaseFrame frame)  cil managed 
    {
        // Method begins at RVA 0x2d70
	// Code size 150 (0x96)
	.maxstack 4
	.locals init (
		object	V_0,
		bool	V_1,
		bool	V_2,
		unsigned int8[]	V_3,
		class [mscorlib]System.Exception	V_4)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_serialLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 1
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  call instance bool class DeviceCommunicationLibrary.DeviceCommunicator::get_IsConnected()
	  IL_0017:  brtrue.s IL_001d

	  IL_0019:  ldc.i4.0 
	  IL_001a:  stloc.2 
	  IL_001b:  leave.s IL_0094

	  IL_001d:  nop 
	  .try { // 0
	    IL_001e:  ldarg.1 
	    IL_001f:  callvirt instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	    IL_0024:  stloc.3 
	    IL_0025:  ldstr " "
	    IL_002a:  ldloc.3 
	    IL_002b:  ldsfld class [mscorlib]System.Func`2<unsigned int8,string> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__33_0'
	    IL_0030:  dup 
	    IL_0031:  brtrue.s IL_004a

	    IL_0033:  pop 
	    IL_0034:  ldsfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c' DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9'
	    IL_0039:  ldftn instance string class DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<SendFrame>b__33_0'(unsigned int8)
	    IL_003f:  newobj instance void class [mscorlib]System.Func`2<unsigned int8, string>::'.ctor'(object, native int)
	    IL_0044:  dup 
	    IL_0045:  stsfld class [mscorlib]System.Func`2<unsigned int8,string> DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9__33_0'
	    IL_004a:  call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!1> class [System.Core]System.Linq.Enumerable::Select<unsigned int8, string> (class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Func`2<!!0,!!1>)
	    IL_004f:  call string string::Join(string, class [mscorlib]System.Collections.Generic.IEnumerable`1<string>)
	    IL_0054:  call void class [mscorlib]System.Console::WriteLine(string)
	    IL_0059:  ldarg.0 
	    IL_005a:  ldfld class [System]System.IO.Ports.SerialPort DeviceCommunicationLibrary.DeviceCommunicator::_serialPort
	    IL_005f:  ldloc.3 
	    IL_0060:  ldc.i4.0 
	    IL_0061:  ldloc.3 
	    IL_0062:  ldlen 
	    IL_0063:  conv.i4 
	    IL_0064:  callvirt instance void class [System]System.IO.Ports.SerialPort::Write(unsigned int8[], int32, int32)
	    IL_0069:  ldc.i4.1 
	    IL_006a:  stloc.2 
	    IL_006b:  leave.s IL_0094

	  } // end .try 0
	  catch class [mscorlib]System.Exception { // 0
	    IL_006d:  stloc.s 4
	    IL_006f:  ldarg.0 
	    IL_0070:  ldstr bytearray (
	d1 53 01 90 31 59 25 8d 3a 00 20 00 01 )         // .S..1Y%.:. ..
	
	    IL_0075:  ldloc.s 4
	    IL_0077:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	    IL_007c:  call string string::Concat(string, string)
	    IL_0081:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::OnErrorOccurred(string)
	    IL_0086:  ldc.i4.0 
	    IL_0087:  stloc.2 
	    IL_0088:  leave.s IL_0094

	  } // end handler 0
	} // end .try 1
	finally  { // 1
	  IL_008a:  ldloc.1 
	  IL_008b:  brfalse.s IL_0093

	  IL_008d:  ldloc.0 
	  IL_008e:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_0093:  endfinally 
	} // end handler 1
	IL_0094:  ldloc.2 
	IL_0095:  ret 
    } // end of method DeviceCommunicator::SendFrame

    // method line 45
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.HandshakeResponse> HandshakeAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 43 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..CDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 48 61 6E 64 73 68 61 6B 65 41 73 79 6E 63   // +<HandshakeAsync
		3E 64 5F 5F 33 34 00 00                         ) // >d__34..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x2e30
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::HandshakeAsync

    // method line 46
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> GetHardwareInfoAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 49 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..IDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 47 65 74 48 61 72 64 77 61 72 65 49 6E 66   // +<GetHardwareInf
		6F 41 73 79 6E 63 3E 64 5F 5F 33 35 00 00       ) // oAsync>d__35..

	.param [1] = int32(0x00000bb8)
        // Method begins at RVA 0x2e7c
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::GetHardwareInfoAsync

    // method line 47
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<bool> SendFrameWithRetryAsync (class DeviceCommunicationLibrary.BaseFrame frame, [opt] int32 maxRetries, [opt] int32 intervalMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4C 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..LDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 53 65 6E 64 46 72 61 6D 65 57 69 74 68 52   // +<SendFrameWithR
		65 74 72 79 41 73 79 6E 63 3E 64 5F 5F 33 36 00   // etryAsync>d__36.
		00                                              ) // .

	.param [2] = int32(0x00000003)
	.param [3] = int32(0x000003e8)
        // Method begins at RVA 0x2ec8
	// Code size 79 (0x4f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld class DeviceCommunicationLibrary.BaseFrame DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::frame
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::maxRetries
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::intervalMs
	IL_002c:  ldloca.s 0
	IL_002e:  ldc.i4.m1 
	IL_002f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	IL_0034:  ldloca.s 0
	IL_0036:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	IL_003b:  ldloca.s 0
	IL_003d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'> ([out] !!0&)
	IL_0042:  ldloca.s 0
	IL_0044:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	IL_0049:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::get_Task()
	IL_004e:  ret 
    } // end of method DeviceCommunicator::SendFrameWithRetryAsync

    // method line 48
    .method private hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<!!T> SendRequestAsync<.ctor (class DeviceCommunicationLibrary.BaseFrame) T> (class DeviceCommunicationLibrary.BaseFrame 'request', int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 47 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..GDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 53 65 6E 64 52 65 71 75 65 73 74 41 73 79   // +<SendRequestAsy
		6E 63 3E 64 5F 5F 33 37 60 31 00 00             ) // nc>d__37`1..

        // Method begins at RVA 0x2f24
	// Code size 71 (0x47)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!T>	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!!T>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld class DeviceCommunicationLibrary.BaseFrame valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'request'
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::timeoutMs
	IL_0024:  ldloca.s 0
	IL_0026:  ldc.i4.m1 
	IL_0027:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'<>1__state'
	IL_002c:  ldloca.s 0
	IL_002e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'<>t__builder'
	IL_0033:  ldloca.s 0
	IL_0035:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!!T>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>> ([out] !!0&)
	IL_003a:  ldloca.s 0
	IL_003c:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!!0>::'<>t__builder'
	IL_0041:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!!T>::get_Task()
	IL_0046:  ret 
    } // end of method DeviceCommunicator::SendRequestAsync

    // method line 49
    .method private hidebysig 
           instance default void CancelAllPendingRequests ()  cil managed 
    {
        // Method begins at RVA 0x2f78
	// Code size 70 (0x46)
	.maxstack 3
	.locals init (
		class [mscorlib]System.Collections.Generic.IEnumerator`1<unsigned int16>	V_0,
		unsigned int16	V_1,
		class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16,class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>> DeviceCommunicationLibrary.DeviceCommunicator::_pendingRequests
	IL_0006:  callvirt instance class [mscorlib]System.Collections.Generic.ICollection`1<!0> class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>>::get_Keys()
	IL_000b:  callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<unsigned int16>::GetEnumerator()
	IL_0010:  stloc.0 
	.try { // 0
	  IL_0011:  br.s IL_0031

	  IL_0013:  ldloc.0 
	  IL_0014:  callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<unsigned int16>::get_Current()
	  IL_0019:  stloc.1 
	  IL_001a:  ldarg.0 
	  IL_001b:  ldfld class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16,class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>> DeviceCommunicationLibrary.DeviceCommunicator::_pendingRequests
	  IL_0020:  ldloc.1 
	  IL_0021:  ldloca.s 2
	  IL_0023:  callvirt instance bool class [mscorlib]System.Collections.Concurrent.ConcurrentDictionary`2<unsigned int16, class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>>::TryRemove(!0, [out] !1&)
	  IL_0028:  brfalse.s IL_0031

	  IL_002a:  ldloc.2 
	  IL_002b:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<class DeviceCommunicationLibrary.BaseFrame>::TrySetCanceled()
	  IL_0030:  pop 
	  IL_0031:  ldloc.0 
	  IL_0032:  callvirt instance bool class [mscorlib]System.Collections.IEnumerator::MoveNext()
	  IL_0037:  brtrue.s IL_0013

	  IL_0039:  leave.s IL_0045

	} // end .try 0
	finally  { // 0
	  IL_003b:  ldloc.0 
	  IL_003c:  brfalse.s IL_0044

	  IL_003e:  ldloc.0 
	  IL_003f:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	  IL_0044:  endfinally 
	} // end handler 0
	IL_0045:  ret 
    } // end of method DeviceCommunicator::CancelAllPendingRequests

    // method line 50
    .method private hidebysig 
           instance default void OnDataReceived (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x2fdc
	// Code size 49 (0x31)
	.maxstack 3
	.locals init (
		object	V_0,
		bool	V_1)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_eventLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 0
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> DeviceCommunicationLibrary.DeviceCommunicator::DataReceived
	  IL_0017:  dup 
	  IL_0018:  brtrue.s IL_001d

	  IL_001a:  pop 
	  IL_001b:  leave.s IL_0030

	  IL_001d:  ldarg.0 
	  IL_001e:  ldarg.1 
	  IL_001f:  callvirt instance void class [mscorlib]System.EventHandler`1<unsigned int8[]>::Invoke(object, !0)
	  IL_0024:  leave.s IL_0030

	} // end .try 0
	finally  { // 0
	  IL_0026:  ldloc.1 
	  IL_0027:  brfalse.s IL_002f

	  IL_0029:  ldloc.0 
	  IL_002a:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_002f:  endfinally 
	} // end handler 0
	IL_0030:  ret 
    } // end of method DeviceCommunicator::OnDataReceived

    // method line 51
    .method private hidebysig 
           instance default void OnErrorOccurred (string message)  cil managed 
    {
        // Method begins at RVA 0x302c
	// Code size 49 (0x31)
	.maxstack 3
	.locals init (
		object	V_0,
		bool	V_1)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld object DeviceCommunicationLibrary.DeviceCommunicator::_eventLock
	IL_0006:  stloc.0 
	IL_0007:  ldc.i4.0 
	IL_0008:  stloc.1 
	.try { // 0
	  IL_0009:  ldloc.0 
	  IL_000a:  ldloca.s 1
	  IL_000c:  call void class [mscorlib]System.Threading.Monitor::Enter(object, [out] bool&)
	  IL_0011:  ldarg.0 
	  IL_0012:  ldfld class [mscorlib]System.EventHandler`1<string> DeviceCommunicationLibrary.DeviceCommunicator::ErrorOccurred
	  IL_0017:  dup 
	  IL_0018:  brtrue.s IL_001d

	  IL_001a:  pop 
	  IL_001b:  leave.s IL_0030

	  IL_001d:  ldarg.0 
	  IL_001e:  ldarg.1 
	  IL_001f:  callvirt instance void class [mscorlib]System.EventHandler`1<string>::Invoke(object, !0)
	  IL_0024:  leave.s IL_0030

	} // end .try 0
	finally  { // 0
	  IL_0026:  ldloc.1 
	  IL_0027:  brfalse.s IL_002f

	  IL_0029:  ldloc.0 
	  IL_002a:  call void class [mscorlib]System.Threading.Monitor::Exit(object)
	  IL_002f:  endfinally 
	} // end handler 0
	IL_0030:  ret 
    } // end of method DeviceCommunicator::OnErrorOccurred

    // method line 52
    .method private hidebysig 
           instance default unsigned int16 GetExpectedResponseCmd (unsigned int16 requestCmd)  cil managed 
    {
        // Method begins at RVA 0x307c
	// Code size 190 (0xbe)
	.maxstack 2
	IL_0000:  ldarg.1 
	IL_0001:  ldc.i4.s 0x72
	IL_0003:  bgt.un.s IL_0034

	IL_0005:  ldarg.1 
	IL_0006:  ldc.i4.s 0x61
	IL_0008:  sub 
	IL_0009:  switch (
	  IL_00a0,
	  IL_00a6,
	  IL_00b2)
	IL_001a:  ldarg.1 
	IL_001b:  ldc.i4.s 0x70
	IL_001d:  sub 
	IL_001e:  switch (
	  IL_009a,
	  IL_0094,
	  IL_0070)
	IL_002f:  br IL_00b8

	IL_0034:  ldarg.1 
	IL_0035:  ldc.i4 128
	IL_003a:  sub 
	IL_003b:  switch (
	  IL_006a,
	  IL_007c,
	  IL_0082,
	  IL_008e,
	  IL_00b8,
	  IL_0076)
	IL_0058:  ldarg.1 
	IL_0059:  ldc.i4 143
	IL_005e:  beq.s IL_0088

	IL_0060:  ldarg.1 
	IL_0061:  ldc.i4 144
	IL_0066:  beq.s IL_00ac

	IL_0068:  br.s IL_00b8

	IL_006a:  ldc.i4 192
	IL_006f:  ret 
	IL_0070:  ldc.i4 178
	IL_0075:  ret 
	IL_0076:  ldc.i4 197
	IL_007b:  ret 
	IL_007c:  ldc.i4 193
	IL_0081:  ret 
	IL_0082:  ldc.i4 194
	IL_0087:  ret 
	IL_0088:  ldc.i4 207
	IL_008d:  ret 
	IL_008e:  ldc.i4 195
	IL_0093:  ret 
	IL_0094:  ldc.i4 177
	IL_0099:  ret 
	IL_009a:  ldc.i4 176
	IL_009f:  ret 
	IL_00a0:  ldc.i4 161
	IL_00a5:  ret 
	IL_00a6:  ldc.i4 162
	IL_00ab:  ret 
	IL_00ac:  ldc.i4 208
	IL_00b1:  ret 
	IL_00b2:  ldc.i4 162
	IL_00b7:  ret 
	IL_00b8:  ldarg.1 
	IL_00b9:  ldc.i4.s 0x40
	IL_00bb:  or 
	IL_00bc:  conv.u2 
	IL_00bd:  ret 
    } // end of method DeviceCommunicator::GetExpectedResponseCmd

    // method line 53
    .method public final virtual hidebysig newslot 
           instance default void Dispose ()  cil managed 
    {
        // Method begins at RVA 0x3146
	// Code size 28 (0x1c)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld bool DeviceCommunicationLibrary.DeviceCommunicator::_disposed
	IL_0006:  brtrue.s IL_001b

	IL_0008:  ldarg.0 
	IL_0009:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::Disconnect()
	IL_000e:  ldarg.0 
	IL_000f:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::CancelAllPendingRequests()
	IL_0014:  ldarg.0 
	IL_0015:  ldc.i4.1 
	IL_0016:  stfld bool DeviceCommunicationLibrary.DeviceCommunicator::_disposed
	IL_001b:  ret 
    } // end of method DeviceCommunicator::Dispose

    // method line 54
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.ChangeStatusResponse> ChangeStatusAsync (unsigned int8 status, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 46 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..FDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 43 68 61 6E 67 65 53 74 61 74 75 73 41 73   // +<ChangeStatusAs
		79 6E 63 3E 64 5F 5F 34 33 00 00                ) // ync>d__43..

	.param [2] = int32(0x00001388)
        // Method begins at RVA 0x3164
	// Code size 71 (0x47)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld unsigned int8 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::status
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::timeoutMs
	IL_0024:  ldloca.s 0
	IL_0026:  ldc.i4.m1 
	IL_0027:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	IL_002c:  ldloca.s 0
	IL_002e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	IL_0033:  ldloca.s 0
	IL_0035:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'> ([out] !!0&)
	IL_003a:  ldloca.s 0
	IL_003c:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	IL_0041:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::get_Task()
	IL_0046:  ret 
    } // end of method DeviceCommunicator::ChangeStatusAsync

    // method line 55
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.RestartResponse> RestartAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 41 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..ADeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 52 65 73 74 61 72 74 41 73 79 6E 63 3E 64   // +<RestartAsync>d
		5F 5F 34 34 00 00                               ) // __44..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x31b8
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::RestartAsync

    // method line 56
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetGifInfoResponse> GetGifInfoAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 44 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..DDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 47 65 74 47 69 66 49 6E 66 6F 41 73 79 6E   // +<GetGifInfoAsyn
		63 3E 64 5F 5F 34 35 00 00                      ) // c>d__45..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x3204
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::GetGifInfoAsync

    // method line 57
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> GetFlashInfoAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 46 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..FDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 47 65 74 46 6C 61 73 68 49 6E 66 6F 41 73   // +<GetFlashInfoAs
		79 6E 63 3E 64 5F 5F 34 36 00 00                ) // ync>d__46..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x3250
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::GetFlashInfoAsync

    // method line 58
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> ConnectDeviceAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 47 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..GDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 43 6F 6E 6E 65 63 74 44 65 76 69 63 65 41   // +<ConnectDeviceA
		73 79 6E 63 3E 64 5F 5F 34 37 00 00             ) // sync>d__47..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x329c
	// Code size 63 (0x3f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::timeoutMs
	IL_001c:  ldloca.s 0
	IL_001e:  ldc.i4.m1 
	IL_001f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	IL_0024:  ldloca.s 0
	IL_0026:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	IL_002b:  ldloca.s 0
	IL_002d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'> ([out] !!0&)
	IL_0032:  ldloca.s 0
	IL_0034:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	IL_0039:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::get_Task()
	IL_003e:  ret 
    } // end of method DeviceCommunicator::ConnectDeviceAsync

    // method line 59
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<bool> ExitRunningAsync ([opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 45 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..EDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 45 78 69 74 52 75 6E 6E 69 6E 67 41 73 79   // +<ExitRunningAsy
		6E 63 3E 64 5F 5F 34 38 00 00                   ) // nc>d__48..

	.param [1] = int32(0x00001388)
        // Method begins at RVA 0x32e8
	// Code size 55 (0x37)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldc.i4.m1 
	IL_0017:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	IL_001c:  ldloca.s 0
	IL_001e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	IL_0023:  ldloca.s 0
	IL_0025:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'> ([out] !!0&)
	IL_002a:  ldloca.s 0
	IL_002c:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	IL_0031:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::get_Task()
	IL_0036:  ret 
    } // end of method DeviceCommunicator::ExitRunningAsync

    // method line 60
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse> SetValueRegisterAsync (unsigned int16 registerId, unsigned int32 'value', [opt] bool needReply, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4A 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..JDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 53 65 74 56 61 6C 75 65 52 65 67 69 73 74   // +<SetValueRegist
		65 72 41 73 79 6E 63 3E 64 5F 5F 34 39 00 00    ) // erAsync>d__49..

	.param [3] = bool(true)
	.param [4] = int32(0x00001388)
        // Method begins at RVA 0x332c
	// Code size 88 (0x58)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld unsigned int16 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::registerId
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'value'
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::needReply
	IL_002c:  ldloca.s 0
	IL_002e:  ldarg.s 4
	IL_0030:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::timeoutMs
	IL_0035:  ldloca.s 0
	IL_0037:  ldc.i4.m1 
	IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	IL_003d:  ldloca.s 0
	IL_003f:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	IL_0044:  ldloca.s 0
	IL_0046:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'> ([out] !!0&)
	IL_004b:  ldloca.s 0
	IL_004d:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	IL_0052:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_Task()
	IL_0057:  ret 
    } // end of method DeviceCommunicator::SetValueRegisterAsync

    // method line 61
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse> SetValueRegistersAsync (class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> registers, [opt] bool needReply, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4B 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..KDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 53 65 74 56 61 6C 75 65 52 65 67 69 73 74   // +<SetValueRegist
		65 72 73 41 73 79 6E 63 3E 64 5F 5F 35 30 00 00 ) // ersAsync>d__50..

	.param [2] = bool(true)
	.param [3] = int32(0x00001388)
        // Method begins at RVA 0x3390
	// Code size 79 (0x4f)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::registers
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::needReply
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::timeoutMs
	IL_002c:  ldloca.s 0
	IL_002e:  ldc.i4.m1 
	IL_002f:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	IL_0034:  ldloca.s 0
	IL_0036:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	IL_003b:  ldloca.s 0
	IL_003d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'> ([out] !!0&)
	IL_0042:  ldloca.s 0
	IL_0044:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	IL_0049:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_Task()
	IL_004e:  ret 
    } // end of method DeviceCommunicator::SetValueRegistersAsync

    // method line 62
    .method public hidebysig 
           instance default class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse> SetStringRegisterAsync (unsigned int16 registerId, string 'value', [opt] bool needReply, [opt] int32 timeoutMs)  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.AsyncStateMachineAttribute::'.ctor'(class [mscorlib]System.Type) =  (
		01 00 4B 44 65 76 69 63 65 43 6F 6D 6D 75 6E 69   // ..KDeviceCommuni
		63 61 74 69 6F 6E 4C 69 62 72 61 72 79 2E 44 65   // cationLibrary.De
		76 69 63 65 43 6F 6D 6D 75 6E 69 63 61 74 6F 72   // viceCommunicator
		2B 3C 53 65 74 53 74 72 69 6E 67 52 65 67 69 73   // +<SetStringRegis
		74 65 72 41 73 79 6E 63 3E 64 5F 5F 35 31 00 00 ) // terAsync>d__51..

	.param [3] = bool(true)
	.param [4] = int32(0x00001388)
        // Method begins at RVA 0x33ec
	// Code size 88 (0x58)
	.maxstack 2
	.locals init (
		valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'	V_0)
	IL_0000:  ldloca.s 0
	IL_0002:  call valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Create()
	IL_0007:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	IL_000c:  ldloca.s 0
	IL_000e:  ldarg.0 
	IL_000f:  stfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>4__this'
	IL_0014:  ldloca.s 0
	IL_0016:  ldarg.1 
	IL_0017:  stfld unsigned int16 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::registerId
	IL_001c:  ldloca.s 0
	IL_001e:  ldarg.2 
	IL_001f:  stfld string DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'value'
	IL_0024:  ldloca.s 0
	IL_0026:  ldarg.3 
	IL_0027:  stfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::needReply
	IL_002c:  ldloca.s 0
	IL_002e:  ldarg.s 4
	IL_0030:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::timeoutMs
	IL_0035:  ldloca.s 0
	IL_0037:  ldc.i4.m1 
	IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	IL_003d:  ldloca.s 0
	IL_003f:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	IL_0044:  ldloca.s 0
	IL_0046:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::Start<valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'> ([out] !!0&)
	IL_004b:  ldloca.s 0
	IL_004d:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	IL_0052:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!0> valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_Task()
	IL_0057:  ret 
    } // end of method DeviceCommunicator::SetStringRegisterAsync

	.property instance bool IsConnected ()
	{
		.get instance default bool DeviceCommunicationLibrary.DeviceCommunicator::get_IsConnected () 
	}
	.event class [mscorlib]System.EventHandler`1<unsigned int8[]> DataReceived
	{
		.addon instance default void DeviceCommunicationLibrary.DeviceCommunicator::add_DataReceived (class [mscorlib]System.EventHandler`1<unsigned int8[]> 'value') 
		.removeon instance default void DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived (class [mscorlib]System.EventHandler`1<unsigned int8[]> 'value') 
	}
	.event class [mscorlib]System.EventHandler`1<string> ErrorOccurred
	{
		.addon instance default void DeviceCommunicationLibrary.DeviceCommunicator::add_ErrorOccurred (class [mscorlib]System.EventHandler`1<string> 'value') 
		.removeon instance default void DeviceCommunicationLibrary.DeviceCommunicator::remove_ErrorOccurred (class [mscorlib]System.EventHandler`1<string> 'value') 
	}
  .class nested private auto ansi sealed serializable beforefieldinit '<>c'
  	extends [mscorlib]System.Object
  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public static initonly  class DeviceCommunicationLibrary.DeviceCommunicator/'<>c' '<>9'
    .field  public static  class [mscorlib]System.EventHandler`1<unsigned int8[]> '<>9__9_0'
    .field  public static  class [mscorlib]System.EventHandler`1<string> '<>9__9_1'
    .field  public static  class [mscorlib]System.Func`2<unsigned int8,string> '<>9__33_0'

    // method line 182
    .method private static hidebysig specialname rtspecialname 
           default void '.cctor' ()  cil managed 
    {
        // Method begins at RVA 0x3f93
	// Code size 11 (0xb)
	.maxstack 8
	IL_0000:  newobj instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'.ctor'()
	IL_0005:  stsfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c' DeviceCommunicationLibrary.DeviceCommunicator/'<>c'::'<>9'
	IL_000a:  ret 
    } // end of method <>c::.cctor

    // method line 183
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3f9f
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  ret 
    } // end of method <>c::.ctor

    // method line 184
    .method assembly hidebysig 
           instance default void '<EnableDebugLogging>b__9_0' (object s, unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3fa8
	// Code size 58 (0x3a)
	.maxstack 6
	.locals init (
		unsigned int16	V_0)
	IL_0000:  ldarg.2 
	IL_0001:  call unsigned int16 class DeviceCommunicationLibrary.BaseFrame::ExtractCmdFromBytes(unsigned int8[])
	IL_0006:  stloc.0 
	IL_0007:  ldstr bytearray (
	5b 00 44 00 45 00 42 00 55 00 47 00 5d 00 20 00  // [.D.E.B.U.G.]. .
	36 65 30 52 70 65 6e 63 3a 00 20 00 43 00 4d 00  // 6e0Rpenc:. .C.M.
	44 00 3d 00 30 00 78 00 7b 00 30 00 3a 00 58 00  // D.=.0.x.{.0.:.X.
	34 00 7d 00 2c 00 20 00 7f 95 a6 5e 3d 00 7b 00  // 4.}.,. ....^=.{.
	31 00 7d 00 2c 00 20 00 70 65 6e 63 3d 00 7b 00  // 1.}.,. .penc=.{.
	32 00 7d 00 01 )                                 // 2.}..
	
	IL_000c:  ldloc.0 
	IL_000d:  box [mscorlib]System.UInt16
	IL_0012:  ldarg.2 
	IL_0013:  ldlen 
	IL_0014:  conv.i4 
	IL_0015:  box [mscorlib]System.Int32
	IL_001a:  ldarg.2 
	IL_001b:  call string class [mscorlib]System.BitConverter::ToString(unsigned int8[])
	IL_0020:  ldstr "-"
	IL_0025:  ldstr " "
	IL_002a:  callvirt instance string string::Replace(string, string)
	IL_002f:  call string string::Format(string, object, object, object)
	IL_0034:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0039:  ret 
    } // end of method <>c::<EnableDebugLogging>b__9_0

    // method line 185
    .method assembly hidebysig 
           instance default void '<EnableDebugLogging>b__9_1' (object s, string msg)  cil managed 
    {
        // Method begins at RVA 0x3fee
	// Code size 17 (0x11)
	.maxstack 8
	IL_0000:  ldstr bytearray (
	5b 00 44 00 45 00 42 00 55 00 47 00 5d 00 20 00  // [.D.E.B.U.G.]. .
	19 95 ef 8b 3a 00 20 00 01 )                     // ....:. ..
	
	IL_0005:  ldarg.2 
	IL_0006:  call string string::Concat(string, string)
	IL_000b:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0010:  ret 
    } // end of method <>c::<EnableDebugLogging>b__9_1

    // method line 186
    .method assembly hidebysig 
           instance default string '<SendFrame>b__33_0' (unsigned int8 b)  cil managed 
    {
        // Method begins at RVA 0x4000
	// Code size 17 (0x11)
	.maxstack 8
	IL_0000:  ldstr "0x{0:X2}"
	IL_0005:  ldarg.1 
	IL_0006:  box [mscorlib]System.Byte
	IL_000b:  call string string::Format(string, object)
	IL_0010:  ret 
    } // end of method <>c::<SendFrame>b__33_0

  } // end of class <>c

  .class nested private auto ansi sealed beforefieldinit '<>c__DisplayClass25_0'
  	extends [mscorlib]System.Object
  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  unsigned int8[] frameData
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'

    // method line 187
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x4012
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  ret 
    } // end of method <>c__DisplayClass25_0::.ctor

    // method line 188
    .method assembly hidebysig 
           instance default void '<ProcessReceiveBuffer>b__0' ()  cil managed 
    {
        // Method begins at RVA 0x401a
	// Code size 18 (0x12)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::'<>4__this'
	IL_0006:  ldarg.0 
	IL_0007:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass25_0'::frameData
	IL_000c:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::ProcessCompleteFrame(unsigned int8[])
	IL_0011:  ret 
    } // end of method <>c__DisplayClass25_0::<ProcessReceiveBuffer>b__0

  } // end of class <>c__DisplayClass25_0

  .class nested private auto ansi sealed beforefieldinit '<>c__DisplayClass37_0`1'<.ctor (class DeviceCommunicationLibrary.BaseFrame) T>
  	extends [mscorlib]System.Object
  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  bool responseReceived
    .field  public  class [mscorlib]System.Threading.CancellationTokenSource cts
    .field  public  unsigned int16 expectedCmd
    .field  public  class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> tcs
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  class [mscorlib]System.EventHandler`1<unsigned int8[]> 'handler'
    .field  public  class DeviceCommunicationLibrary.BaseFrame 'request'

    // method line 189
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x402d
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void object::'.ctor'()
	IL_0006:  ret 
    } // end of method <>c__DisplayClass37_0`1::.ctor

    // method line 190
    .method assembly hidebysig 
           instance default void '<SendRequestAsync>b__0' (object sender, unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x4038
	// Code size 415 (0x19f)
	.maxstack 5
	.locals init (
		unsigned int16	V_0,
		!T	V_1,
		bool	V_2,
		valuetype [mscorlib]System.Threading.CancellationToken	V_3,
		class [mscorlib]System.Exception	V_4)
	.try { // 0
	  IL_0000:  ldarg.0 
	  IL_0001:  ldfld bool class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::responseReceived
	  IL_0006:  brtrue.s IL_001d

	  IL_0008:  ldarg.0 
	  IL_0009:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	  IL_000e:  callvirt instance valuetype [mscorlib]System.Threading.CancellationToken class [mscorlib]System.Threading.CancellationTokenSource::get_Token()
	  IL_0013:  stloc.3 
	  IL_0014:  ldloca.s 3
	  IL_0016:  call instance bool valuetype [mscorlib]System.Threading.CancellationToken::get_IsCancellationRequested()
	  IL_001b:  brfalse.s IL_002c

	  IL_001d:  ldstr bytearray (
	cd 54 94 5e f2 5d 04 59 06 74 16 62 f2 5d d6 53  // .T.^.].Y.t.b.].S
	88 6d 0c ff fd 5f 65 75 64 6b cd 54 94 5e 01 )   // .m..._eudk.T.^.
	
	  IL_0022:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0027:  leave IL_019e

	  IL_002c:  ldstr bytearray (
	36 65 30 52 9f 53 cb 59 70 65 6e 63 3a 00 20 00  // 6e0R.S.Ypenc:. .
	7f 95 a6 5e 3d 00 7b 00 30 00 7d 00 2c 00 20 00  // ...^=.{.0.}.,. .
	85 51 b9 5b 3d 00 7b 00 31 00 7d 00 01 )         // .Q.[=.{.1.}..
	
	  IL_0031:  ldarg.2 
	  IL_0032:  ldlen 
	  IL_0033:  conv.i4 
	  IL_0034:  box [mscorlib]System.Int32
	  IL_0039:  ldarg.2 
	  IL_003a:  call string class [mscorlib]System.BitConverter::ToString(unsigned int8[])
	  IL_003f:  ldstr "-"
	  IL_0044:  ldstr " "
	  IL_0049:  callvirt instance string string::Replace(string, string)
	  IL_004e:  call string string::Format(string, object, object)
	  IL_0053:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0058:  ldarg.2 
	  IL_0059:  call unsigned int16 class DeviceCommunicationLibrary.BaseFrame::ExtractCmdFromBytes(unsigned int8[])
	  IL_005e:  stloc.0 
	  IL_005f:  ldstr bytearray (
	d0 63 d6 53 84 76 43 00 4d 00 44 00 3a 00 20 00  // .c.S.vC.M.D.:. .
	30 00 78 00 7b 00 30 00 3a 00 58 00 34 00 7d 00  // 0.x.{.0.:.X.4.}.
	01 )                                             // .
	
	  IL_0064:  ldloc.0 
	  IL_0065:  box [mscorlib]System.UInt16
	  IL_006a:  call string string::Format(string, object)
	  IL_006f:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0074:  call !!0 class [mscorlib]System.Activator::CreateInstance<!0> ()
	  IL_0079:  stloc.1 
	  IL_007a:  ldloc.1 
	  IL_007b:  box !0
	  IL_0080:  ldarg.2 
	  IL_0081:  callvirt instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	  IL_0086:  stloc.2 
	  IL_0087:  ldstr bytearray (
	e3 89 90 67 d3 7e 9c 67 3a 00 20 00 7b 00 30 00  // ...g.~.g:. .{.0.
	7d 00 2c 00 20 00 e3 89 90 67 0e 54 84 76 43 00  // }.,. ....g.T.vC.
	4d 00 44 00 3a 00 20 00 30 00 78 00 7b 00 31 00  // M.D.:. .0.x.{.1.
	3a 00 58 00 34 00 7d 00 01 )                     // :.X.4.}..
	
	  IL_008c:  ldloc.2 
	  IL_008d:  box [mscorlib]System.Boolean
	  IL_0092:  ldloc.1 
	  IL_0093:  box !0
	  IL_0098:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_009d:  box [mscorlib]System.UInt16
	  IL_00a2:  call string string::Format(string, object, object)
	  IL_00a7:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_00ac:  ldloc.2 
	  IL_00ad:  brfalse IL_016c

	  IL_00b2:  ldstr bytearray (
	36 65 30 52 cd 54 94 5e 3a 00 20 00 43 00 4d 00  // 6e0R.T.^:. .C.M.
	44 00 3d 00 30 00 78 00 7b 00 30 00 3a 00 58 00  // D.=.0.x.{.0.:.X.
	34 00 7d 00 2c 00 20 00 1f 67 1b 67 3a 00 20 00  // 4.}.,. ..g.g:. .
	30 00 78 00 7b 00 31 00 3a 00 58 00 34 00 7d 00  // 0.x.{.1.:.X.4.}.
	01 )                                             // .
	
	  IL_00b7:  ldloc.1 
	  IL_00b8:  box !0
	  IL_00bd:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_00c2:  box [mscorlib]System.UInt16
	  IL_00c7:  ldarg.0 
	  IL_00c8:  ldfld unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::expectedCmd
	  IL_00cd:  box [mscorlib]System.UInt16
	  IL_00d2:  call string string::Format(string, object, object)
	  IL_00d7:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_00dc:  ldloc.1 
	  IL_00dd:  box !0
	  IL_00e2:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_00e7:  ldarg.0 
	  IL_00e8:  ldfld unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::expectedCmd
	  IL_00ed:  bne.un.s IL_0140

	  IL_00ef:  ldarg.0 
	  IL_00f0:  ldc.i4.1 
	  IL_00f1:  stfld bool class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::responseReceived
	  IL_00f6:  ldarg.0 
	  IL_00f7:  ldfld class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::tcs
	  IL_00fc:  ldloc.1 
	  IL_00fd:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!T>::TrySetResult(!0)
	  IL_0102:  pop 
	  IL_0103:  ldarg.0 
	  IL_0104:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	  IL_0109:  callvirt instance void class [mscorlib]System.Threading.CancellationTokenSource::Cancel()
	  IL_010e:  ldarg.0 
	  IL_010f:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'<>4__this'
	  IL_0114:  ldarg.0 
	  IL_0115:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	  IL_011a:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	  IL_011f:  ldstr bytearray (
	cd 54 94 5e 39 53 4d 91 10 62 9f 52 3a 00 20 00  // .T.^9SM..b.R:. .
	43 00 4d 00 44 00 3d 00 30 00 78 00 7b 00 30 00  // C.M.D.=.0.x.{.0.
	3a 00 58 00 34 00 7d 00 01 )                     // :.X.4.}..
	
	  IL_0124:  ldloc.1 
	  IL_0125:  box !0
	  IL_012a:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_012f:  box [mscorlib]System.UInt16
	  IL_0134:  call string string::Format(string, object)
	  IL_0139:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_013e:  br.s IL_0176

	  IL_0140:  ldstr bytearray (
	cd 54 94 5e 43 00 4d 00 44 00 0d 4e 39 53 4d 91  // .T.^C.M.D..N9SM.
	3a 00 20 00 36 65 30 52 30 00 78 00 7b 00 30 00  // :. .6e0R0.x.{.0.
	3a 00 58 00 34 00 7d 00 2c 00 20 00 1f 67 1b 67  // :.X.4.}.,. ..g.g
	30 00 78 00 7b 00 31 00 3a 00 58 00 34 00 7d 00  // 0.x.{.1.:.X.4.}.
	01 )                                             // .
	
	  IL_0145:  ldloc.1 
	  IL_0146:  box !0
	  IL_014b:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_0150:  box [mscorlib]System.UInt16
	  IL_0155:  ldarg.0 
	  IL_0156:  ldfld unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::expectedCmd
	  IL_015b:  box [mscorlib]System.UInt16
	  IL_0160:  call string string::Format(string, object, object)
	  IL_0165:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_016a:  br.s IL_0176

	  IL_016c:  ldstr bytearray (
	e3 89 90 67 31 59 25 8d 01 )                     // ...g1Y%..
	
	  IL_0171:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0176:  leave.s IL_019e

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_0178:  stloc.s 4
	  IL_017a:  ldstr bytearray (
	04 59 06 74 cd 54 94 5e f6 65 d1 53 1f 75 02 5f  // .Y.t.T.^.e.S.u._
	38 5e 3a 00 20 00 01 )                           // 8^:. ..
	
	  IL_017f:  ldloc.s 4
	  IL_0181:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	  IL_0186:  ldstr bytearray (
	2c 00 20 00 06 58 08 68 3a 00 20 00 01 )         // ,. ..X.h:. ..
	
	  IL_018b:  ldloc.s 4
	  IL_018d:  callvirt instance string class [mscorlib]System.Exception::get_StackTrace()
	  IL_0192:  call string string::Concat(string, string, string, string)
	  IL_0197:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_019c:  leave.s IL_019e

	} // end handler 0
	IL_019e:  ret 
    } // end of method <>c__DisplayClass37_0`1::<SendRequestAsync>b__0

    // method line 191
    .method assembly hidebysig 
           instance default void '<SendRequestAsync>b__1' (class [mscorlib]System.Threading.Tasks.Task t)  cil managed 
    {
        // Method begins at RVA 0x4200
	// Code size 115 (0x73)
	.maxstack 2
	.locals init (
		!T	V_0)
	IL_0000:  ldarg.1 
	IL_0001:  callvirt instance bool class [mscorlib]System.Threading.Tasks.Task::get_IsCanceled()
	IL_0006:  brfalse.s IL_0013

	IL_0008:  ldstr bytearray (
	85 8d f6 65 fb 4e a1 52 f2 5d d6 53 88 6d 01 )   // ...e.N.R.].S.m.
	
	IL_000d:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0012:  ret 
	IL_0013:  ldarg.0 
	IL_0014:  ldfld bool class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::responseReceived
	IL_0019:  brtrue.s IL_0072

	IL_001b:  ldarg.0 
	IL_001c:  ldfld class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::tcs
	IL_0021:  callvirt instance class [mscorlib]System.Threading.Tasks.Task`1<!0> class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!T>::get_Task()
	IL_0026:  callvirt instance bool class [mscorlib]System.Threading.Tasks.Task::get_IsCompleted()
	IL_002b:  brtrue.s IL_0072

	IL_002d:  ldstr bytearray (
	f7 8b 42 6c 85 8d f6 65 20 00 28 00 43 00 4d 00  // ..Bl...e .(.C.M.
	44 00 3d 00 30 00 78 00 7b 00 30 00 3a 00 58 00  // D.=.0.x.{.0.:.X.
	34 00 7d 00 29 00 01 )                           // 4.}.)..
	
	IL_0032:  ldarg.0 
	IL_0033:  ldfld class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'request'
	IL_0038:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	IL_003d:  box [mscorlib]System.UInt16
	IL_0042:  call string string::Format(string, object)
	IL_0047:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_004c:  ldarg.0 
	IL_004d:  ldfld class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::tcs
	IL_0052:  ldloca.s 0
	IL_0054:  initobj !0
	IL_005a:  ldloc.0 
	IL_005b:  callvirt instance bool class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!T>::TrySetResult(!0)
	IL_0060:  pop 
	IL_0061:  ldarg.0 
	IL_0062:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'<>4__this'
	IL_0067:  ldarg.0 
	IL_0068:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	IL_006d:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	IL_0072:  ret 
    } // end of method <>c__DisplayClass37_0`1::<SendRequestAsync>b__1

  } // end of class <>c__DisplayClass37_0`1

  .class nested private auto ansi sealed beforefieldinit '<ChangeStatusAsync>d__43'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> '<>t__builder'
    .field  public  unsigned int8 status
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse> '<>u__1'

    // method line 192
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4280
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 182 (0xb6)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.ChangeStatusResponse	V_2,
		class DeviceCommunicationLibrary.ChangeStatusRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0061

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.ChangeStatusRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld unsigned int8 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::status
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.ChangeStatusRequest::set_Status(unsigned int8)
	  IL_0022:  stloc.3 
	  IL_0023:  ldloc.1 
	  IL_0024:  ldloc.3 
	  IL_0025:  ldarg.0 
	  IL_0026:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::timeoutMs
	  IL_002b:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.ChangeStatusResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0030:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::GetAwaiter()
	  IL_0035:  stloc.s 4
	  IL_0037:  ldloca.s 4
	  IL_0039:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::get_IsCompleted()
	  IL_003e:  brtrue.s IL_007e

	  IL_0040:  ldarg.0 
	  IL_0041:  ldc.i4.0 
	  IL_0042:  dup 
	  IL_0043:  stloc.0 
	  IL_0044:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	  IL_0049:  ldarg.0 
	  IL_004a:  ldloc.s 4
	  IL_004c:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>u__1'
	  IL_0051:  ldarg.0 
	  IL_0052:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	  IL_0057:  ldloca.s 4
	  IL_0059:  ldarg.0 
	  IL_005a:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'> ([out] !!0&, [out] !!1&)
	  IL_005f:  leave.s IL_00b5

	  IL_0061:  ldarg.0 
	  IL_0062:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>u__1'
	  IL_0067:  stloc.s 4
	  IL_0069:  ldarg.0 
	  IL_006a:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>u__1'
	  IL_006f:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse>
	  IL_0075:  ldarg.0 
	  IL_0076:  ldc.i4.m1 
	  IL_0077:  dup 
	  IL_0078:  stloc.0 
	  IL_0079:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	  IL_007e:  ldloca.s 4
	  IL_0080:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::GetResult()
	  IL_0085:  stloc.2 
	  IL_0086:  leave.s IL_00a1

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_0088:  stloc.s 5
	  IL_008a:  ldarg.0 
	  IL_008b:  ldc.i4.s 0xfffffffe
	  IL_008d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	  IL_0092:  ldarg.0 
	  IL_0093:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	  IL_0098:  ldloc.s 5
	  IL_009a:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::SetException(class [mscorlib]System.Exception)
	  IL_009f:  leave.s IL_00b5

	} // end handler 0
	IL_00a1:  ldarg.0 
	IL_00a2:  ldc.i4.s 0xfffffffe
	IL_00a4:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>1__state'
	IL_00a9:  ldarg.0 
	IL_00aa:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	IL_00af:  ldloc.2 
	IL_00b0:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::SetResult(!0)
	IL_00b5:  ret 
    } // end of method <ChangeStatusAsync>d__43::MoveNext

    // method line 193
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4354
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ChangeStatusAsync>d__43'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.ChangeStatusResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <ChangeStatusAsync>d__43::SetStateMachine

  } // end of class <ChangeStatusAsync>d__43

  .class nested private auto ansi sealed beforefieldinit '<ConnectDeviceAsync>d__47'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> '<>u__1'

    // method line 194
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4364
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.GetFlashInfoResponse	V_2,
		class DeviceCommunicationLibrary.ConnectDeviceRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.ConnectDeviceRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.GetFlashInfoResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <ConnectDeviceAsync>d__47::MoveNext

    // method line 195
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x442c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<ConnectDeviceAsync>d__47'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <ConnectDeviceAsync>d__47::SetStateMachine

  } // end of class <ConnectDeviceAsync>d__47

  .class nested private auto ansi sealed beforefieldinit '<DownloadCompleteAsync>d__20'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> '<>u__1'

    // method line 196
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x443c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.DownloadCompleteResponse	V_2,
		class DeviceCommunicationLibrary.DownloadCompleteRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.DownloadCompleteRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.DownloadCompleteResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <DownloadCompleteAsync>d__20::MoveNext

    // method line 197
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4504
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadCompleteAsync>d__20'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadCompleteResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <DownloadCompleteAsync>d__20::SetStateMachine

  } // end of class <DownloadCompleteAsync>d__20

  .class nested private auto ansi sealed beforefieldinit '<DownloadDataAsync>d__19'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> '<>t__builder'
    .field  public  unsigned int32 offset
    .field  public  unsigned int8[] data
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse> '<>u__1'

    // method line 198
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4514
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 194 (0xc2)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.DownloadDataResponse	V_2,
		class DeviceCommunicationLibrary.DownloadDataRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_006d

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.DownloadDataRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::offset
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.DownloadDataRequest::set_Offset(unsigned int32)
	  IL_0022:  dup 
	  IL_0023:  ldarg.0 
	  IL_0024:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::data
	  IL_0029:  callvirt instance void class DeviceCommunicationLibrary.DownloadDataRequest::set_Data(unsigned int8[])
	  IL_002e:  stloc.3 
	  IL_002f:  ldloc.1 
	  IL_0030:  ldloc.3 
	  IL_0031:  ldarg.0 
	  IL_0032:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::timeoutMs
	  IL_0037:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.DownloadDataResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_003c:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.DownloadDataResponse>::GetAwaiter()
	  IL_0041:  stloc.s 4
	  IL_0043:  ldloca.s 4
	  IL_0045:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse>::get_IsCompleted()
	  IL_004a:  brtrue.s IL_008a

	  IL_004c:  ldarg.0 
	  IL_004d:  ldc.i4.0 
	  IL_004e:  dup 
	  IL_004f:  stloc.0 
	  IL_0050:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	  IL_0055:  ldarg.0 
	  IL_0056:  ldloc.s 4
	  IL_0058:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>u__1'
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	  IL_0063:  ldloca.s 4
	  IL_0065:  ldarg.0 
	  IL_0066:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'> ([out] !!0&, [out] !!1&)
	  IL_006b:  leave.s IL_00c1

	  IL_006d:  ldarg.0 
	  IL_006e:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>u__1'
	  IL_0073:  stloc.s 4
	  IL_0075:  ldarg.0 
	  IL_0076:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>u__1'
	  IL_007b:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse>
	  IL_0081:  ldarg.0 
	  IL_0082:  ldc.i4.m1 
	  IL_0083:  dup 
	  IL_0084:  stloc.0 
	  IL_0085:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	  IL_008a:  ldloca.s 4
	  IL_008c:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.DownloadDataResponse>::GetResult()
	  IL_0091:  stloc.2 
	  IL_0092:  leave.s IL_00ad

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_0094:  stloc.s 5
	  IL_0096:  ldarg.0 
	  IL_0097:  ldc.i4.s 0xfffffffe
	  IL_0099:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	  IL_009e:  ldarg.0 
	  IL_009f:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	  IL_00a4:  ldloc.s 5
	  IL_00a6:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00ab:  leave.s IL_00c1

	} // end handler 0
	IL_00ad:  ldarg.0 
	IL_00ae:  ldc.i4.s 0xfffffffe
	IL_00b0:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>1__state'
	IL_00b5:  ldarg.0 
	IL_00b6:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	IL_00bb:  ldloc.2 
	IL_00bc:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::SetResult(!0)
	IL_00c1:  ret 
    } // end of method <DownloadDataAsync>d__19::MoveNext

    // method line 199
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x45f4
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<DownloadDataAsync>d__19'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.DownloadDataResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <DownloadDataAsync>d__19::SetStateMachine

  } // end of class <DownloadDataAsync>d__19

  .class nested private auto ansi sealed beforefieldinit '<ExitRunningAsync>d__48'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool> '<>u__1'

    // method line 200
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4604
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 4
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		bool	V_2,
		class DeviceCommunicationLibrary.ExitRunningRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.ExitRunningRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldc.i4.3 
	  IL_001a:  ldc.i4 1000
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<bool> class DeviceCommunicationLibrary.DeviceCommunicator::SendFrameWithRetryAsync(class DeviceCommunicationLibrary.BaseFrame, int32, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<bool>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<bool>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <ExitRunningAsync>d__48::MoveNext

    // method line 201
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x46cc
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<ExitRunningAsync>d__48'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <ExitRunningAsync>d__48::SetStateMachine

  } // end of class <ExitRunningAsync>d__48

  .class nested private auto ansi sealed beforefieldinit '<GetDownloadStatusAsync>d__17'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> '<>u__1'

    // method line 202
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x46dc
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.GetDownloadStatusResponse	V_2,
		class DeviceCommunicationLibrary.GetDownloadStatusRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.GetDownloadStatusRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.GetDownloadStatusResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <GetDownloadStatusAsync>d__17::MoveNext

    // method line 203
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x47a4
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetDownloadStatusAsync>d__17'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetDownloadStatusResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <GetDownloadStatusAsync>d__17::SetStateMachine

  } // end of class <GetDownloadStatusAsync>d__17

  .class nested private auto ansi sealed beforefieldinit '<GetFlashInfoAsync>d__46'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> '<>u__1'

    // method line 204
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x47b4
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.GetFlashInfoResponse	V_2,
		class DeviceCommunicationLibrary.GetFlashInfoRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.GetFlashInfoRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.GetFlashInfoResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <GetFlashInfoAsync>d__46::MoveNext

    // method line 205
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x487c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetFlashInfoAsync>d__46'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetFlashInfoResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <GetFlashInfoAsync>d__46::SetStateMachine

  } // end of class <GetFlashInfoAsync>d__46

  .class nested private auto ansi sealed beforefieldinit '<GetGifInfoAsync>d__45'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse> '<>u__1'

    // method line 206
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x488c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.GetGifInfoResponse	V_2,
		class DeviceCommunicationLibrary.GetGifInfoRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.GetGifInfoRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.GetGifInfoResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <GetGifInfoAsync>d__45::MoveNext

    // method line 207
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4954
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetGifInfoAsync>d__45'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetGifInfoResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <GetGifInfoAsync>d__45::SetStateMachine

  } // end of class <GetGifInfoAsync>d__45

  .class nested private auto ansi sealed beforefieldinit '<GetHardwareInfoAsync>d__35'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> '<>u__1'

    // method line 208
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4964
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 220 (0xdc)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.GetHardwareInfoResponse	V_2,
		class DeviceCommunicationLibrary.GetHardwareInfoRequest	V_3,
		class DeviceCommunicationLibrary.GetHardwareInfoResponse	V_4,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>	V_5,
		class [mscorlib]System.Exception	V_6)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_005f

	  IL_0011:  ldstr bytearray (
	3d 00 3d 00 3d 00 20 00 00 5f cb 59 b7 83 d6 53  // =.=.=. .._.Y...S
	6c 78 f6 4e e1 4f 6f 60 20 00 3d 00 3d 00 3d 00  // lx.N.Oo` .=.=.=.
	01 )                                             // .
	
	  IL_0016:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_001b:  newobj instance void class DeviceCommunicationLibrary.GetHardwareInfoRequest::'.ctor'()
	  IL_0020:  stloc.3 
	  IL_0021:  ldloc.1 
	  IL_0022:  ldloc.3 
	  IL_0023:  ldarg.0 
	  IL_0024:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::timeoutMs
	  IL_0029:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.GetHardwareInfoResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_002e:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::GetAwaiter()
	  IL_0033:  stloc.s 5
	  IL_0035:  ldloca.s 5
	  IL_0037:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::get_IsCompleted()
	  IL_003c:  brtrue.s IL_007c

	  IL_003e:  ldarg.0 
	  IL_003f:  ldc.i4.0 
	  IL_0040:  dup 
	  IL_0041:  stloc.0 
	  IL_0042:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	  IL_0047:  ldarg.0 
	  IL_0048:  ldloc.s 5
	  IL_004a:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>u__1'
	  IL_004f:  ldarg.0 
	  IL_0050:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	  IL_0055:  ldloca.s 5
	  IL_0057:  ldarg.0 
	  IL_0058:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'> ([out] !!0&, [out] !!1&)
	  IL_005d:  leave.s IL_00db

	  IL_005f:  ldarg.0 
	  IL_0060:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>u__1'
	  IL_0065:  stloc.s 5
	  IL_0067:  ldarg.0 
	  IL_0068:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>u__1'
	  IL_006d:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>
	  IL_0073:  ldarg.0 
	  IL_0074:  ldc.i4.m1 
	  IL_0075:  dup 
	  IL_0076:  stloc.0 
	  IL_0077:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	  IL_007c:  ldloca.s 5
	  IL_007e:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::GetResult()
	  IL_0083:  stloc.s 4
	  IL_0085:  ldstr bytearray (
	3d 00 3d 00 3d 00 20 00 b7 83 d6 53 6c 78 f6 4e  // =.=.=. ....Slx.N
	e1 4f 6f 60 d3 7e 5f 67 0c ff d3 7e 9c 67 3a 00  // .Oo`.~_g...~.g:.
	20 00 01 )                                       //  ..
	
	  IL_008a:  ldloc.s 4
	  IL_008c:  brfalse.s IL_0095

	  IL_008e:  ldstr bytearray (
	10 62 9f 52 01 )                                 // .b.R.
	
	  IL_0093:  br.s IL_009a

	  IL_0095:  ldstr "null"
	  IL_009a:  ldstr " ==="
	  IL_009f:  call string string::Concat(string, string, string)
	  IL_00a4:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_00a9:  ldloc.s 4
	  IL_00ab:  stloc.2 
	  IL_00ac:  leave.s IL_00c7

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_00ae:  stloc.s 6
	  IL_00b0:  ldarg.0 
	  IL_00b1:  ldc.i4.s 0xfffffffe
	  IL_00b3:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	  IL_00b8:  ldarg.0 
	  IL_00b9:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	  IL_00be:  ldloc.s 6
	  IL_00c0:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00c5:  leave.s IL_00db

	} // end handler 0
	IL_00c7:  ldarg.0 
	IL_00c8:  ldc.i4.s 0xfffffffe
	IL_00ca:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>1__state'
	IL_00cf:  ldarg.0 
	IL_00d0:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	IL_00d5:  ldloc.2 
	IL_00d6:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::SetResult(!0)
	IL_00db:  ret 
    } // end of method <GetHardwareInfoAsync>d__35::MoveNext

    // method line 209
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4a5c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<GetHardwareInfoAsync>d__35'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.GetHardwareInfoResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <GetHardwareInfoAsync>d__35::SetStateMachine

  } // end of class <GetHardwareInfoAsync>d__35

  .class nested private auto ansi sealed beforefieldinit '<HandshakeAsync>d__34'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse> '<>u__1'

    // method line 210
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4a6c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.HandshakeResponse	V_2,
		class DeviceCommunicationLibrary.HandshakeRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.HandshakeRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.HandshakeResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.HandshakeResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.HandshakeResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <HandshakeAsync>d__34::MoveNext

    // method line 211
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4b34
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<HandshakeAsync>d__34'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.HandshakeResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <HandshakeAsync>d__34::SetStateMachine

  } // end of class <HandshakeAsync>d__34

  .class nested private auto ansi sealed beforefieldinit '<RequestDownloadAsync>d__18'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> '<>t__builder'
    .field  public  unsigned int32 address
    .field  public  unsigned int32 fileSize
    .field  public  unsigned int8[] fileId
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse> '<>u__1'

    // method line 212
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4b44
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 206 (0xce)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.RequestDownloadResponse	V_2,
		class DeviceCommunicationLibrary.RequestDownloadRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0079

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.RequestDownloadRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::address
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.RequestDownloadRequest::set_Addr(unsigned int32)
	  IL_0022:  dup 
	  IL_0023:  ldarg.0 
	  IL_0024:  ldfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::fileSize
	  IL_0029:  callvirt instance void class DeviceCommunicationLibrary.RequestDownloadRequest::set_FileSize(unsigned int32)
	  IL_002e:  dup 
	  IL_002f:  ldarg.0 
	  IL_0030:  ldfld unsigned int8[] DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::fileId
	  IL_0035:  callvirt instance void class DeviceCommunicationLibrary.RequestDownloadRequest::set_FileId(unsigned int8[])
	  IL_003a:  stloc.3 
	  IL_003b:  ldloc.1 
	  IL_003c:  ldloc.3 
	  IL_003d:  ldarg.0 
	  IL_003e:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::timeoutMs
	  IL_0043:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.RequestDownloadResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0048:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::GetAwaiter()
	  IL_004d:  stloc.s 4
	  IL_004f:  ldloca.s 4
	  IL_0051:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::get_IsCompleted()
	  IL_0056:  brtrue.s IL_0096

	  IL_0058:  ldarg.0 
	  IL_0059:  ldc.i4.0 
	  IL_005a:  dup 
	  IL_005b:  stloc.0 
	  IL_005c:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	  IL_0061:  ldarg.0 
	  IL_0062:  ldloc.s 4
	  IL_0064:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>u__1'
	  IL_0069:  ldarg.0 
	  IL_006a:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	  IL_006f:  ldloca.s 4
	  IL_0071:  ldarg.0 
	  IL_0072:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'> ([out] !!0&, [out] !!1&)
	  IL_0077:  leave.s IL_00cd

	  IL_0079:  ldarg.0 
	  IL_007a:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>u__1'
	  IL_007f:  stloc.s 4
	  IL_0081:  ldarg.0 
	  IL_0082:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>u__1'
	  IL_0087:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse>
	  IL_008d:  ldarg.0 
	  IL_008e:  ldc.i4.m1 
	  IL_008f:  dup 
	  IL_0090:  stloc.0 
	  IL_0091:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	  IL_0096:  ldloca.s 4
	  IL_0098:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::GetResult()
	  IL_009d:  stloc.2 
	  IL_009e:  leave.s IL_00b9

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_00a0:  stloc.s 5
	  IL_00a2:  ldarg.0 
	  IL_00a3:  ldc.i4.s 0xfffffffe
	  IL_00a5:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	  IL_00aa:  ldarg.0 
	  IL_00ab:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	  IL_00b0:  ldloc.s 5
	  IL_00b2:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00b7:  leave.s IL_00cd

	} // end handler 0
	IL_00b9:  ldarg.0 
	IL_00ba:  ldc.i4.s 0xfffffffe
	IL_00bc:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>1__state'
	IL_00c1:  ldarg.0 
	IL_00c2:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	IL_00c7:  ldloc.2 
	IL_00c8:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::SetResult(!0)
	IL_00cd:  ret 
    } // end of method <RequestDownloadAsync>d__18::MoveNext

    // method line 213
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4c30
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RequestDownloadAsync>d__18'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RequestDownloadResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <RequestDownloadAsync>d__18::SetStateMachine

  } // end of class <RequestDownloadAsync>d__18

  .class nested private auto ansi sealed beforefieldinit '<RestartAsync>d__44'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse> '<>u__1'

    // method line 214
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4c40
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 170 (0xaa)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.RestartResponse	V_2,
		class DeviceCommunicationLibrary.RestartRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0055

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.RestartRequest::'.ctor'()
	  IL_0016:  stloc.3 
	  IL_0017:  ldloc.1 
	  IL_0018:  ldloc.3 
	  IL_0019:  ldarg.0 
	  IL_001a:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::timeoutMs
	  IL_001f:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.RestartResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0024:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.RestartResponse>::GetAwaiter()
	  IL_0029:  stloc.s 4
	  IL_002b:  ldloca.s 4
	  IL_002d:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse>::get_IsCompleted()
	  IL_0032:  brtrue.s IL_0072

	  IL_0034:  ldarg.0 
	  IL_0035:  ldc.i4.0 
	  IL_0036:  dup 
	  IL_0037:  stloc.0 
	  IL_0038:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloc.s 4
	  IL_0040:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>u__1'
	  IL_0045:  ldarg.0 
	  IL_0046:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	  IL_004b:  ldloca.s 4
	  IL_004d:  ldarg.0 
	  IL_004e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'> ([out] !!0&, [out] !!1&)
	  IL_0053:  leave.s IL_00a9

	  IL_0055:  ldarg.0 
	  IL_0056:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>u__1'
	  IL_005b:  stloc.s 4
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>u__1'
	  IL_0063:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse>
	  IL_0069:  ldarg.0 
	  IL_006a:  ldc.i4.m1 
	  IL_006b:  dup 
	  IL_006c:  stloc.0 
	  IL_006d:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	  IL_0072:  ldloca.s 4
	  IL_0074:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.RestartResponse>::GetResult()
	  IL_0079:  stloc.2 
	  IL_007a:  leave.s IL_0095

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_007c:  stloc.s 5
	  IL_007e:  ldarg.0 
	  IL_007f:  ldc.i4.s 0xfffffffe
	  IL_0081:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	  IL_008c:  ldloc.s 5
	  IL_008e:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::SetException(class [mscorlib]System.Exception)
	  IL_0093:  leave.s IL_00a9

	} // end handler 0
	IL_0095:  ldarg.0 
	IL_0096:  ldc.i4.s 0xfffffffe
	IL_0098:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>1__state'
	IL_009d:  ldarg.0 
	IL_009e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	IL_00a3:  ldloc.2 
	IL_00a4:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::SetResult(!0)
	IL_00a9:  ret 
    } // end of method <RestartAsync>d__44::MoveNext

    // method line 215
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4d08
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<RestartAsync>d__44'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.RestartResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <RestartAsync>d__44::SetStateMachine

  } // end of class <RestartAsync>d__44

  .class nested private auto ansi sealed beforefieldinit '<SendFrameWithRetryAsync>d__36'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  class DeviceCommunicationLibrary.BaseFrame frame
    .field  public  int32 maxRetries
    .field  public  int32 intervalMs
    .field  private  int32 '<i>5__2'
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter '<>u__1'

    // method line 216
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4d18
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 244 (0xf4)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		bool	V_2,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter	V_3,
		int32	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_007c

	  IL_0011:  ldarg.0 
	  IL_0012:  ldc.i4.0 
	  IL_0013:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<i>5__2'
	  IL_0018:  br IL_00b1

	  IL_001d:  ldloc.1 
	  IL_001e:  ldarg.0 
	  IL_001f:  ldfld class DeviceCommunicationLibrary.BaseFrame DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::frame
	  IL_0024:  call instance bool class DeviceCommunicationLibrary.DeviceCommunicator::SendFrame(class DeviceCommunicationLibrary.BaseFrame)
	  IL_0029:  brfalse.s IL_0032

	  IL_002b:  ldc.i4.1 
	  IL_002c:  stloc.2 
	  IL_002d:  leave IL_00df

	  IL_0032:  ldarg.0 
	  IL_0033:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<i>5__2'
	  IL_0038:  ldarg.0 
	  IL_0039:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::maxRetries
	  IL_003e:  ldc.i4.1 
	  IL_003f:  sub 
	  IL_0040:  bge.s IL_009f

	  IL_0042:  ldarg.0 
	  IL_0043:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::intervalMs
	  IL_0048:  call class [mscorlib]System.Threading.Tasks.Task class [mscorlib]System.Threading.Tasks.Task::Delay(int32)
	  IL_004d:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter class [mscorlib]System.Threading.Tasks.Task::GetAwaiter()
	  IL_0052:  stloc.3 
	  IL_0053:  ldloca.s 3
	  IL_0055:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter::get_IsCompleted()
	  IL_005a:  brtrue.s IL_0098

	  IL_005c:  ldarg.0 
	  IL_005d:  ldc.i4.0 
	  IL_005e:  dup 
	  IL_005f:  stloc.0 
	  IL_0060:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	  IL_0065:  ldarg.0 
	  IL_0066:  ldloc.3 
	  IL_0067:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>u__1'
	  IL_006c:  ldarg.0 
	  IL_006d:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	  IL_0072:  ldloca.s 3
	  IL_0074:  ldarg.0 
	  IL_0075:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'> ([out] !!0&, [out] !!1&)
	  IL_007a:  leave.s IL_00f3

	  IL_007c:  ldarg.0 
	  IL_007d:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>u__1'
	  IL_0082:  stloc.3 
	  IL_0083:  ldarg.0 
	  IL_0084:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>u__1'
	  IL_0089:  initobj [mscorlib]System.Runtime.CompilerServices.TaskAwaiter
	  IL_008f:  ldarg.0 
	  IL_0090:  ldc.i4.m1 
	  IL_0091:  dup 
	  IL_0092:  stloc.0 
	  IL_0093:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	  IL_0098:  ldloca.s 3
	  IL_009a:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter::GetResult()
	  IL_009f:  ldarg.0 
	  IL_00a0:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<i>5__2'
	  IL_00a5:  stloc.s 4
	  IL_00a7:  ldarg.0 
	  IL_00a8:  ldloc.s 4
	  IL_00aa:  ldc.i4.1 
	  IL_00ab:  add 
	  IL_00ac:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<i>5__2'
	  IL_00b1:  ldarg.0 
	  IL_00b2:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<i>5__2'
	  IL_00b7:  ldarg.0 
	  IL_00b8:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::maxRetries
	  IL_00bd:  blt IL_001d

	  IL_00c2:  ldc.i4.0 
	  IL_00c3:  stloc.2 
	  IL_00c4:  leave.s IL_00df

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_00c6:  stloc.s 5
	  IL_00c8:  ldarg.0 
	  IL_00c9:  ldc.i4.s 0xfffffffe
	  IL_00cb:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	  IL_00d0:  ldarg.0 
	  IL_00d1:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	  IL_00d6:  ldloc.s 5
	  IL_00d8:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetException(class [mscorlib]System.Exception)
	  IL_00dd:  leave.s IL_00f3

	} // end handler 0
	IL_00df:  ldarg.0 
	IL_00e0:  ldc.i4.s 0xfffffffe
	IL_00e2:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>1__state'
	IL_00e7:  ldarg.0 
	IL_00e8:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	IL_00ed:  ldloc.2 
	IL_00ee:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetResult(!0)
	IL_00f3:  ret 
    } // end of method <SendFrameWithRetryAsync>d__36::MoveNext

    // method line 217
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x4e28
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool> DeviceCommunicationLibrary.DeviceCommunicator/'<SendFrameWithRetryAsync>d__36'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<bool>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <SendFrameWithRetryAsync>d__36::SetStateMachine

  } // end of class <SendFrameWithRetryAsync>d__36

  .class nested private auto ansi sealed beforefieldinit '<SendRequestAsync>d__37`1'<.ctor (class DeviceCommunicationLibrary.BaseFrame) T>
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> '<>t__builder'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  class DeviceCommunicationLibrary.BaseFrame 'request'
    .field  public  int32 timeoutMs
    .field  private  class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> '<>8__1'
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> '<>u__1'

    // method line 218
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x4e38
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 787 (0x313)
	.maxstack 4
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		!T	V_2,
		!T	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!T>	V_4,
		class [mscorlib]System.Exception	V_5,
		class [mscorlib]System.Exception	V_6)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 1
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse IL_01a7

	  IL_0014:  ldarg.0 
	  IL_0015:  newobj instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!T>::'.ctor'()
	  IL_001a:  stfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_001f:  ldarg.0 
	  IL_0020:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0025:  ldarg.0 
	  IL_0026:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>4__this'
	  IL_002b:  stfld class DeviceCommunicationLibrary.DeviceCommunicator class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'<>4__this'
	  IL_0030:  ldarg.0 
	  IL_0031:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0036:  ldarg.0 
	  IL_0037:  ldfld class DeviceCommunicationLibrary.BaseFrame valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'request'
	  IL_003c:  stfld class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'request'
	  IL_0041:  ldstr bytearray (
	3d 00 3d 00 3d 00 20 00 53 00 65 00 6e 00 64 00  // =.=.=. .S.e.n.d.
	52 00 65 00 71 00 75 00 65 00 73 00 74 00 41 00  // R.e.q.u.e.s.t.A.
	73 00 79 00 6e 00 63 00 00 5f cb 59 3a 00 20 00  // s.y.n.c.._.Y:. .
	43 00 4d 00 44 00 3d 00 30 00 78 00 7b 00 30 00  // C.M.D.=.0.x.{.0.
	3a 00 58 00 34 00 7d 00 2c 00 20 00 85 8d f6 65  // :.X.4.}.,. ....e
	3a 00 20 00 7b 00 31 00 7d 00 6d 00 73 00 20 00  // :. .{.1.}.m.s. .
	3d 00 3d 00 3d 00 01 )                           // =.=.=..
	
	  IL_0046:  ldarg.0 
	  IL_0047:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_004c:  ldfld class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'request'
	  IL_0051:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_0056:  box [mscorlib]System.UInt16
	  IL_005b:  ldarg.0 
	  IL_005c:  ldfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::timeoutMs
	  IL_0061:  box [mscorlib]System.Int32
	  IL_0066:  call string string::Format(string, object, object)
	  IL_006b:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_0070:  ldarg.0 
	  IL_0071:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0076:  newobj instance void class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!T>::'.ctor'()
	  IL_007b:  stfld class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::tcs
	  IL_0080:  ldarg.0 
	  IL_0081:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0086:  ldarg.0 
	  IL_0087:  ldfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::timeoutMs
	  IL_008c:  newobj instance void class [mscorlib]System.Threading.CancellationTokenSource::'.ctor'(int32)
	  IL_0091:  stfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	  IL_0096:  ldarg.0 
	  IL_0097:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_009c:  ldloc.1 
	  IL_009d:  ldarg.0 
	  IL_009e:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00a3:  ldfld class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'request'
	  IL_00a8:  callvirt instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::get_CMD()
	  IL_00ad:  call instance unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator::GetExpectedResponseCmd(unsigned int16)
	  IL_00b2:  stfld unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::expectedCmd
	  IL_00b7:  ldstr bytearray (
	1f 67 1b 67 cd 54 94 5e 7d 54 e4 4e 3a 00 20 00  // .g.g.T.^}T.N:. .
	30 00 78 00 7b 00 30 00 3a 00 58 00 34 00 7d 00  // 0.x.{.0.:.X.4.}.
	01 )                                             // .
	
	  IL_00bc:  ldarg.0 
	  IL_00bd:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00c2:  ldfld unsigned int16 class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::expectedCmd
	  IL_00c7:  box [mscorlib]System.UInt16
	  IL_00cc:  call string string::Format(string, object)
	  IL_00d1:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_00d6:  ldarg.0 
	  IL_00d7:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00dc:  ldnull 
	  IL_00dd:  stfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	  IL_00e2:  ldarg.0 
	  IL_00e3:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00e8:  ldc.i4.0 
	  IL_00e9:  stfld bool class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::responseReceived
	  IL_00ee:  ldarg.0 
	  IL_00ef:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00f4:  ldarg.0 
	  IL_00f5:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_00fa:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!T>::'<SendRequestAsync>b__0'(object, unsigned int8[])
	  IL_0100:  newobj instance void class [mscorlib]System.EventHandler`1<unsigned int8[]>::'.ctor'(object, native int)
	  IL_0105:  stfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	  IL_010a:  ldloc.1 
	  IL_010b:  ldarg.0 
	  IL_010c:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0111:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	  IL_0116:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::add_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	  IL_011b:  ldarg.0 
	  IL_011c:  ldfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::timeoutMs
	  IL_0121:  ldarg.0 
	  IL_0122:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0127:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	  IL_012c:  callvirt instance valuetype [mscorlib]System.Threading.CancellationToken class [mscorlib]System.Threading.CancellationTokenSource::get_Token()
	  IL_0131:  call class [mscorlib]System.Threading.Tasks.Task class [mscorlib]System.Threading.Tasks.Task::Delay(int32, valuetype [mscorlib]System.Threading.CancellationToken)
	  IL_0136:  ldarg.0 
	  IL_0137:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_013c:  ldftn instance void class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!T>::'<SendRequestAsync>b__1'(class [mscorlib]System.Threading.Tasks.Task)
	  IL_0142:  newobj instance void class [mscorlib]System.Action`1<class [mscorlib]System.Threading.Tasks.Task>::'.ctor'(object, native int)
	  IL_0147:  call class [mscorlib]System.Threading.Tasks.TaskScheduler class [mscorlib]System.Threading.Tasks.TaskScheduler::get_Default()
	  IL_014c:  callvirt instance class [mscorlib]System.Threading.Tasks.Task class [mscorlib]System.Threading.Tasks.Task::ContinueWith(class [mscorlib]System.Action`1<class [mscorlib]System.Threading.Tasks.Task>, class [mscorlib]System.Threading.Tasks.TaskScheduler)
	  IL_0151:  pop 
	  IL_0152:  ldloc.1 
	  IL_0153:  ldarg.0 
	  IL_0154:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0159:  ldfld class DeviceCommunicationLibrary.BaseFrame class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'request'
	  IL_015e:  call instance bool class DeviceCommunicationLibrary.DeviceCommunicator::SendFrame(class DeviceCommunicationLibrary.BaseFrame)
	  IL_0163:  brtrue.s IL_019d

	  IL_0165:  ldstr bytearray (
	d1 53 01 90 f7 8b 42 6c 31 59 25 8d 01 )         // .S....Bl1Y%..
	
	  IL_016a:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_016f:  ldloc.1 
	  IL_0170:  ldarg.0 
	  IL_0171:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0176:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	  IL_017b:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	  IL_0180:  ldarg.0 
	  IL_0181:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_0186:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	  IL_018b:  callvirt instance void class [mscorlib]System.Threading.CancellationTokenSource::Cancel()
	  IL_0190:  ldloca.s 2
	  IL_0192:  initobj !0
	  IL_0198:  leave IL_02f7

	  IL_019d:  ldstr bytearray (
	f2 5d d1 53 01 90 f7 8b 42 6c 0c ff 49 7b 85 5f  // .].S....Bl..I{._
	cd 54 94 5e 2e 00 2e 00 2e 00 01 )               // .T.^.......
	
	  IL_01a2:  call void class [mscorlib]System.Console::WriteLine(string)
	  IL_01a7:  nop 
	  .try { // 0
	    IL_01a8:  ldloc.0 
	    IL_01a9:  brfalse.s IL_01ef

	    IL_01ab:  ldarg.0 
	    IL_01ac:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_01b1:  ldfld class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!0> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::tcs
	    IL_01b6:  callvirt instance class [mscorlib]System.Threading.Tasks.Task`1<!0> class [mscorlib]System.Threading.Tasks.TaskCompletionSource`1<!T>::get_Task()
	    IL_01bb:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<!T>::GetAwaiter()
	    IL_01c0:  stloc.s 4
	    IL_01c2:  ldloca.s 4
	    IL_01c4:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!T>::get_IsCompleted()
	    IL_01c9:  brtrue.s IL_020c

	    IL_01cb:  ldarg.0 
	    IL_01cc:  ldc.i4.0 
	    IL_01cd:  dup 
	    IL_01ce:  stloc.0 
	    IL_01cf:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>1__state'
	    IL_01d4:  ldarg.0 
	    IL_01d5:  ldloc.s 4
	    IL_01d7:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>u__1'
	    IL_01dc:  ldarg.0 
	    IL_01dd:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>t__builder'
	    IL_01e2:  ldloca.s 4
	    IL_01e4:  ldarg.0 
	    IL_01e5:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!T>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>> ([out] !!0&, [out] !!1&)
	    IL_01ea:  leave IL_0312

	    IL_01ef:  ldarg.0 
	    IL_01f0:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>u__1'
	    IL_01f5:  stloc.s 4
	    IL_01f7:  ldarg.0 
	    IL_01f8:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>u__1'
	    IL_01fd:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0>
	    IL_0203:  ldarg.0 
	    IL_0204:  ldc.i4.m1 
	    IL_0205:  dup 
	    IL_0206:  stloc.0 
	    IL_0207:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>1__state'
	    IL_020c:  ldloca.s 4
	    IL_020e:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!T>::GetResult()
	    IL_0213:  stloc.3 
	    IL_0214:  ldarg.0 
	    IL_0215:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_021a:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	    IL_021f:  callvirt instance bool class [mscorlib]System.Threading.CancellationTokenSource::get_IsCancellationRequested()
	    IL_0224:  brtrue.s IL_0236

	    IL_0226:  ldarg.0 
	    IL_0227:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_022c:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	    IL_0231:  callvirt instance void class [mscorlib]System.Threading.CancellationTokenSource::Cancel()
	    IL_0236:  ldloc.1 
	    IL_0237:  ldarg.0 
	    IL_0238:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_023d:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	    IL_0242:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	    IL_0247:  ldstr bytearray (
	3d 00 3d 00 3d 00 20 00 53 00 65 00 6e 00 64 00  // =.=.=. .S.e.n.d.
	52 00 65 00 71 00 75 00 65 00 73 00 74 00 41 00  // R.e.q.u.e.s.t.A.
	73 00 79 00 6e 00 63 00 d3 7e 5f 67 3a 00 20 00  // s.y.n.c..~_g:. .
	d3 7e 9c 67 3d 00 01 )                           // .~.g=..
	
	    IL_024c:  ldloc.3 
	    IL_024d:  box !0
	    IL_0252:  brfalse.s IL_025b

	    IL_0254:  ldstr bytearray (
	10 62 9f 52 01 )                                 // .b.R.
	
	    IL_0259:  br.s IL_0260

	    IL_025b:  ldstr "null"
	    IL_0260:  ldstr " ==="
	    IL_0265:  call string string::Concat(string, string, string)
	    IL_026a:  call void class [mscorlib]System.Console::WriteLine(string)
	    IL_026f:  ldloc.3 
	    IL_0270:  stloc.2 
	    IL_0271:  leave IL_02f7

	  } // end .try 0
	  catch class [mscorlib]System.Exception { // 0
	    IL_0276:  stloc.s 5
	    IL_0278:  ldstr bytearray (
	49 7b 85 5f cd 54 94 5e f6 65 d1 53 1f 75 02 5f  // I{._.T.^.e.S.u._
	38 5e 3a 00 20 00 01 )                           // 8^:. ..
	
	    IL_027d:  ldloc.s 5
	    IL_027f:  callvirt instance string class [mscorlib]System.Exception::get_Message()
	    IL_0284:  ldstr bytearray (
	2c 00 20 00 06 58 08 68 3a 00 20 00 01 )         // ,. ..X.h:. ..
	
	    IL_0289:  ldloc.s 5
	    IL_028b:  callvirt instance string class [mscorlib]System.Exception::get_StackTrace()
	    IL_0290:  call string string::Concat(string, string, string, string)
	    IL_0295:  call void class [mscorlib]System.Console::WriteLine(string)
	    IL_029a:  ldarg.0 
	    IL_029b:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_02a0:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	    IL_02a5:  callvirt instance bool class [mscorlib]System.Threading.CancellationTokenSource::get_IsCancellationRequested()
	    IL_02aa:  brtrue.s IL_02bc

	    IL_02ac:  ldarg.0 
	    IL_02ad:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_02b2:  ldfld class [mscorlib]System.Threading.CancellationTokenSource class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::cts
	    IL_02b7:  callvirt instance void class [mscorlib]System.Threading.CancellationTokenSource::Cancel()
	    IL_02bc:  ldloc.1 
	    IL_02bd:  ldarg.0 
	    IL_02be:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	    IL_02c3:  ldfld class [mscorlib]System.EventHandler`1<unsigned int8[]> class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0>::'handler'
	    IL_02c8:  call instance void class DeviceCommunicationLibrary.DeviceCommunicator::remove_DataReceived(class [mscorlib]System.EventHandler`1<unsigned int8[]>)
	    IL_02cd:  ldloca.s 2
	    IL_02cf:  initobj !0
	    IL_02d5:  leave.s IL_02f7

	  } // end handler 0
	} // end .try 1
	catch class [mscorlib]System.Exception { // 1
	  IL_02d7:  stloc.s 6
	  IL_02d9:  ldarg.0 
	  IL_02da:  ldc.i4.s 0xfffffffe
	  IL_02dc:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>1__state'
	  IL_02e1:  ldarg.0 
	  IL_02e2:  ldnull 
	  IL_02e3:  stfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	  IL_02e8:  ldarg.0 
	  IL_02e9:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>t__builder'
	  IL_02ee:  ldloc.s 6
	  IL_02f0:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!T>::SetException(class [mscorlib]System.Exception)
	  IL_02f5:  leave.s IL_0312

	} // end handler 1
	IL_02f7:  ldarg.0 
	IL_02f8:  ldc.i4.s 0xfffffffe
	IL_02fa:  stfld int32 valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>1__state'
	IL_02ff:  ldarg.0 
	IL_0300:  ldnull 
	IL_0301:  stfld class DeviceCommunicationLibrary.DeviceCommunicator/'<>c__DisplayClass37_0`1'<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>8__1'
	IL_0306:  ldarg.0 
	IL_0307:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>t__builder'
	IL_030c:  ldloc.2 
	IL_030d:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!T>::SetResult(!0)
	IL_0312:  ret 
    } // end of method <SendRequestAsync>d__37`1::MoveNext

    // method line 219
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x518c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!0> valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SendRequestAsync>d__37`1'<!0>::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<!T>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <SendRequestAsync>d__37`1::SetStateMachine

  } // end of class <SendRequestAsync>d__37`1

  .class nested private auto ansi sealed beforefieldinit '<SetStringRegisterAsync>d__51'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>t__builder'
    .field  public  bool needReply
    .field  public  unsigned int16 registerId
    .field  public  string 'value'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>u__1'

    // method line 220
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x519c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 206 (0xce)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.BaseRegisterResponse	V_2,
		class DeviceCommunicationLibrary.SetStringRegisterRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0079

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.SetStringRegisterRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::needReply
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_NeedReply(bool)
	  IL_0022:  dup 
	  IL_0023:  ldarg.0 
	  IL_0024:  ldfld unsigned int16 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::registerId
	  IL_0029:  callvirt instance void class DeviceCommunicationLibrary.SetStringRegisterRequest::set_RegisterId(unsigned int16)
	  IL_002e:  dup 
	  IL_002f:  ldarg.0 
	  IL_0030:  ldfld string DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'value'
	  IL_0035:  callvirt instance void class DeviceCommunicationLibrary.SetStringRegisterRequest::set_StringValue(string)
	  IL_003a:  stloc.3 
	  IL_003b:  ldloc.1 
	  IL_003c:  ldloc.3 
	  IL_003d:  ldarg.0 
	  IL_003e:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::timeoutMs
	  IL_0043:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.BaseRegisterResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_0048:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetAwaiter()
	  IL_004d:  stloc.s 4
	  IL_004f:  ldloca.s 4
	  IL_0051:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_IsCompleted()
	  IL_0056:  brtrue.s IL_0096

	  IL_0058:  ldarg.0 
	  IL_0059:  ldc.i4.0 
	  IL_005a:  dup 
	  IL_005b:  stloc.0 
	  IL_005c:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	  IL_0061:  ldarg.0 
	  IL_0062:  ldloc.s 4
	  IL_0064:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>u__1'
	  IL_0069:  ldarg.0 
	  IL_006a:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	  IL_006f:  ldloca.s 4
	  IL_0071:  ldarg.0 
	  IL_0072:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'> ([out] !!0&, [out] !!1&)
	  IL_0077:  leave.s IL_00cd

	  IL_0079:  ldarg.0 
	  IL_007a:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>u__1'
	  IL_007f:  stloc.s 4
	  IL_0081:  ldarg.0 
	  IL_0082:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>u__1'
	  IL_0087:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>
	  IL_008d:  ldarg.0 
	  IL_008e:  ldc.i4.m1 
	  IL_008f:  dup 
	  IL_0090:  stloc.0 
	  IL_0091:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	  IL_0096:  ldloca.s 4
	  IL_0098:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetResult()
	  IL_009d:  stloc.2 
	  IL_009e:  leave.s IL_00b9

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_00a0:  stloc.s 5
	  IL_00a2:  ldarg.0 
	  IL_00a3:  ldc.i4.s 0xfffffffe
	  IL_00a5:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	  IL_00aa:  ldarg.0 
	  IL_00ab:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	  IL_00b0:  ldloc.s 5
	  IL_00b2:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00b7:  leave.s IL_00cd

	} // end handler 0
	IL_00b9:  ldarg.0 
	IL_00ba:  ldc.i4.s 0xfffffffe
	IL_00bc:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>1__state'
	IL_00c1:  ldarg.0 
	IL_00c2:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	IL_00c7:  ldloc.2 
	IL_00c8:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetResult(!0)
	IL_00cd:  ret 
    } // end of method <SetStringRegisterAsync>d__51::MoveNext

    // method line 221
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x5288
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetStringRegisterAsync>d__51'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <SetStringRegisterAsync>d__51::SetStateMachine

  } // end of class <SetStringRegisterAsync>d__51

  .class nested private auto ansi sealed beforefieldinit '<SetValueRegisterAsync>d__49'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>t__builder'
    .field  public  bool needReply
    .field  public  unsigned int16 registerId
    .field  public  unsigned int32 'value'
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>u__1'

    // method line 222
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x5298
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 229 (0xe5)
	.maxstack 4
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.BaseRegisterResponse	V_2,
		class DeviceCommunicationLibrary.SetValueRegisterRequest	V_3,
		valuetype DeviceCommunicationLibrary.ValueRegister	V_4,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>	V_5,
		class [mscorlib]System.Exception	V_6)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_0090

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.SetValueRegisterRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::needReply
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_NeedReply(bool)
	  IL_0022:  dup 
	  IL_0023:  callvirt instance class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> class DeviceCommunicationLibrary.SetValueRegisterRequest::get_Registers()
	  IL_0028:  ldloca.s 4
	  IL_002a:  initobj DeviceCommunicationLibrary.ValueRegister
	  IL_0030:  ldloca.s 4
	  IL_0032:  ldarg.0 
	  IL_0033:  ldfld unsigned int16 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::registerId
	  IL_0038:  call instance void valuetype DeviceCommunicationLibrary.ValueRegister::set_RegisterId(unsigned int16)
	  IL_003d:  ldloca.s 4
	  IL_003f:  ldarg.0 
	  IL_0040:  ldfld unsigned int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'value'
	  IL_0045:  call instance void valuetype DeviceCommunicationLibrary.ValueRegister::set_Value(unsigned int32)
	  IL_004a:  ldloc.s 4
	  IL_004c:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister>::Add(!0)
	  IL_0051:  stloc.3 
	  IL_0052:  ldloc.1 
	  IL_0053:  ldloc.3 
	  IL_0054:  ldarg.0 
	  IL_0055:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::timeoutMs
	  IL_005a:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.BaseRegisterResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_005f:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetAwaiter()
	  IL_0064:  stloc.s 5
	  IL_0066:  ldloca.s 5
	  IL_0068:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_IsCompleted()
	  IL_006d:  brtrue.s IL_00ad

	  IL_006f:  ldarg.0 
	  IL_0070:  ldc.i4.0 
	  IL_0071:  dup 
	  IL_0072:  stloc.0 
	  IL_0073:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	  IL_0078:  ldarg.0 
	  IL_0079:  ldloc.s 5
	  IL_007b:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>u__1'
	  IL_0080:  ldarg.0 
	  IL_0081:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	  IL_0086:  ldloca.s 5
	  IL_0088:  ldarg.0 
	  IL_0089:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'> ([out] !!0&, [out] !!1&)
	  IL_008e:  leave.s IL_00e4

	  IL_0090:  ldarg.0 
	  IL_0091:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>u__1'
	  IL_0096:  stloc.s 5
	  IL_0098:  ldarg.0 
	  IL_0099:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>u__1'
	  IL_009e:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>
	  IL_00a4:  ldarg.0 
	  IL_00a5:  ldc.i4.m1 
	  IL_00a6:  dup 
	  IL_00a7:  stloc.0 
	  IL_00a8:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	  IL_00ad:  ldloca.s 5
	  IL_00af:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetResult()
	  IL_00b4:  stloc.2 
	  IL_00b5:  leave.s IL_00d0

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_00b7:  stloc.s 6
	  IL_00b9:  ldarg.0 
	  IL_00ba:  ldc.i4.s 0xfffffffe
	  IL_00bc:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	  IL_00c1:  ldarg.0 
	  IL_00c2:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	  IL_00c7:  ldloc.s 6
	  IL_00c9:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00ce:  leave.s IL_00e4

	} // end handler 0
	IL_00d0:  ldarg.0 
	IL_00d1:  ldc.i4.s 0xfffffffe
	IL_00d3:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>1__state'
	IL_00d8:  ldarg.0 
	IL_00d9:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	IL_00de:  ldloc.2 
	IL_00df:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetResult(!0)
	IL_00e4:  ret 
    } // end of method <SetValueRegisterAsync>d__49::MoveNext

    // method line 223
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x539c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegisterAsync>d__49'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <SetValueRegisterAsync>d__49::SetStateMachine

  } // end of class <SetValueRegisterAsync>d__49

  .class nested private auto ansi sealed beforefieldinit '<SetValueRegistersAsync>d__50'
  	extends [mscorlib]System.ValueType
  	implements [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine  {
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  public  int32 '<>1__state'
    .field  public  valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>t__builder'
    .field  public  bool needReply
    .field  public  class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> registers
    .field  public  class DeviceCommunicationLibrary.DeviceCommunicator '<>4__this'
    .field  public  int32 timeoutMs
    .field  private  valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> '<>u__1'

    // method line 224
    .method private final virtual hidebysig newslot 
           instance default void MoveNext ()  cil managed 
    {
        // Method begins at RVA 0x53ac
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::MoveNext
	// Code size 194 (0xc2)
	.maxstack 3
	.locals init (
		int32	V_0,
		class DeviceCommunicationLibrary.DeviceCommunicator	V_1,
		class DeviceCommunicationLibrary.BaseRegisterResponse	V_2,
		class DeviceCommunicationLibrary.SetValueRegisterRequest	V_3,
		valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>	V_4,
		class [mscorlib]System.Exception	V_5)
	IL_0000:  ldarg.0 
	IL_0001:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	IL_0006:  stloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldfld class DeviceCommunicationLibrary.DeviceCommunicator DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>4__this'
	IL_000d:  stloc.1 
	.try { // 0
	  IL_000e:  ldloc.0 
	  IL_000f:  brfalse.s IL_006d

	  IL_0011:  newobj instance void class DeviceCommunicationLibrary.SetValueRegisterRequest::'.ctor'()
	  IL_0016:  dup 
	  IL_0017:  ldarg.0 
	  IL_0018:  ldfld bool DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::needReply
	  IL_001d:  callvirt instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_NeedReply(bool)
	  IL_0022:  dup 
	  IL_0023:  ldarg.0 
	  IL_0024:  ldfld class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::registers
	  IL_0029:  callvirt instance void class DeviceCommunicationLibrary.SetValueRegisterRequest::set_Registers(class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister>)
	  IL_002e:  stloc.3 
	  IL_002f:  ldloc.1 
	  IL_0030:  ldloc.3 
	  IL_0031:  ldarg.0 
	  IL_0032:  ldfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::timeoutMs
	  IL_0037:  call instance class [mscorlib]System.Threading.Tasks.Task`1<!!0> class DeviceCommunicationLibrary.DeviceCommunicator::SendRequestAsync<class DeviceCommunicationLibrary.BaseRegisterResponse> (class DeviceCommunicationLibrary.BaseFrame, int32)
	  IL_003c:  callvirt instance valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<!0> class [mscorlib]System.Threading.Tasks.Task`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetAwaiter()
	  IL_0041:  stloc.s 4
	  IL_0043:  ldloca.s 4
	  IL_0045:  call instance bool valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::get_IsCompleted()
	  IL_004a:  brtrue.s IL_008a

	  IL_004c:  ldarg.0 
	  IL_004d:  ldc.i4.0 
	  IL_004e:  dup 
	  IL_004f:  stloc.0 
	  IL_0050:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	  IL_0055:  ldarg.0 
	  IL_0056:  ldloc.s 4
	  IL_0058:  stfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>u__1'
	  IL_005d:  ldarg.0 
	  IL_005e:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	  IL_0063:  ldloca.s 4
	  IL_0065:  ldarg.0 
	  IL_0066:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::AwaitUnsafeOnCompleted<valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>, valuetype DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'> ([out] !!0&, [out] !!1&)
	  IL_006b:  leave.s IL_00c1

	  IL_006d:  ldarg.0 
	  IL_006e:  ldfld valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>u__1'
	  IL_0073:  stloc.s 4
	  IL_0075:  ldarg.0 
	  IL_0076:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>u__1'
	  IL_007b:  initobj valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>
	  IL_0081:  ldarg.0 
	  IL_0082:  ldc.i4.m1 
	  IL_0083:  dup 
	  IL_0084:  stloc.0 
	  IL_0085:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	  IL_008a:  ldloca.s 4
	  IL_008c:  call instance !0 valuetype [mscorlib]System.Runtime.CompilerServices.TaskAwaiter`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::GetResult()
	  IL_0091:  stloc.2 
	  IL_0092:  leave.s IL_00ad

	} // end .try 0
	catch class [mscorlib]System.Exception { // 0
	  IL_0094:  stloc.s 5
	  IL_0096:  ldarg.0 
	  IL_0097:  ldc.i4.s 0xfffffffe
	  IL_0099:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	  IL_009e:  ldarg.0 
	  IL_009f:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	  IL_00a4:  ldloc.s 5
	  IL_00a6:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetException(class [mscorlib]System.Exception)
	  IL_00ab:  leave.s IL_00c1

	} // end handler 0
	IL_00ad:  ldarg.0 
	IL_00ae:  ldc.i4.s 0xfffffffe
	IL_00b0:  stfld int32 DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>1__state'
	IL_00b5:  ldarg.0 
	IL_00b6:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	IL_00bb:  ldloc.2 
	IL_00bc:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetResult(!0)
	IL_00c1:  ret 
    } // end of method <SetValueRegistersAsync>d__50::MoveNext

    // method line 225
    .method private final virtual hidebysig newslot 
           instance default void SetStateMachine (class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine stateMachine)  cil managed 
    {
        .custom instance void class [mscorlib]System.Diagnostics.DebuggerHiddenAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x548c
	.override class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine::SetStateMachine
	// Code size 13 (0xd)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldflda valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse> DeviceCommunicationLibrary.DeviceCommunicator/'<SetValueRegistersAsync>d__50'::'<>t__builder'
	IL_0006:  ldarg.1 
	IL_0007:  call instance void valuetype [mscorlib]System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1<class DeviceCommunicationLibrary.BaseRegisterResponse>::SetStateMachine(class [mscorlib]System.Runtime.CompilerServices.IAsyncStateMachine)
	IL_000c:  ret 
    } // end of method <SetValueRegistersAsync>d__50::SetStateMachine

  } // end of class <SetValueRegistersAsync>d__50

  } // end of class DeviceCommunicationLibrary.DeviceCommunicator
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetDownloadStatusResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int8 '<Status>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8[] '<FileId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int32 '<Offset>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 63
    .method public hidebysig specialname 
           instance default unsigned int8 get_Status ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3450
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8 DeviceCommunicationLibrary.GetDownloadStatusResponse::'<Status>k__BackingField'
	IL_0006:  ret 
    } // end of method GetDownloadStatusResponse::get_Status

    // method line 64
    .method private hidebysig specialname 
           instance default void set_Status (unsigned int8 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3458
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8 DeviceCommunicationLibrary.GetDownloadStatusResponse::'<Status>k__BackingField'
	IL_0007:  ret 
    } // end of method GetDownloadStatusResponse::set_Status

    // method line 65
    .method public hidebysig specialname 
           instance default unsigned int8[] get_FileId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3461
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8[] DeviceCommunicationLibrary.GetDownloadStatusResponse::'<FileId>k__BackingField'
	IL_0006:  ret 
    } // end of method GetDownloadStatusResponse::get_FileId

    // method line 66
    .method private hidebysig specialname 
           instance default void set_FileId (unsigned int8[] 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3469
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8[] DeviceCommunicationLibrary.GetDownloadStatusResponse::'<FileId>k__BackingField'
	IL_0007:  ret 
    } // end of method GetDownloadStatusResponse::set_FileId

    // method line 67
    .method public hidebysig specialname 
           instance default unsigned int32 get_Offset ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3472
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.GetDownloadStatusResponse::'<Offset>k__BackingField'
	IL_0006:  ret 
    } // end of method GetDownloadStatusResponse::get_Offset

    // method line 68
    .method private hidebysig specialname 
           instance default void set_Offset (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x347a
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.GetDownloadStatusResponse::'<Offset>k__BackingField'
	IL_0007:  ret 
    } // end of method GetDownloadStatusResponse::set_Offset

    // method line 69
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3484
	// Code size 101 (0x65)
	.maxstack 5
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0063

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.s 0x15
	IL_001d:  blt.s IL_0063

	IL_001f:  ldarg.0 
	IL_0020:  ldarg.0 
	IL_0021:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0026:  ldc.i4.0 
	IL_0027:  ldelem.u1 
	IL_0028:  call instance void class DeviceCommunicationLibrary.GetDownloadStatusResponse::set_Status(unsigned int8)
	IL_002d:  ldarg.0 
	IL_002e:  ldc.i4.s 0x10
	IL_0030:  newarr [mscorlib]System.Byte
	IL_0035:  call instance void class DeviceCommunicationLibrary.GetDownloadStatusResponse::set_FileId(unsigned int8[])
	IL_003a:  ldarg.0 
	IL_003b:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0040:  ldc.i4.1 
	IL_0041:  ldarg.0 
	IL_0042:  call instance unsigned int8[] class DeviceCommunicationLibrary.GetDownloadStatusResponse::get_FileId()
	IL_0047:  ldc.i4.0 
	IL_0048:  ldc.i4.s 0x10
	IL_004a:  call void class [mscorlib]System.Array::Copy(class [mscorlib]System.Array, int32, class [mscorlib]System.Array, int32, int32)
	IL_004f:  ldarg.0 
	IL_0050:  ldarg.0 
	IL_0051:  ldarg.0 
	IL_0052:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0057:  ldc.i4.s 0x11
	IL_0059:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_005e:  call instance void class DeviceCommunicationLibrary.GetDownloadStatusResponse::set_Offset(unsigned int32)
	IL_0063:  ldc.i4.1 
	IL_0064:  ret 
    } // end of method GetDownloadStatusResponse::Parse

    // method line 70
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x34f5
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method GetDownloadStatusResponse::.ctor

	.property instance unsigned int8 Status ()
	{
		.get instance default unsigned int8 DeviceCommunicationLibrary.GetDownloadStatusResponse::get_Status () 
		.set instance default void DeviceCommunicationLibrary.GetDownloadStatusResponse::set_Status (unsigned int8 'value') 
	}
	.property instance unsigned int8[] FileId ()
	{
		.get instance default unsigned int8[] DeviceCommunicationLibrary.GetDownloadStatusResponse::get_FileId () 
		.set instance default void DeviceCommunicationLibrary.GetDownloadStatusResponse::set_FileId (unsigned int8[] 'value') 
	}
	.property instance unsigned int32 Offset ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.GetDownloadStatusResponse::get_Offset () 
		.set instance default void DeviceCommunicationLibrary.GetDownloadStatusResponse::set_Offset (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.GetDownloadStatusResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit DownloadCompleteRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 71
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x34fd
	// Code size 30 (0x1e)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 143
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ldarg.0 
	IL_0012:  ldc.i4.0 
	IL_0013:  newarr [mscorlib]System.Byte
	IL_0018:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001d:  ret 
    } // end of method DownloadCompleteRequest::.ctor

  } // end of class DeviceCommunicationLibrary.DownloadCompleteRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit DownloadCompleteResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Res>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 72
    .method public hidebysig specialname 
           instance default unsigned int32 get_Res ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x351c
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.DownloadCompleteResponse::'<Res>k__BackingField'
	IL_0006:  ret 
    } // end of method DownloadCompleteResponse::get_Res

    // method line 73
    .method private hidebysig specialname 
           instance default void set_Res (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3524
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.DownloadCompleteResponse::'<Res>k__BackingField'
	IL_0007:  ret 
    } // end of method DownloadCompleteResponse::set_Res

    // method line 74
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x352d
	// Code size 51 (0x33)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0031

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0031

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  ldarg.0 
	IL_0021:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0026:  ldc.i4.0 
	IL_0027:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_002c:  call instance void class DeviceCommunicationLibrary.DownloadCompleteResponse::set_Res(unsigned int32)
	IL_0031:  ldc.i4.1 
	IL_0032:  ret 
    } // end of method DownloadCompleteResponse::Parse

    // method line 75
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3561
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method DownloadCompleteResponse::.ctor

	.property instance unsigned int32 Res ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.DownloadCompleteResponse::get_Res () 
		.set instance default void DeviceCommunicationLibrary.DownloadCompleteResponse::set_Res (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.DownloadCompleteResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetDownloadStatusRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 76
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3569
	// Code size 30 (0x1e)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 133
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ldarg.0 
	IL_0012:  ldc.i4.0 
	IL_0013:  newarr [mscorlib]System.Byte
	IL_0018:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001d:  ret 
    } // end of method GetDownloadStatusRequest::.ctor

  } // end of class DeviceCommunicationLibrary.GetDownloadStatusRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit ChangeStatusRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int8 '<Status>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 77
    .method public hidebysig specialname 
           instance default unsigned int8 get_Status ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3588
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8 DeviceCommunicationLibrary.ChangeStatusRequest::'<Status>k__BackingField'
	IL_0006:  ret 
    } // end of method ChangeStatusRequest::get_Status

    // method line 78
    .method public hidebysig specialname 
           instance default void set_Status (unsigned int8 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3590
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8 DeviceCommunicationLibrary.ChangeStatusRequest::'<Status>k__BackingField'
	IL_0007:  ret 
    } // end of method ChangeStatusRequest::set_Status

    // method line 79
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3599
	// Code size 15 (0xf)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x71
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ret 
    } // end of method ChangeStatusRequest::.ctor

    // method line 80
    .method family virtual hidebysig 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x35a9
	// Code size 2 (0x2)
	.maxstack 8
	IL_0000:  ldc.i4.3 
	IL_0001:  ret 
    } // end of method ChangeStatusRequest::CalculateContentLength

    // method line 81
    .method public virtual hidebysig 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x35ac
	// Code size 28 (0x1c)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldc.i4.1 
	IL_0002:  newarr [mscorlib]System.Byte
	IL_0007:  dup 
	IL_0008:  ldc.i4.0 
	IL_0009:  ldarg.0 
	IL_000a:  call instance unsigned int8 class DeviceCommunicationLibrary.ChangeStatusRequest::get_Status()
	IL_000f:  stelem.i1 
	IL_0010:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_0015:  ldarg.0 
	IL_0016:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	IL_001b:  ret 
    } // end of method ChangeStatusRequest::ToBytes

	.property instance unsigned int8 Status ()
	{
		.get instance default unsigned int8 DeviceCommunicationLibrary.ChangeStatusRequest::get_Status () 
		.set instance default void DeviceCommunicationLibrary.ChangeStatusRequest::set_Status (unsigned int8 'value') 
	}
  } // end of class DeviceCommunicationLibrary.ChangeStatusRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit RestartRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 82
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x35c9
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x70
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method RestartRequest::.ctor

  } // end of class DeviceCommunicationLibrary.RestartRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetGifInfoRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 83
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x35e5
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x61
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method GetGifInfoRequest::.ctor

  } // end of class DeviceCommunicationLibrary.GetGifInfoRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetFlashInfoRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 84
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3601
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x62
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method GetFlashInfoRequest::.ctor

  } // end of class DeviceCommunicationLibrary.GetFlashInfoRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit ConnectDeviceRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 85
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x361d
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x62
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method ConnectDeviceRequest::.ctor

  } // end of class DeviceCommunicationLibrary.ConnectDeviceRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit ExitRunningRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 86
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3639
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x63
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method ExitRunningRequest::.ctor

  } // end of class DeviceCommunicationLibrary.ExitRunningRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit ChangeStatusResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Res>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 87
    .method public hidebysig specialname 
           instance default unsigned int32 get_Res ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3655
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.ChangeStatusResponse::'<Res>k__BackingField'
	IL_0006:  ret 
    } // end of method ChangeStatusResponse::get_Res

    // method line 88
    .method private hidebysig specialname 
           instance default void set_Res (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x365d
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.ChangeStatusResponse::'<Res>k__BackingField'
	IL_0007:  ret 
    } // end of method ChangeStatusResponse::set_Res

    // method line 89
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3668
	// Code size 87 (0x57)
	.maxstack 3
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0032

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0032

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0025:  ldc.i4.0 
	IL_0026:  call unsigned int32 class [mscorlib]System.BitConverter::ToUInt32(unsigned int8[], int32)
	IL_002b:  call instance void class DeviceCommunicationLibrary.ChangeStatusResponse::set_Res(unsigned int32)
	IL_0030:  br.s IL_0055

	IL_0032:  ldstr bytearray (
	43 00 68 00 61 00 6e 00 67 00 65 00 53 00 74 00  // C.h.a.n.g.e.S.t.
	61 00 74 00 75 00 73 00 52 00 65 00 73 00 70 00  // a.t.u.s.R.e.s.p.
	6f 00 6e 00 73 00 65 00 20 00 85 51 b9 5b 7f 95  // o.n.s.e. ..Q.[..
	a6 5e 0d 4e b3 8d 3a 00 20 00 7b 00 30 00 7d 00  // .^.N..:. .{.0.}.
	01 )                                             // .
	
	IL_0037:  ldarg.0 
	IL_0038:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_003d:  dup 
	IL_003e:  brtrue.s IL_0044

	IL_0040:  pop 
	IL_0041:  ldc.i4.0 
	IL_0042:  br.s IL_0046

	IL_0044:  ldlen 
	IL_0045:  conv.i4 
	IL_0046:  box [mscorlib]System.Int32
	IL_004b:  call string string::Format(string, object)
	IL_0050:  call void class [mscorlib]System.Console::WriteLine(string)
	IL_0055:  ldc.i4.1 
	IL_0056:  ret 
    } // end of method ChangeStatusResponse::Parse

    // method line 90
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x36cb
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method ChangeStatusResponse::.ctor

	.property instance unsigned int32 Res ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.ChangeStatusResponse::get_Res () 
		.set instance default void DeviceCommunicationLibrary.ChangeStatusResponse::set_Res (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.ChangeStatusResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit RestartResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Res>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 91
    .method public hidebysig specialname 
           instance default unsigned int32 get_Res ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x36d3
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.RestartResponse::'<Res>k__BackingField'
	IL_0006:  ret 
    } // end of method RestartResponse::get_Res

    // method line 92
    .method private hidebysig specialname 
           instance default void set_Res (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x36db
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.RestartResponse::'<Res>k__BackingField'
	IL_0007:  ret 
    } // end of method RestartResponse::set_Res

    // method line 93
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x36e4
	// Code size 50 (0x32)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0030

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0030

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0025:  ldc.i4.0 
	IL_0026:  call unsigned int32 class [mscorlib]System.BitConverter::ToUInt32(unsigned int8[], int32)
	IL_002b:  call instance void class DeviceCommunicationLibrary.RestartResponse::set_Res(unsigned int32)
	IL_0030:  ldc.i4.1 
	IL_0031:  ret 
    } // end of method RestartResponse::Parse

    // method line 94
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3717
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method RestartResponse::.ctor

	.property instance unsigned int32 Res ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.RestartResponse::get_Res () 
		.set instance default void DeviceCommunicationLibrary.RestartResponse::set_Res (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.RestartResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetGifInfoResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int16 '<Num>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  class [mscorlib]System.Collections.Generic.List`1<string> '<Names>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 95
    .method public hidebysig specialname 
           instance default unsigned int16 get_Num ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x371f
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.GetGifInfoResponse::'<Num>k__BackingField'
	IL_0006:  ret 
    } // end of method GetGifInfoResponse::get_Num

    // method line 96
    .method private hidebysig specialname 
           instance default void set_Num (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3727
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.GetGifInfoResponse::'<Num>k__BackingField'
	IL_0007:  ret 
    } // end of method GetGifInfoResponse::set_Num

    // method line 97
    .method public hidebysig specialname 
           instance default class [mscorlib]System.Collections.Generic.List`1<string> get_Names ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3730
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.Collections.Generic.List`1<string> DeviceCommunicationLibrary.GetGifInfoResponse::'<Names>k__BackingField'
	IL_0006:  ret 
    } // end of method GetGifInfoResponse::get_Names

    // method line 98
    .method private hidebysig specialname 
           instance default void set_Names (class [mscorlib]System.Collections.Generic.List`1<string> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3738
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld class [mscorlib]System.Collections.Generic.List`1<string> DeviceCommunicationLibrary.GetGifInfoResponse::'<Names>k__BackingField'
	IL_0007:  ret 
    } // end of method GetGifInfoResponse::set_Names

    // method line 99
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3744
	// Code size 117 (0x75)
	.maxstack 4
	.locals init (
		int32	V_0,
		int32	V_1,
		string	V_2)
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0073

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.2 
	IL_001c:  blt.s IL_0073

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0025:  ldc.i4.0 
	IL_0026:  call unsigned int16 class [mscorlib]System.BitConverter::ToUInt16(unsigned int8[], int32)
	IL_002b:  call instance void class DeviceCommunicationLibrary.GetGifInfoResponse::set_Num(unsigned int16)
	IL_0030:  ldc.i4.2 
	IL_0031:  stloc.0 
	IL_0032:  ldc.i4.0 
	IL_0033:  stloc.1 
	IL_0034:  br.s IL_005d

	IL_0036:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_ASCII()
	IL_003b:  ldarg.0 
	IL_003c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0041:  ldloc.0 
	IL_0042:  ldc.i4.4 
	IL_0043:  callvirt instance string class [mscorlib]System.Text.Encoding::GetString(unsigned int8[], int32, int32)
	IL_0048:  stloc.2 
	IL_0049:  ldarg.0 
	IL_004a:  call instance class [mscorlib]System.Collections.Generic.List`1<string> class DeviceCommunicationLibrary.GetGifInfoResponse::get_Names()
	IL_004f:  ldloc.2 
	IL_0050:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<string>::Add(!0)
	IL_0055:  ldloc.0 
	IL_0056:  ldc.i4.4 
	IL_0057:  add 
	IL_0058:  stloc.0 
	IL_0059:  ldloc.1 
	IL_005a:  ldc.i4.1 
	IL_005b:  add 
	IL_005c:  stloc.1 
	IL_005d:  ldloc.1 
	IL_005e:  ldarg.0 
	IL_005f:  call instance unsigned int16 class DeviceCommunicationLibrary.GetGifInfoResponse::get_Num()
	IL_0064:  bge.s IL_0073

	IL_0066:  ldloc.0 
	IL_0067:  ldc.i4.4 
	IL_0068:  add 
	IL_0069:  ldarg.0 
	IL_006a:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_006f:  ldlen 
	IL_0070:  conv.i4 
	IL_0071:  ble.s IL_0036

	IL_0073:  ldc.i4.1 
	IL_0074:  ret 
    } // end of method GetGifInfoResponse::Parse

    // method line 100
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x37c5
	// Code size 18 (0x12)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<string>::'.ctor'()
	IL_0006:  stfld class [mscorlib]System.Collections.Generic.List`1<string> DeviceCommunicationLibrary.GetGifInfoResponse::'<Names>k__BackingField'
	IL_000b:  ldarg.0 
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0011:  ret 
    } // end of method GetGifInfoResponse::.ctor

	.property instance unsigned int16 Num ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.GetGifInfoResponse::get_Num () 
		.set instance default void DeviceCommunicationLibrary.GetGifInfoResponse::set_Num (unsigned int16 'value') 
	}
	.property instance class [mscorlib]System.Collections.Generic.List`1<string> Names ()
	{
		.get instance default class [mscorlib]System.Collections.Generic.List`1<string> DeviceCommunicationLibrary.GetGifInfoResponse::get_Names () 
		.set instance default void DeviceCommunicationLibrary.GetGifInfoResponse::set_Names (class [mscorlib]System.Collections.Generic.List`1<string> 'value') 
	}
  } // end of class DeviceCommunicationLibrary.GetGifInfoResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetFlashInfoResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<FreeSpace>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 101
    .method public hidebysig specialname 
           instance default unsigned int32 get_FreeSpace ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x37d8
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.GetFlashInfoResponse::'<FreeSpace>k__BackingField'
	IL_0006:  ret 
    } // end of method GetFlashInfoResponse::get_FreeSpace

    // method line 102
    .method private hidebysig specialname 
           instance default void set_FreeSpace (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x37e0
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.GetFlashInfoResponse::'<FreeSpace>k__BackingField'
	IL_0007:  ret 
    } // end of method GetFlashInfoResponse::set_FreeSpace

    // method line 103
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x37e9
	// Code size 50 (0x32)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0030

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0030

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0025:  ldc.i4.0 
	IL_0026:  call unsigned int32 class [mscorlib]System.BitConverter::ToUInt32(unsigned int8[], int32)
	IL_002b:  call instance void class DeviceCommunicationLibrary.GetFlashInfoResponse::set_FreeSpace(unsigned int32)
	IL_0030:  ldc.i4.1 
	IL_0031:  ret 
    } // end of method GetFlashInfoResponse::Parse

    // method line 104
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x381c
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method GetFlashInfoResponse::.ctor

	.property instance unsigned int32 FreeSpace ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.GetFlashInfoResponse::get_FreeSpace () 
		.set instance default void DeviceCommunicationLibrary.GetFlashInfoResponse::set_FreeSpace (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.GetFlashInfoResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GenericFrameResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 105
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3824
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method GenericFrameResponse::.ctor

  } // end of class DeviceCommunicationLibrary.GenericFrameResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit BaseRegisterResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int8 '<Status>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 106
    .method public hidebysig specialname 
           instance default unsigned int8 get_Status ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x382c
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8 DeviceCommunicationLibrary.BaseRegisterResponse::'<Status>k__BackingField'
	IL_0006:  ret 
    } // end of method BaseRegisterResponse::get_Status

    // method line 107
    .method family hidebysig specialname 
           instance default void set_Status (unsigned int8 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3834
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8 DeviceCommunicationLibrary.BaseRegisterResponse::'<Status>k__BackingField'
	IL_0007:  ret 
    } // end of method BaseRegisterResponse::set_Status

    // method line 108
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x383d
	// Code size 44 (0x2c)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_002a

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  brfalse.s IL_002a

	IL_001c:  ldarg.0 
	IL_001d:  ldarg.0 
	IL_001e:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0023:  ldc.i4.0 
	IL_0024:  ldelem.u1 
	IL_0025:  call instance void class DeviceCommunicationLibrary.BaseRegisterResponse::set_Status(unsigned int8)
	IL_002a:  ldc.i4.1 
	IL_002b:  ret 
    } // end of method BaseRegisterResponse::Parse

    // method line 109
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x386a
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method BaseRegisterResponse::.ctor

	.property instance unsigned int8 Status ()
	{
		.get instance default unsigned int8 DeviceCommunicationLibrary.BaseRegisterResponse::get_Status () 
		.set instance default void DeviceCommunicationLibrary.BaseRegisterResponse::set_Status (unsigned int8 'value') 
	}
  } // end of class DeviceCommunicationLibrary.BaseRegisterResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit HandshakeRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 110
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3872
	// Code size 30 (0x1e)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 128
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ldarg.0 
	IL_0012:  ldc.i4.0 
	IL_0013:  newarr [mscorlib]System.Byte
	IL_0018:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001d:  ret 
    } // end of method HandshakeRequest::.ctor

  } // end of class DeviceCommunicationLibrary.HandshakeRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit HandshakeResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<MaxPackageSize>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 111
    .method public hidebysig specialname 
           instance default unsigned int32 get_MaxPackageSize ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3891
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.HandshakeResponse::'<MaxPackageSize>k__BackingField'
	IL_0006:  ret 
    } // end of method HandshakeResponse::get_MaxPackageSize

    // method line 112
    .method private hidebysig specialname 
           instance default void set_MaxPackageSize (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3899
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.HandshakeResponse::'<MaxPackageSize>k__BackingField'
	IL_0007:  ret 
    } // end of method HandshakeResponse::set_MaxPackageSize

    // method line 113
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x38a2
	// Code size 18 (0x12)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 192
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ret 
    } // end of method HandshakeResponse::.ctor

    // method line 114
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x38b5
	// Code size 51 (0x33)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0031

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0031

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  ldarg.0 
	IL_0021:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0026:  ldc.i4.0 
	IL_0027:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_002c:  call instance void class DeviceCommunicationLibrary.HandshakeResponse::set_MaxPackageSize(unsigned int32)
	IL_0031:  ldc.i4.1 
	IL_0032:  ret 
    } // end of method HandshakeResponse::Parse

	.property instance unsigned int32 MaxPackageSize ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.HandshakeResponse::get_MaxPackageSize () 
		.set instance default void DeviceCommunicationLibrary.HandshakeResponse::set_MaxPackageSize (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.HandshakeResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetHardwareInfoRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {

    // method line 115
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x38e9
	// Code size 27 (0x1b)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.s 0x72
	IL_0009:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_000e:  ldarg.0 
	IL_000f:  ldc.i4.0 
	IL_0010:  newarr [mscorlib]System.Byte
	IL_0015:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_001a:  ret 
    } // end of method GetHardwareInfoRequest::.ctor

  } // end of class DeviceCommunicationLibrary.GetHardwareInfoRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit GetHardwareInfoResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  string '<IcId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int16 '<MaxAcfSize>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int16 '<DisplayHeight>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int16 '<DisplayWidth>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  string '<ProductId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 116
    .method public hidebysig specialname 
           instance default string get_IcId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3905
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld string DeviceCommunicationLibrary.GetHardwareInfoResponse::'<IcId>k__BackingField'
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::get_IcId

    // method line 117
    .method private hidebysig specialname 
           instance default void set_IcId (string 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x390d
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld string DeviceCommunicationLibrary.GetHardwareInfoResponse::'<IcId>k__BackingField'
	IL_0007:  ret 
    } // end of method GetHardwareInfoResponse::set_IcId

    // method line 118
    .method public hidebysig specialname 
           instance default unsigned int16 get_MaxAcfSize ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3916
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<MaxAcfSize>k__BackingField'
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::get_MaxAcfSize

    // method line 119
    .method private hidebysig specialname 
           instance default void set_MaxAcfSize (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x391e
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<MaxAcfSize>k__BackingField'
	IL_0007:  ret 
    } // end of method GetHardwareInfoResponse::set_MaxAcfSize

    // method line 120
    .method public hidebysig specialname 
           instance default unsigned int16 get_DisplayHeight ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3927
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<DisplayHeight>k__BackingField'
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::get_DisplayHeight

    // method line 121
    .method private hidebysig specialname 
           instance default void set_DisplayHeight (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x392f
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<DisplayHeight>k__BackingField'
	IL_0007:  ret 
    } // end of method GetHardwareInfoResponse::set_DisplayHeight

    // method line 122
    .method public hidebysig specialname 
           instance default unsigned int16 get_DisplayWidth ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3938
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<DisplayWidth>k__BackingField'
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::get_DisplayWidth

    // method line 123
    .method private hidebysig specialname 
           instance default void set_DisplayWidth (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3940
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::'<DisplayWidth>k__BackingField'
	IL_0007:  ret 
    } // end of method GetHardwareInfoResponse::set_DisplayWidth

    // method line 124
    .method public hidebysig specialname 
           instance default string get_ProductId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3949
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld string DeviceCommunicationLibrary.GetHardwareInfoResponse::'<ProductId>k__BackingField'
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::get_ProductId

    // method line 125
    .method private hidebysig specialname 
           instance default void set_ProductId (string 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3951
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld string DeviceCommunicationLibrary.GetHardwareInfoResponse::'<ProductId>k__BackingField'
	IL_0007:  ret 
    } // end of method GetHardwareInfoResponse::set_ProductId

    // method line 126
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x395c
	// Code size 170 (0xaa)
	.maxstack 5
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse IL_00a8

	IL_0016:  ldarg.0 
	IL_0017:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_001c:  ldlen 
	IL_001d:  conv.i4 
	IL_001e:  ldc.i4.s 0x2e
	IL_0020:  blt IL_00a8

	IL_0025:  ldarg.0 
	IL_0026:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_ASCII()
	IL_002b:  ldarg.0 
	IL_002c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0031:  ldc.i4.0 
	IL_0032:  ldc.i4.8 
	IL_0033:  callvirt instance string class [mscorlib]System.Text.Encoding::GetString(unsigned int8[], int32, int32)
	IL_0038:  ldc.i4.1 
	IL_0039:  newarr [mscorlib]System.Char
	IL_003e:  callvirt instance string string::TrimEnd(char[])
	IL_0043:  call instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::set_IcId(string)
	IL_0048:  ldarg.0 
	IL_0049:  ldarg.0 
	IL_004a:  ldarg.0 
	IL_004b:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0050:  ldc.i4.8 
	IL_0051:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::FromBigEndian(unsigned int8[], int32)
	IL_0056:  call instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::set_MaxAcfSize(unsigned int16)
	IL_005b:  ldarg.0 
	IL_005c:  ldarg.0 
	IL_005d:  ldarg.0 
	IL_005e:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0063:  ldc.i4.s 0x0a
	IL_0065:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::FromBigEndian(unsigned int8[], int32)
	IL_006a:  call instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::set_DisplayHeight(unsigned int16)
	IL_006f:  ldarg.0 
	IL_0070:  ldarg.0 
	IL_0071:  ldarg.0 
	IL_0072:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0077:  ldc.i4.s 0x0c
	IL_0079:  call instance unsigned int16 class DeviceCommunicationLibrary.BaseFrame::FromBigEndian(unsigned int8[], int32)
	IL_007e:  call instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::set_DisplayWidth(unsigned int16)
	IL_0083:  ldarg.0 
	IL_0084:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_ASCII()
	IL_0089:  ldarg.0 
	IL_008a:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_008f:  ldc.i4.s 0x0e
	IL_0091:  ldc.i4.s 0x20
	IL_0093:  callvirt instance string class [mscorlib]System.Text.Encoding::GetString(unsigned int8[], int32, int32)
	IL_0098:  ldc.i4.1 
	IL_0099:  newarr [mscorlib]System.Char
	IL_009e:  callvirt instance string string::TrimEnd(char[])
	IL_00a3:  call instance void class DeviceCommunicationLibrary.GetHardwareInfoResponse::set_ProductId(string)
	IL_00a8:  ldc.i4.1 
	IL_00a9:  ret 
    } // end of method GetHardwareInfoResponse::Parse

    // method line 127
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3a12
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method GetHardwareInfoResponse::.ctor

	.property instance string IcId ()
	{
		.get instance default string DeviceCommunicationLibrary.GetHardwareInfoResponse::get_IcId () 
		.set instance default void DeviceCommunicationLibrary.GetHardwareInfoResponse::set_IcId (string 'value') 
	}
	.property instance unsigned int16 MaxAcfSize ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::get_MaxAcfSize () 
		.set instance default void DeviceCommunicationLibrary.GetHardwareInfoResponse::set_MaxAcfSize (unsigned int16 'value') 
	}
	.property instance unsigned int16 DisplayHeight ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::get_DisplayHeight () 
		.set instance default void DeviceCommunicationLibrary.GetHardwareInfoResponse::set_DisplayHeight (unsigned int16 'value') 
	}
	.property instance unsigned int16 DisplayWidth ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.GetHardwareInfoResponse::get_DisplayWidth () 
		.set instance default void DeviceCommunicationLibrary.GetHardwareInfoResponse::set_DisplayWidth (unsigned int16 'value') 
	}
	.property instance string ProductId ()
	{
		.get instance default string DeviceCommunicationLibrary.GetHardwareInfoResponse::get_ProductId () 
		.set instance default void DeviceCommunicationLibrary.GetHardwareInfoResponse::set_ProductId (string 'value') 
	}
  } // end of class DeviceCommunicationLibrary.GetHardwareInfoResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit RequestDownloadRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Addr>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int32 '<FileSize>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8[] '<FileId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 128
    .method public hidebysig specialname 
           instance default unsigned int32 get_Addr ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a1a
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::'<Addr>k__BackingField'
	IL_0006:  ret 
    } // end of method RequestDownloadRequest::get_Addr

    // method line 129
    .method public hidebysig specialname 
           instance default void set_Addr (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a22
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::'<Addr>k__BackingField'
	IL_0007:  ret 
    } // end of method RequestDownloadRequest::set_Addr

    // method line 130
    .method public hidebysig specialname 
           instance default unsigned int32 get_FileSize ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a2b
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::'<FileSize>k__BackingField'
	IL_0006:  ret 
    } // end of method RequestDownloadRequest::get_FileSize

    // method line 131
    .method public hidebysig specialname 
           instance default void set_FileSize (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a33
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::'<FileSize>k__BackingField'
	IL_0007:  ret 
    } // end of method RequestDownloadRequest::set_FileSize

    // method line 132
    .method public hidebysig specialname 
           instance default unsigned int8[] get_FileId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a3c
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8[] DeviceCommunicationLibrary.RequestDownloadRequest::'<FileId>k__BackingField'
	IL_0006:  ret 
    } // end of method RequestDownloadRequest::get_FileId

    // method line 133
    .method public hidebysig specialname 
           instance default void set_FileId (unsigned int8[] 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3a44
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8[] DeviceCommunicationLibrary.RequestDownloadRequest::'<FileId>k__BackingField'
	IL_0007:  ret 
    } // end of method RequestDownloadRequest::set_FileId

    // method line 134
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3a4d
	// Code size 31 (0x1f)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 129
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ldarg.0 
	IL_0012:  ldc.i4.s 0x10
	IL_0014:  newarr [mscorlib]System.Byte
	IL_0019:  call instance void class DeviceCommunicationLibrary.RequestDownloadRequest::set_FileId(unsigned int8[])
	IL_001e:  ret 
    } // end of method RequestDownloadRequest::.ctor

    // method line 135
    .method family virtual hidebysig 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x3a6d
	// Code size 3 (0x3)
	.maxstack 8
	IL_0000:  ldc.i4.s 0x1a
	IL_0002:  ret 
    } // end of method RequestDownloadRequest::CalculateContentLength

    // method line 136
    .method public virtual hidebysig 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x3a74
	// Code size 73 (0x49)
	.maxstack 3
	.locals init (
		class [mscorlib]System.Collections.Generic.List`1<unsigned int8>	V_0)
	IL_0000:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::'.ctor'()
	IL_0005:  stloc.0 
	IL_0006:  ldloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldarg.0 
	IL_0009:  call instance unsigned int32 class DeviceCommunicationLibrary.RequestDownloadRequest::get_Addr()
	IL_000e:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int32)
	IL_0013:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0018:  ldloc.0 
	IL_0019:  ldarg.0 
	IL_001a:  ldarg.0 
	IL_001b:  call instance unsigned int32 class DeviceCommunicationLibrary.RequestDownloadRequest::get_FileSize()
	IL_0020:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int32)
	IL_0025:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_002a:  ldloc.0 
	IL_002b:  ldarg.0 
	IL_002c:  call instance unsigned int8[] class DeviceCommunicationLibrary.RequestDownloadRequest::get_FileId()
	IL_0031:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0036:  ldarg.0 
	IL_0037:  ldloc.0 
	IL_0038:  callvirt instance !0[] class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::ToArray()
	IL_003d:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_0042:  ldarg.0 
	IL_0043:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	IL_0048:  ret 
    } // end of method RequestDownloadRequest::ToBytes

	.property instance unsigned int32 Addr ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::get_Addr () 
		.set instance default void DeviceCommunicationLibrary.RequestDownloadRequest::set_Addr (unsigned int32 'value') 
	}
	.property instance unsigned int32 FileSize ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.RequestDownloadRequest::get_FileSize () 
		.set instance default void DeviceCommunicationLibrary.RequestDownloadRequest::set_FileSize (unsigned int32 'value') 
	}
	.property instance unsigned int8[] FileId ()
	{
		.get instance default unsigned int8[] DeviceCommunicationLibrary.RequestDownloadRequest::get_FileId () 
		.set instance default void DeviceCommunicationLibrary.RequestDownloadRequest::set_FileId (unsigned int8[] 'value') 
	}
  } // end of class DeviceCommunicationLibrary.RequestDownloadRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit RequestDownloadResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<MaxPackageSize>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int32 '<Res>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 137
    .method public hidebysig specialname 
           instance default unsigned int32 get_MaxPackageSize ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ac9
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::'<MaxPackageSize>k__BackingField'
	IL_0006:  ret 
    } // end of method RequestDownloadResponse::get_MaxPackageSize

    // method line 138
    .method private hidebysig specialname 
           instance default void set_MaxPackageSize (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ad1
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::'<MaxPackageSize>k__BackingField'
	IL_0007:  ret 
    } // end of method RequestDownloadResponse::set_MaxPackageSize

    // method line 139
    .method public hidebysig specialname 
           instance default unsigned int32 get_Res ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ada
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::'<Res>k__BackingField'
	IL_0006:  ret 
    } // end of method RequestDownloadResponse::get_Res

    // method line 140
    .method private hidebysig specialname 
           instance default void set_Res (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ae2
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::'<Res>k__BackingField'
	IL_0007:  ret 
    } // end of method RequestDownloadResponse::set_Res

    // method line 141
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3aec
	// Code size 70 (0x46)
	.maxstack 4
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0044

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.8 
	IL_001c:  blt.s IL_0044

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  ldarg.0 
	IL_0021:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0026:  ldc.i4.0 
	IL_0027:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_002c:  call instance void class DeviceCommunicationLibrary.RequestDownloadResponse::set_MaxPackageSize(unsigned int32)
	IL_0031:  ldarg.0 
	IL_0032:  ldarg.0 
	IL_0033:  ldarg.0 
	IL_0034:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0039:  ldc.i4.4 
	IL_003a:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_003f:  call instance void class DeviceCommunicationLibrary.RequestDownloadResponse::set_Res(unsigned int32)
	IL_0044:  ldc.i4.1 
	IL_0045:  ret 
    } // end of method RequestDownloadResponse::Parse

    // method line 142
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3b3e
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method RequestDownloadResponse::.ctor

	.property instance unsigned int32 MaxPackageSize ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::get_MaxPackageSize () 
		.set instance default void DeviceCommunicationLibrary.RequestDownloadResponse::set_MaxPackageSize (unsigned int32 'value') 
	}
	.property instance unsigned int32 Res ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.RequestDownloadResponse::get_Res () 
		.set instance default void DeviceCommunicationLibrary.RequestDownloadResponse::set_Res (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.RequestDownloadResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit DownloadDataRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Offset>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8[] '<Data>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 143
    .method public hidebysig specialname 
           instance default unsigned int32 get_Offset ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3b46
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.DownloadDataRequest::'<Offset>k__BackingField'
	IL_0006:  ret 
    } // end of method DownloadDataRequest::get_Offset

    // method line 144
    .method public hidebysig specialname 
           instance default void set_Offset (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3b4e
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.DownloadDataRequest::'<Offset>k__BackingField'
	IL_0007:  ret 
    } // end of method DownloadDataRequest::set_Offset

    // method line 145
    .method public hidebysig specialname 
           instance default unsigned int8[] get_Data ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3b57
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8[] DeviceCommunicationLibrary.DownloadDataRequest::'<Data>k__BackingField'
	IL_0006:  ret 
    } // end of method DownloadDataRequest::get_Data

    // method line 146
    .method public hidebysig specialname 
           instance default void set_Data (unsigned int8[] 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3b5f
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8[] DeviceCommunicationLibrary.DownloadDataRequest::'<Data>k__BackingField'
	IL_0007:  ret 
    } // end of method DownloadDataRequest::set_Data

    // method line 147
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3b68
	// Code size 18 (0x12)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 130
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ret 
    } // end of method DownloadDataRequest::.ctor

    // method line 148
    .method family virtual hidebysig 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x3b7b
	// Code size 19 (0x13)
	.maxstack 8
	IL_0000:  ldc.i4.6 
	IL_0001:  ldarg.0 
	IL_0002:  call instance unsigned int8[] class DeviceCommunicationLibrary.DownloadDataRequest::get_Data()
	IL_0007:  dup 
	IL_0008:  brtrue.s IL_000e

	IL_000a:  pop 
	IL_000b:  ldc.i4.0 
	IL_000c:  br.s IL_0010

	IL_000e:  ldlen 
	IL_000f:  conv.i4 
	IL_0010:  add 
	IL_0011:  conv.u2 
	IL_0012:  ret 
    } // end of method DownloadDataRequest::CalculateContentLength

    // method line 149
    .method public virtual hidebysig 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x3b90
	// Code size 63 (0x3f)
	.maxstack 3
	.locals init (
		class [mscorlib]System.Collections.Generic.List`1<unsigned int8>	V_0)
	IL_0000:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::'.ctor'()
	IL_0005:  stloc.0 
	IL_0006:  ldloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  ldarg.0 
	IL_0009:  call instance unsigned int32 class DeviceCommunicationLibrary.DownloadDataRequest::get_Offset()
	IL_000e:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int32)
	IL_0013:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0018:  ldarg.0 
	IL_0019:  call instance unsigned int8[] class DeviceCommunicationLibrary.DownloadDataRequest::get_Data()
	IL_001e:  brfalse.s IL_002c

	IL_0020:  ldloc.0 
	IL_0021:  ldarg.0 
	IL_0022:  call instance unsigned int8[] class DeviceCommunicationLibrary.DownloadDataRequest::get_Data()
	IL_0027:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_002c:  ldarg.0 
	IL_002d:  ldloc.0 
	IL_002e:  callvirt instance !0[] class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::ToArray()
	IL_0033:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_0038:  ldarg.0 
	IL_0039:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	IL_003e:  ret 
    } // end of method DownloadDataRequest::ToBytes

	.property instance unsigned int32 Offset ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.DownloadDataRequest::get_Offset () 
		.set instance default void DeviceCommunicationLibrary.DownloadDataRequest::set_Offset (unsigned int32 'value') 
	}
	.property instance unsigned int8[] Data ()
	{
		.get instance default unsigned int8[] DeviceCommunicationLibrary.DownloadDataRequest::get_Data () 
		.set instance default void DeviceCommunicationLibrary.DownloadDataRequest::set_Data (unsigned int8[] 'value') 
	}
  } // end of class DeviceCommunicationLibrary.DownloadDataRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit DownloadDataResponse
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  unsigned int32 '<Res>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 150
    .method public hidebysig specialname 
           instance default unsigned int32 get_Res ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3bdb
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.DownloadDataResponse::'<Res>k__BackingField'
	IL_0006:  ret 
    } // end of method DownloadDataResponse::get_Res

    // method line 151
    .method private hidebysig specialname 
           instance default void set_Res (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3be3
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.DownloadDataResponse::'<Res>k__BackingField'
	IL_0007:  ret 
    } // end of method DownloadDataResponse::set_Res

    // method line 152
    .method public virtual hidebysig 
           instance default bool Parse (unsigned int8[] data)  cil managed 
    {
        // Method begins at RVA 0x3bec
	// Code size 51 (0x33)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  call instance bool class DeviceCommunicationLibrary.BaseFrame::Parse(unsigned int8[])
	IL_0007:  brtrue.s IL_000b

	IL_0009:  ldc.i4.0 
	IL_000a:  ret 
	IL_000b:  ldarg.0 
	IL_000c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0011:  brfalse.s IL_0031

	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0019:  ldlen 
	IL_001a:  conv.i4 
	IL_001b:  ldc.i4.4 
	IL_001c:  blt.s IL_0031

	IL_001e:  ldarg.0 
	IL_001f:  ldarg.0 
	IL_0020:  ldarg.0 
	IL_0021:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::get_Content()
	IL_0026:  ldc.i4.0 
	IL_0027:  call instance unsigned int32 class DeviceCommunicationLibrary.BaseFrame::FromBigEndianUInt32(unsigned int8[], int32)
	IL_002c:  call instance void class DeviceCommunicationLibrary.DownloadDataResponse::set_Res(unsigned int32)
	IL_0031:  ldc.i4.1 
	IL_0032:  ret 
    } // end of method DownloadDataResponse::Parse

    // method line 153
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3c20
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ret 
    } // end of method DownloadDataResponse::.ctor

	.property instance unsigned int32 Res ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.DownloadDataResponse::get_Res () 
		.set instance default void DeviceCommunicationLibrary.DownloadDataResponse::set_Res (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.DownloadDataResponse
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi abstract sealed beforefieldinit ProtocolConstants
  	extends [mscorlib]System.Object
  {
    .field public static literal  unsigned int16 SF = int16(0x00004148)
    .field public static literal  unsigned int16 EF = int16(0x00004d49)
    .field public static literal  unsigned int16 CMD_HANDSHAKE_REQ = int16(0x00000080)
    .field public static literal  unsigned int16 CMD_HANDSHAKE_RESP = int16(0x000000c0)
    .field public static literal  unsigned int16 CMD_GET_HW_INFO_REQ = int16(0x00000072)
    .field public static literal  unsigned int16 CMD_GET_HW_INFO_RESP = int16(0x000000b2)
    .field public static literal  unsigned int16 CMD_GET_DOWNLOAD_STATUS_REQ = int16(0x00000085)
    .field public static literal  unsigned int16 CMD_GET_DOWNLOAD_STATUS_RESP = int16(0x000000c5)
    .field public static literal  unsigned int16 CMD_REQUEST_DOWNLOAD_REQ = int16(0x00000081)
    .field public static literal  unsigned int16 CMD_REQUEST_DOWNLOAD_RESP = int16(0x000000c1)
    .field public static literal  unsigned int16 CMD_DOWNLOAD_DATA_REQ = int16(0x00000082)
    .field public static literal  unsigned int16 CMD_DOWNLOAD_DATA_RESP = int16(0x000000c2)
    .field public static literal  unsigned int16 CMD_DOWNLOAD_COMPLETE_REQ = int16(0x0000008f)
    .field public static literal  unsigned int16 CMD_DOWNLOAD_COMPLETE_RESP = int16(0x000000cf)
    .field public static literal  unsigned int16 CMD_UPLOAD_DATA_REQ = int16(0x00000083)
    .field public static literal  unsigned int16 CMD_UPLOAD_DATA_RESP = int16(0x000000c3)
    .field public static literal  unsigned int16 CMD_CHANGE_STATUS_REQ = int16(0x00000071)
    .field public static literal  unsigned int16 CMD_CHANGE_STATUS_RESP = int16(0x000000b1)
    .field public static literal  unsigned int16 CMD_RESTART_REQ = int16(0x00000070)
    .field public static literal  unsigned int16 CMD_RESTART_RESP = int16(0x000000b0)
    .field public static literal  unsigned int16 CMD_REGISTER_OPERATION = int16(0x00000090)
    .field public static literal  unsigned int16 CMD_REGISTER_RESPONSE = int16(0x000000d0)
    .field public static literal  unsigned int16 CMD_GET_GIF_INFO_REQ = int16(0x00000061)
    .field public static literal  unsigned int16 CMD_GET_GIF_INFO_RESP = int16(0x000000a1)
    .field public static literal  unsigned int16 CMD_GET_FLASH_INFO_REQ = int16(0x00000062)
    .field public static literal  unsigned int16 CMD_GET_FLASH_INFO_RESP = int16(0x000000a2)
    .field public static literal  unsigned int16 CMD_CONNECT_DEVICE = int16(0x00000062)
    .field public static literal  unsigned int16 CMD_EXIT_RUNNING = int16(0x00000063)
    .field public static literal  unsigned int8 STATUS_DOWNLOAD_READY = int8(0x10)
    .field public static literal  unsigned int8 STATUS_DOWNLOADING = int8(0x11)
    .field public static literal  unsigned int8 STATUS_AHMI = int8(0x20)
    .field public static literal  unsigned int8 FUNC_SET_VALUE_REG = int8(0x00)
    .field public static literal  unsigned int8 FUNC_READ_VALUE_REG = int8(0x04)
    .field public static literal  unsigned int8 FUNC_SET_STRING_REG = int8(0x05)
    .field public static literal  unsigned int8 FUNC_READ_STRING_REG = int8(0x06)
    .field public static literal  unsigned int8 FUNC_SET_ARRAY_REG = int8(0x07)
    .field  public static initonly  class [mscorlib]System.Collections.Generic.Dictionary`2<string,valuetype DeviceCommunicationLibrary.FlashAddress> FlashAddresses

    // method line 154
    .method private static hidebysig specialname rtspecialname 
           default void '.cctor' ()  cil managed 
    {
        // Method begins at RVA 0x3c28
	// Code size 241 (0xf1)
	.maxstack 5
	IL_0000:  newobj instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::'.ctor'()
	IL_0005:  dup 
	IL_0006:  ldstr "cpu1.bin"
	IL_000b:  ldc.i4 134479872
	IL_0010:  ldc.i4 614400
	IL_0015:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_001a:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_001f:  dup 
	IL_0020:  ldstr "cpu0_config.bin"
	IL_0025:  ldc.i4 135233536
	IL_002a:  ldc.i4 4096
	IL_002f:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_0034:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_0039:  dup 
	IL_003a:  ldstr "calibration.bin"
	IL_003f:  ldc.i4 135245824
	IL_0044:  ldc.i4 4096
	IL_0049:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_004e:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_0053:  dup 
	IL_0054:  ldstr "EraseStoreSpace.bin"
	IL_0059:  ldc.i4 135249920
	IL_005e:  ldc.i4 4096
	IL_0063:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_0068:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_006d:  dup 
	IL_006e:  ldstr "hwconfig.bin"
	IL_0073:  ldc.i4 135258112
	IL_0078:  ldc.i4 4096
	IL_007d:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_0082:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_0087:  dup 
	IL_0088:  ldstr "product.bin"
	IL_008d:  ldc.i4 135262208
	IL_0092:  ldc.i4 4096
	IL_0097:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_009c:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_00a1:  dup 
	IL_00a2:  ldstr "Texture.acf"
	IL_00a7:  ldc.i4 135266304
	IL_00ac:  ldc.i4 15728640
	IL_00b1:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_00b6:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_00bb:  dup 
	IL_00bc:  ldstr "upg_cfg.bin"
	IL_00c1:  ldc.i4 135229440
	IL_00c6:  ldc.i4 4096
	IL_00cb:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_00d0:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_00d5:  dup 
	IL_00d6:  ldstr "bootloader.bin"
	IL_00db:  ldc.i4 138149888
	IL_00e0:  ldc.i4.0 
	IL_00e1:  newobj instance void valuetype DeviceCommunicationLibrary.FlashAddress::'.ctor'(unsigned int32, unsigned int32)
	IL_00e6:  callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<string, valuetype DeviceCommunicationLibrary.FlashAddress>::Add(!0, !1)
	IL_00eb:  stsfld class [mscorlib]System.Collections.Generic.Dictionary`2<string,valuetype DeviceCommunicationLibrary.FlashAddress> DeviceCommunicationLibrary.ProtocolConstants::FlashAddresses
	IL_00f0:  ret 
    } // end of method ProtocolConstants::.cctor

  } // end of class DeviceCommunicationLibrary.ProtocolConstants
}

.namespace DeviceCommunicationLibrary
{
  .class public sequential ansi sealed beforefieldinit FlashAddress
  	extends [mscorlib]System.ValueType
  {
    .field  private initonly  unsigned int32 '<Address>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private initonly  unsigned int32 '<Size>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 155
    .method public hidebysig specialname 
           instance default unsigned int32 get_Address ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d25
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.FlashAddress::'<Address>k__BackingField'
	IL_0006:  ret 
    } // end of method FlashAddress::get_Address

    // method line 156
    .method public hidebysig specialname 
           instance default unsigned int32 get_Size ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d2d
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.FlashAddress::'<Size>k__BackingField'
	IL_0006:  ret 
    } // end of method FlashAddress::get_Size

    // method line 157
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' (unsigned int32 address, unsigned int32 size)  cil managed 
    {
        // Method begins at RVA 0x3d35
	// Code size 15 (0xf)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.FlashAddress::'<Address>k__BackingField'
	IL_0007:  ldarg.0 
	IL_0008:  ldarg.2 
	IL_0009:  stfld unsigned int32 DeviceCommunicationLibrary.FlashAddress::'<Size>k__BackingField'
	IL_000e:  ret 
    } // end of method FlashAddress::.ctor

	.property instance unsigned int32 Address ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.FlashAddress::get_Address () 
	}
	.property instance unsigned int32 Size ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.FlashAddress::get_Size () 
	}
  } // end of class DeviceCommunicationLibrary.FlashAddress
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi abstract beforefieldinit RegisterOperationRequest
  	extends DeviceCommunicationLibrary.BaseFrame
  {
    .field  private  bool '<NeedReply>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8 '<FunctionCode>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int8 '<RegisterCount>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 158
    .method public hidebysig specialname 
           instance default bool get_NeedReply ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d45
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld bool DeviceCommunicationLibrary.RegisterOperationRequest::'<NeedReply>k__BackingField'
	IL_0006:  ret 
    } // end of method RegisterOperationRequest::get_NeedReply

    // method line 159
    .method public hidebysig specialname 
           instance default void set_NeedReply (bool 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d4d
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld bool DeviceCommunicationLibrary.RegisterOperationRequest::'<NeedReply>k__BackingField'
	IL_0007:  ret 
    } // end of method RegisterOperationRequest::set_NeedReply

    // method line 160
    .method public hidebysig specialname 
           instance default unsigned int8 get_FunctionCode ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d56
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::'<FunctionCode>k__BackingField'
	IL_0006:  ret 
    } // end of method RegisterOperationRequest::get_FunctionCode

    // method line 161
    .method public hidebysig specialname 
           instance default void set_FunctionCode (unsigned int8 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d5e
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::'<FunctionCode>k__BackingField'
	IL_0007:  ret 
    } // end of method RegisterOperationRequest::set_FunctionCode

    // method line 162
    .method public hidebysig specialname 
           instance default unsigned int8 get_RegisterCount ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d67
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::'<RegisterCount>k__BackingField'
	IL_0006:  ret 
    } // end of method RegisterOperationRequest::get_RegisterCount

    // method line 163
    .method public hidebysig specialname 
           instance default void set_RegisterCount (unsigned int8 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3d6f
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::'<RegisterCount>k__BackingField'
	IL_0007:  ret 
    } // end of method RegisterOperationRequest::set_RegisterCount

    // method line 164
    .method family hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3d78
	// Code size 18 (0x12)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.BaseFrame::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4 144
	IL_000c:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_CMD(unsigned int16)
	IL_0011:  ret 
    } // end of method RegisterOperationRequest::.ctor

    // method line 165
    .method family hidebysig 
           instance default unsigned int8 BuildControlByte ()  cil managed 
    {
        // Method begins at RVA 0x3d8c
	// Code size 50 (0x32)
	.maxstack 3
	.locals init (
		unsigned int8	V_0)
	IL_0000:  ldc.i4.0 
	IL_0001:  stloc.0 
	IL_0002:  ldarg.0 
	IL_0003:  call instance bool class DeviceCommunicationLibrary.RegisterOperationRequest::get_NeedReply()
	IL_0008:  brfalse.s IL_0013

	IL_000a:  ldloc.0 
	IL_000b:  ldc.i4 128
	IL_0010:  or 
	IL_0011:  conv.u1 
	IL_0012:  stloc.0 
	IL_0013:  ldloc.0 
	IL_0014:  ldarg.0 
	IL_0015:  call instance unsigned int8 class DeviceCommunicationLibrary.RegisterOperationRequest::get_FunctionCode()
	IL_001a:  ldc.i4.7 
	IL_001b:  and 
	IL_001c:  ldc.i4.4 
	IL_001d:  shl 
	IL_001e:  conv.u1 
	IL_001f:  or 
	IL_0020:  conv.u1 
	IL_0021:  stloc.0 
	IL_0022:  ldloc.0 
	IL_0023:  ldarg.0 
	IL_0024:  call instance unsigned int8 class DeviceCommunicationLibrary.RegisterOperationRequest::get_RegisterCount()
	IL_0029:  ldc.i4.s 0x0f
	IL_002b:  and 
	IL_002c:  conv.u1 
	IL_002d:  or 
	IL_002e:  conv.u1 
	IL_002f:  stloc.0 
	IL_0030:  ldloc.0 
	IL_0031:  ret 
    } // end of method RegisterOperationRequest::BuildControlByte

	.property instance bool NeedReply ()
	{
		.get instance default bool DeviceCommunicationLibrary.RegisterOperationRequest::get_NeedReply () 
		.set instance default void DeviceCommunicationLibrary.RegisterOperationRequest::set_NeedReply (bool 'value') 
	}
	.property instance unsigned int8 FunctionCode ()
	{
		.get instance default unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::get_FunctionCode () 
		.set instance default void DeviceCommunicationLibrary.RegisterOperationRequest::set_FunctionCode (unsigned int8 'value') 
	}
	.property instance unsigned int8 RegisterCount ()
	{
		.get instance default unsigned int8 DeviceCommunicationLibrary.RegisterOperationRequest::get_RegisterCount () 
		.set instance default void DeviceCommunicationLibrary.RegisterOperationRequest::set_RegisterCount (unsigned int8 'value') 
	}
  } // end of class DeviceCommunicationLibrary.RegisterOperationRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit SetValueRegisterRequest
  	extends DeviceCommunicationLibrary.RegisterOperationRequest
  {
    .field  private  class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> '<Registers>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 166
    .method public hidebysig specialname 
           instance default class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> get_Registers ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3dca
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.SetValueRegisterRequest::'<Registers>k__BackingField'
	IL_0006:  ret 
    } // end of method SetValueRegisterRequest::get_Registers

    // method line 167
    .method public hidebysig specialname 
           instance default void set_Registers (class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3dd2
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.SetValueRegisterRequest::'<Registers>k__BackingField'
	IL_0007:  ret 
    } // end of method SetValueRegisterRequest::set_Registers

    // method line 168
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3ddb
	// Code size 25 (0x19)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister>::'.ctor'()
	IL_0006:  stfld class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.SetValueRegisterRequest::'<Registers>k__BackingField'
	IL_000b:  ldarg.0 
	IL_000c:  call instance void class DeviceCommunicationLibrary.RegisterOperationRequest::'.ctor'()
	IL_0011:  ldarg.0 
	IL_0012:  ldc.i4.0 
	IL_0013:  call instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_FunctionCode(unsigned int8)
	IL_0018:  ret 
    } // end of method SetValueRegisterRequest::.ctor

    // method line 169
    .method family virtual hidebysig 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x3df5
	// Code size 17 (0x11)
	.maxstack 8
	IL_0000:  ldc.i4.3 
	IL_0001:  ldarg.0 
	IL_0002:  call instance class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> class DeviceCommunicationLibrary.SetValueRegisterRequest::get_Registers()
	IL_0007:  callvirt instance int32 class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister>::get_Count()
	IL_000c:  ldc.i4.6 
	IL_000d:  mul 
	IL_000e:  add 
	IL_000f:  conv.u2 
	IL_0010:  ret 
    } // end of method SetValueRegisterRequest::CalculateContentLength

    // method line 170
    .method public virtual hidebysig 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x3e08
	// Code size 128 (0x80)
	.maxstack 2
	.locals init (
		class [mscorlib]System.Collections.Generic.List`1<unsigned int8>	V_0,
		valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype DeviceCommunicationLibrary.ValueRegister>	V_1,
		valuetype DeviceCommunicationLibrary.ValueRegister	V_2,
		unsigned int8[]	V_3,
		unsigned int8[]	V_4)
	IL_0000:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::'.ctor'()
	IL_0005:  stloc.0 
	IL_0006:  ldloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  call instance unsigned int8 class DeviceCommunicationLibrary.RegisterOperationRequest::BuildControlByte()
	IL_000d:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_0012:  ldarg.0 
	IL_0013:  call instance class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> class DeviceCommunicationLibrary.SetValueRegisterRequest::get_Registers()
	IL_0018:  callvirt instance valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<!0> class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister>::GetEnumerator()
	IL_001d:  stloc.1 
	.try { // 0
	  IL_001e:  br.s IL_0054

	  IL_0020:  ldloca.s 1
	  IL_0022:  call instance !0 valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype DeviceCommunicationLibrary.ValueRegister>::get_Current()
	  IL_0027:  stloc.2 
	  IL_0028:  ldarg.0 
	  IL_0029:  ldloca.s 2
	  IL_002b:  call instance unsigned int16 valuetype DeviceCommunicationLibrary.ValueRegister::get_RegisterId()
	  IL_0030:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int16)
	  IL_0035:  stloc.3 
	  IL_0036:  ldloc.0 
	  IL_0037:  ldloc.3 
	  IL_0038:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	  IL_003d:  ldarg.0 
	  IL_003e:  ldloca.s 2
	  IL_0040:  call instance unsigned int32 valuetype DeviceCommunicationLibrary.ValueRegister::get_Value()
	  IL_0045:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int32)
	  IL_004a:  stloc.s 4
	  IL_004c:  ldloc.0 
	  IL_004d:  ldloc.s 4
	  IL_004f:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	  IL_0054:  ldloca.s 1
	  IL_0056:  call instance bool valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype DeviceCommunicationLibrary.ValueRegister>::MoveNext()
	  IL_005b:  brtrue.s IL_0020

	  IL_005d:  leave.s IL_006d

	} // end .try 0
	finally  { // 0
	  IL_005f:  ldloca.s 1
	  IL_0061:  constrained. valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype DeviceCommunicationLibrary.ValueRegister>
	  IL_0067:  callvirt instance void class [mscorlib]System.IDisposable::Dispose()
	  IL_006c:  endfinally 
	} // end handler 0
	IL_006d:  ldarg.0 
	IL_006e:  ldloc.0 
	IL_006f:  callvirt instance !0[] class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::ToArray()
	IL_0074:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_0079:  ldarg.0 
	IL_007a:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	IL_007f:  ret 
    } // end of method SetValueRegisterRequest::ToBytes

	.property instance class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> Registers ()
	{
		.get instance default class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> DeviceCommunicationLibrary.SetValueRegisterRequest::get_Registers () 
		.set instance default void DeviceCommunicationLibrary.SetValueRegisterRequest::set_Registers (class [mscorlib]System.Collections.Generic.List`1<valuetype DeviceCommunicationLibrary.ValueRegister> 'value') 
	}
  } // end of class DeviceCommunicationLibrary.SetValueRegisterRequest
}

.namespace DeviceCommunicationLibrary
{
  .class public sequential ansi sealed beforefieldinit ValueRegister
  	extends [mscorlib]System.ValueType
  {
    .field  private  unsigned int16 '<RegisterId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  unsigned int32 '<Value>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 171
    .method public hidebysig specialname 
           instance default unsigned int16 get_RegisterId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ea4
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.ValueRegister::'<RegisterId>k__BackingField'
	IL_0006:  ret 
    } // end of method ValueRegister::get_RegisterId

    // method line 172
    .method public hidebysig specialname 
           instance default void set_RegisterId (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3eac
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.ValueRegister::'<RegisterId>k__BackingField'
	IL_0007:  ret 
    } // end of method ValueRegister::set_RegisterId

    // method line 173
    .method public hidebysig specialname 
           instance default unsigned int32 get_Value ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3eb5
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int32 DeviceCommunicationLibrary.ValueRegister::'<Value>k__BackingField'
	IL_0006:  ret 
    } // end of method ValueRegister::get_Value

    // method line 174
    .method public hidebysig specialname 
           instance default void set_Value (unsigned int32 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ebd
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int32 DeviceCommunicationLibrary.ValueRegister::'<Value>k__BackingField'
	IL_0007:  ret 
    } // end of method ValueRegister::set_Value

	.property instance unsigned int16 RegisterId ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.ValueRegister::get_RegisterId () 
		.set instance default void DeviceCommunicationLibrary.ValueRegister::set_RegisterId (unsigned int16 'value') 
	}
	.property instance unsigned int32 Value ()
	{
		.get instance default unsigned int32 DeviceCommunicationLibrary.ValueRegister::get_Value () 
		.set instance default void DeviceCommunicationLibrary.ValueRegister::set_Value (unsigned int32 'value') 
	}
  } // end of class DeviceCommunicationLibrary.ValueRegister
}

.namespace DeviceCommunicationLibrary
{
  .class public auto ansi beforefieldinit SetStringRegisterRequest
  	extends DeviceCommunicationLibrary.RegisterOperationRequest
  {
    .field  private  unsigned int16 '<RegisterId>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

    .field  private  string '<StringValue>k__BackingField'
    .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....


    // method line 175
    .method public hidebysig specialname 
           instance default unsigned int16 get_RegisterId ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ec6
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld unsigned int16 DeviceCommunicationLibrary.SetStringRegisterRequest::'<RegisterId>k__BackingField'
	IL_0006:  ret 
    } // end of method SetStringRegisterRequest::get_RegisterId

    // method line 176
    .method public hidebysig specialname 
           instance default void set_RegisterId (unsigned int16 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ece
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld unsigned int16 DeviceCommunicationLibrary.SetStringRegisterRequest::'<RegisterId>k__BackingField'
	IL_0007:  ret 
    } // end of method SetStringRegisterRequest::set_RegisterId

    // method line 177
    .method public hidebysig specialname 
           instance default string get_StringValue ()  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3ed7
	// Code size 7 (0x7)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldfld string DeviceCommunicationLibrary.SetStringRegisterRequest::'<StringValue>k__BackingField'
	IL_0006:  ret 
    } // end of method SetStringRegisterRequest::get_StringValue

    // method line 178
    .method public hidebysig specialname 
           instance default void set_StringValue (string 'value')  cil managed 
    {
        .custom instance void class [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::'.ctor'() =  (01 00 00 00 ) // ....

        // Method begins at RVA 0x3edf
	// Code size 8 (0x8)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  ldarg.1 
	IL_0002:  stfld string DeviceCommunicationLibrary.SetStringRegisterRequest::'<StringValue>k__BackingField'
	IL_0007:  ret 
    } // end of method SetStringRegisterRequest::set_StringValue

    // method line 179
    .method public hidebysig specialname rtspecialname 
           instance default void '.ctor' ()  cil managed 
    {
        // Method begins at RVA 0x3ee8
	// Code size 21 (0x15)
	.maxstack 8
	IL_0000:  ldarg.0 
	IL_0001:  call instance void class DeviceCommunicationLibrary.RegisterOperationRequest::'.ctor'()
	IL_0006:  ldarg.0 
	IL_0007:  ldc.i4.5 
	IL_0008:  call instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_FunctionCode(unsigned int8)
	IL_000d:  ldarg.0 
	IL_000e:  ldc.i4.1 
	IL_000f:  call instance void class DeviceCommunicationLibrary.RegisterOperationRequest::set_RegisterCount(unsigned int8)
	IL_0014:  ret 
    } // end of method SetStringRegisterRequest::.ctor

    // method line 180
    .method family virtual hidebysig 
           instance default unsigned int16 CalculateContentLength ()  cil managed 
    {
        // Method begins at RVA 0x3f00
	// Code size 24 (0x18)
	.maxstack 2
	.locals init (
		unsigned int8[]	V_0)
	IL_0000:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_UTF8()
	IL_0005:  ldarg.0 
	IL_0006:  call instance string class DeviceCommunicationLibrary.SetStringRegisterRequest::get_StringValue()
	IL_000b:  callvirt instance unsigned int8[] class [mscorlib]System.Text.Encoding::GetBytes(string)
	IL_0010:  stloc.0 
	IL_0011:  ldc.i4.7 
	IL_0012:  ldloc.0 
	IL_0013:  ldlen 
	IL_0014:  conv.i4 
	IL_0015:  add 
	IL_0016:  conv.u2 
	IL_0017:  ret 
    } // end of method SetStringRegisterRequest::CalculateContentLength

    // method line 181
    .method public virtual hidebysig 
           instance default unsigned int8[] ToBytes ()  cil managed 
    {
        // Method begins at RVA 0x3f24
	// Code size 99 (0x63)
	.maxstack 2
	.locals init (
		class [mscorlib]System.Collections.Generic.List`1<unsigned int8>	V_0,
		unsigned int8[]	V_1,
		unsigned int8[]	V_2,
		unsigned int8[]	V_3)
	IL_0000:  newobj instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::'.ctor'()
	IL_0005:  stloc.0 
	IL_0006:  ldloc.0 
	IL_0007:  ldarg.0 
	IL_0008:  call instance unsigned int8 class DeviceCommunicationLibrary.RegisterOperationRequest::BuildControlByte()
	IL_000d:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::Add(!0)
	IL_0012:  ldarg.0 
	IL_0013:  ldarg.0 
	IL_0014:  call instance unsigned int16 class DeviceCommunicationLibrary.SetStringRegisterRequest::get_RegisterId()
	IL_0019:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int16)
	IL_001e:  stloc.1 
	IL_001f:  ldloc.0 
	IL_0020:  ldloc.1 
	IL_0021:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0026:  call class [mscorlib]System.Text.Encoding class [mscorlib]System.Text.Encoding::get_UTF8()
	IL_002b:  ldarg.0 
	IL_002c:  call instance string class DeviceCommunicationLibrary.SetStringRegisterRequest::get_StringValue()
	IL_0031:  callvirt instance unsigned int8[] class [mscorlib]System.Text.Encoding::GetBytes(string)
	IL_0036:  stloc.2 
	IL_0037:  ldarg.0 
	IL_0038:  ldloc.2 
	IL_0039:  ldlen 
	IL_003a:  conv.i4 
	IL_003b:  conv.u2 
	IL_003c:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::GetBigEndianBytes(unsigned int16)
	IL_0041:  stloc.3 
	IL_0042:  ldloc.0 
	IL_0043:  ldloc.3 
	IL_0044:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0049:  ldloc.0 
	IL_004a:  ldloc.2 
	IL_004b:  callvirt instance void class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::AddRange(class [mscorlib]System.Collections.Generic.IEnumerable`1<!0>)
	IL_0050:  ldarg.0 
	IL_0051:  ldloc.0 
	IL_0052:  callvirt instance !0[] class [mscorlib]System.Collections.Generic.List`1<unsigned int8>::ToArray()
	IL_0057:  call instance void class DeviceCommunicationLibrary.BaseFrame::set_Content(unsigned int8[])
	IL_005c:  ldarg.0 
	IL_005d:  call instance unsigned int8[] class DeviceCommunicationLibrary.BaseFrame::ToBytes()
	IL_0062:  ret 
    } // end of method SetStringRegisterRequest::ToBytes

	.property instance unsigned int16 RegisterId ()
	{
		.get instance default unsigned int16 DeviceCommunicationLibrary.SetStringRegisterRequest::get_RegisterId () 
		.set instance default void DeviceCommunicationLibrary.SetStringRegisterRequest::set_RegisterId (unsigned int16 'value') 
	}
	.property instance string StringValue ()
	{
		.get instance default string DeviceCommunicationLibrary.SetStringRegisterRequest::get_StringValue () 
		.set instance default void DeviceCommunicationLibrary.SetStringRegisterRequest::set_StringValue (string 'value') 
	}
  } // end of class DeviceCommunicationLibrary.SetStringRegisterRequest
}

