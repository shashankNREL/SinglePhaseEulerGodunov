module face_velocity_multifab

contains

subroutine build_face_multifab(facemfab)
    use my_amr_module, only : verbose
    use amr_data_module
    implicit none
 
    integer :: idim
    logical :: nodal(3)
    type(amrex_multifab) :: facemfab(amrex_spacedim,0:amrex_max_level)
    integer :: lev, nlevs

    nlevs = amrex_get_finest_level()

    do lev=0,nlevs
       do idim = 1, amrex_spacedim
          nodal = .false.
          nodal(idim) = .true.
          call amrex_multifab_build(facemfab(idim,lev), phi_new(lev)%ba, phi_new(lev)%dm, 1, 0, nodal)
       end do
    end do

end subroutine build_face_multifab

subroutine destroy_face_multifab(facemfab)
    use my_amr_module, only : verbose
    use amr_data_module
    implicit none
 
    integer :: idim
    logical :: nodal(3)
    type(amrex_multifab) :: facemfab(amrex_spacedim,0:amrex_max_level)
    integer :: lev, nlevs

    nlevs = amrex_get_finest_level()

    do lev=0,nlevs
       do idim = 1, amrex_spacedim
          call amrex_multifab_destroy(facemfab(idim,lev))
       end do
    end do

end subroutine destroy_face_multifab


subroutine get_face_velocity_multifab(phi,facemfab)

    use my_amr_module, only : verbose
    use amr_data_module
    use face_velocity_module
    use fillpatch_module, only : fillpatch
    implicit none
  
    real(amrex_real)  :: time

    integer, parameter :: ngrow = 3
    integer :: idim
    logical :: nodal(3)
    type(amrex_multifab) :: phiborder,Uborder
    type(amrex_mfiter) :: mfi
    type(amrex_box) :: bx, tbx, bxnodal
    real(amrex_real), contiguous, pointer, dimension(:,:,:,:) :: pin,pout,pux,puy,puz,pfx,pfy,pfz, &
         pf, pfab, Uin
    type(amrex_fab) :: facevel(amrex_spacedim)
    type(amrex_multifab) :: facemfab(amrex_spacedim,0:amrex_max_level),phi(0:)
    integer :: lev, nlevs, check

    time=0.0d0

    nlevs = amrex_get_finest_level()

    do lev=0,nlevs

    call amrex_multifab_build(phiborder, phi_new(lev)%ba, phi_new(lev)%dm, ncomp, ngrow)
    call amrex_multifab_build(Uborder, phi_new(lev)%ba, phi_new(lev)%dm, ncomp, ngrow)

    call fillpatch(lev, time, phiborder,phi,phi)

    call amrex_mfiter_build(mfi, phi_new(lev), tiling=.true.)
    do while(mfi%next())
       bx = mfi%tilebox()

       pin  => phiborder%dataptr(mfi)
       Uin  => Uborder%dataptr(mfi)

       do idim = 1, amrex_spacedim
          tbx = bx
          call tbx%nodalize(idim)
          call tbx%grow(1)
          call facevel(idim)%resize(tbx,1)
       end do

       pux => facevel(1)%dataptr()
       puy => facevel(2)%dataptr()
#if BL_SPACEDIM == 3
       puz => facevel(3)%dataptr()
#endif

       !call compute_velocity(pin(:,:,:,1),pin(:,:,:,2),pin(:,:,:,3),Uin(:,:,:,1),lbound(pin),ubound(pin))

       call get_face_velocity(pin(:,:,:,1),pin(:,:,:,2),pin(:,:,:,3),pin(:,:,:,4),lbound(pin),ubound(pin), &
            pux, lbound(pux), ubound(pux), &
            puy, lbound(puy), ubound(puy), &
#if BL_SPACEDIM == 3
            puz, lbound(puz), ubound(puz), &
#endif
            amrex_geom(lev)%dx, amrex_problo)


         do idim = 1, amrex_spacedim
             pf => facemfab(idim,lev)%dataptr(mfi)
             pfab => facevel(idim)%dataptr()
             tbx = mfi%nodaltilebox(idim)

	     pf       (tbx%lo(1):tbx%hi(1),tbx%lo(2):tbx%hi(2),tbx%lo(3):tbx%hi(3),:) = &
#if BL_SPACEDIM == 2
             pfab(tbx%lo(1):tbx%hi(1),tbx%lo(2):tbx%hi(2),0:0,:)
#endif
#if BL_SPACEDIM == 3
             pfab(tbx%lo(1):tbx%hi(1),tbx%lo(2):tbx%hi(2),tbx%lo(3):tbx%hi(3),:)
#endif
		!if(idim.eq.1)then
		!print*,lbound(pf),lbound(pfab),ubound(pf),ubound(pfab)
		!print*, bx%lo,tbx%lo,bx%hi,tbx%hi
		!print*, pfab(:,:,0,1)
	 	!endif
          end do

     enddo

     call amrex_mfiter_destroy(mfi)

     do idim = 1, amrex_spacedim
       call amrex_fab_destroy(facevel(idim))
     end do
    !$omp end parallel

    call amrex_multifab_destroy(phiborder)
    call amrex_multifab_destroy(Uborder)

  enddo


end subroutine get_face_velocity_multifab

end module face_velocity_multifab
