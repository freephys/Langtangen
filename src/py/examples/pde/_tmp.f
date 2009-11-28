
      subroutine scheme_f77(up, u, um, x, y, t, nx, ny, Cx2, Cy2,
     &                      dt2, t_old)
      integer nx, ny
      real*8 up(0:nx, 0:ny), u(0:nx, 0:ny), um(0:nx, 0:ny)
      real*8 x(0:nx), y(0:ny)
      real*8 Cx2, Cy2, dt2, t, t_old
Cf2py intent(in, out) up
      real*8 f
      external f

      do j = 1, ny-1
         do i = 1, nx-1
            up(i,j) = - um(i,j) + 2*u(i,j) + 
     &          Cx2*(u(i-1,j) - 2*u(i,j) + u(i+1,j)) +
     &          Cy2*(u(i,j-1) - 2*u(i,j) + u(i,j+1)) +
     &          dt2*f(x(i),y(j),t_old)
         end do
      end do
      return
      end

      subroutine ic_f77(u, um, x, y, nx, ny, Cx2, Cy2, dt)
      integer nx, ny
      real*8 u(0:nx, 0:ny), um(0:nx, 0:ny)
      real*8 x(0:nx), y(0:ny)
      real*8 Cx2, Cy2, dt, dt2
Cf2py intent(in, out) u, um
      real*8 f, ic
      external f, ic

      dt2 = dt*dt
      do j = 0, ny
         do i = 0, nx
            u(i,j) = ic(x(i),y(j))
         end do
      end do
      do j = 1, ny-1
         do i = 1, nx-1
            um(i,j) = u(i,j) +
     &          0.5*Cx2*(u(i-1,j) - 2*u(i,j) + u(i+1,j)) +
     &          0.5*Cy2*(u(i,j-1) - 2*u(i,j) + u(i,j+1)) +
     &          dt2*f(x(i),y(j),0.0D0)
         end do
      end do
C     boundary values:
      call bc_f77(um, x, y, nx, ny, dt)
      return
      end

      subroutine bc_f77(up, x, y, nx, ny, t)
      integer nx, ny
      real*8 up(0:nx, 0:ny)
      real*8 x(0:nx), y(0:ny)
      real*8 t
Cf2py intent(in, out) up
      real*8 bc
      external bc

      i = 0
      do j = 0, ny
         up(i,j) = bc(x(i),y(j),t)
      end do
      j = 0
      do i = 0, nx
         up(i,j) = bc(x(i),y(j),t)
      end do
      i = nx
      do j = 0, ny
         up(i,j) = bc(x(i),y(j),t)
      end do
      j = ny
      do i = 0, nx
         up(i,j) = bc(x(i),y(j),t)
      end do
      return
      end



      real*8 function f(x, y, t)
C     independent variables:
      real*8 x
      real*8 y
      real*8 t

      f = 0.0

      return
      end



      real*8 function bc(x, y, t)
C     independent variables:
      real*8 x
      real*8 y
      real*8 t

      bc = 0.0

      return
      end



      real*8 function ic(x, y)
C     independent variables:
      real*8 x
      real*8 y

C     parameters:
      real*8 Lx
      real*8 Ly
      Lx = 10
      Ly = 10

      ic = exp(-(x-Lx/2.0)**2/2.0 -(y-Ly/2.0)**2/2.0)

      return
      end




      real*8 function pow(x, a)
      real*8 x
C     the power a is usually a number (single precision),
C     note: it cannot be int
      real*4 a
      pow = x**a
      return
      end
      
