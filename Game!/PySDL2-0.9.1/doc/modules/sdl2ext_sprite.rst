.. currentmodule:: sdl2.ext

Sprite, texture and pixel surface routines
==========================================

.. data:: TEXTURE

   Indicates that texture-based rendering or sprite creation is wanted.

.. data:: SOFTWARE

   Indicates that software-based rendering or sprite creation is wanted.

.. class:: Sprite()

   A simple 2D object, implemented as abstract base class.

   .. attribute:: x

      The top-left horizontal offset at which the :class:`Sprite`
      resides.

   .. attribute:: y

      The top-left vertical offset at which the :class:`Sprite`
      resides.

   .. attribute:: position

      The top-left position (:attr:`x` and :attr:`y`) as tuple.

   .. attribute:: size

      The width and height of the :class:`Sprite` as tuple.

      .. note::

         This is an abstract property and needs to be implemented by inheriting
         classes.

   .. attribute:: area

      The rectangular area occupied by the :class:`Sprite`.

   .. attribute:: depth

      The layer depth on which to draw the :class:`Sprite`.
      :class:`Sprite` objects with higher :attr:`depth` values will be
      drawn on top of other :class:`Sprite` values by the
      :class:`SpriteRenderSystem`.

.. class:: SoftwareSprite()

   A simple, visible, pixel-based 2D object, implemented on top of
   SDL2 software surfaces.

   .. attribute:: surface

      The :class:`sdl2.SDL_Surface` containing the pixel data.

   .. attribute:: size

      The size of the :class:`SoftwareSprite` as tuple.

   .. method:: subsprite(area : (int, int, int, int)) -> SoftwareSprite

      Creates another :class:`SoftwareSprite` from a part of the
      :class:`SoftwareSprite`. The two sprites share pixel data, so if the
      parent sprite's surface is not managed by the sprite (``free`` is False),
      you will need to keep it alive while the subsprite exists.

.. class:: TextureSprite()

   A simple, visible, pixel-based 2D object, implemented on top of SDL2
   textures.

   .. attribute:: size

      The size of the :class:`TextureSprite` as tuple.

   .. attribute:: texture

      The :class:`sdl2.SDL_Texture` containing the texture data.

.. class:: SpriteRenderSystem()

   A rendering system for :class:`Sprite` components. This is a base class for
   rendering systems capable of drawing and displaying :class:`Sprite` based
   objects. Inheriting classes need to implement the rendering capability by
   overriding the render() method.

   .. attribute:: sortfunc

      Sort function for the component processing order. The default sort order
      is based on the depth attribute of every sprite. Lower depth values will
      cause sprites to be drawn below sprites with higher depth values.  If
      :attr:`sortfunc` shall be overridden, it must match the callback
      requirements for :func:`sorted()`.

   .. method:: process(world : World, components : iterable) -> None

      Renders the passed :class:`Sprite` objects via the
      :meth:`render()` method. The :class:`Sprite` objects are sorted
      via :attr:`sortfunc` before they are passed to :meth:`render()`.

   .. method:: render(sprite : iterable) -> None

      Renders the :class:`Sprite` objects.

      .. note::

         This is a no-op function and needs to be implemented by inheriting
         classes.

.. class:: SoftwareSpriteRenderSystem(window : object)

   A rendering system for :class:`SoftwareSprite` components. The
   :class:`SoftwareSpriteRenderSystem` class uses a :class:`sdl2.SDL_Window` as
   drawing device to display :class:`SoftwareSprite` surfaces. It uses the
   internal SDL surface of the *window* as drawing context, so that GL
   operations, such as texture handling or the usage of SDL renderers is not
   possible.

   *window* can be either a :class:`sdl2.ext.Window` or
   :class:`sdl2.SDL_Window` instance.

   .. attribute:: window

      The :class:`sdl2.SDL_Window` that is used as drawing device.

   .. attribute:: surface

      The :class:`sdl2.SDL_Surface` that acts as drawing context for
      :attr:`window`.

   .. method:: render(sprites : object[, x=None[, y=None]]) -> None

      Draws the passed *sprites* on the :class:`sdl2.ext.Window` surface. *x*
      and *y* are optional arguments that can be used as relative drawing
      location for *sprites*. If set to ``None``, the location information of
      the *sprites* are used. If set and *sprites* is an iterable, such as a
      list of :class:`SoftwareSprite` objects, *x* and *y* are relative
      location values that will be added to each individual sprite's
      position. If *sprites* is a single :class:`SoftwareSprite`, *x* and *y*
      denote the absolute position of the :class:`SoftwareSprite`, if set.

.. class:: TextureSpriteRenderSystem(target : object)

   A rendering system for :class:`TextureSprite` components. The
   :class:`TextureSpriteRenderSystem` class uses a :class:`sdl2.SDL_Renderer` as
   drawing device to display :class:`Sprite` surfaces.

   *target* can be a :class:`sdl2.ext.Window`, :class:`sdl2.SDL_Window`,
   a:class:`sdl2.ext.Renderer` or a :class:`sdl2.SDL_Renderer`. If it is a
   :class:`sdl2.ext.Window` or :class:`sdl2.SDL_Window` instance, it will try
   to create a :class:`sdl2.SDL_Renderer` with hardware acceleration for it.

   .. attribute:: renderer

      The :class:`sdl2.SDL_Renderer` that is used as drawing context.

   .. attribute:: rendertarget

      The target for which the :attr:`renderer` was created, if any.

   .. method:: render(sprites : object[, x=None[, y=None]]) -> None

      Renders the passed *sprites* via the :attr:`renderer`.  *x* and
      *y* are optional arguments that can be used as relative drawing
      location for *sprites*. If set to ``None``, the location
      information of the *sprites* are used. If set and *sprites* is an
      iterable, such as a list of :class:`TextureSprite` objects, *x*
      and *y* are relative location values that will be added to each
      individual sprite's position. If *sprites* is a single
      :class:`TextureSprite`, *x* and *y* denote the absolute position of the
      :class:`TextureSprite`, if set.

.. class:: SpriteFactory(sprite_type=TEXTURE, **kwargs)

   A factory class for creating :class:`Sprite` objects. The
   :class:`SpriteFactory` can create :class:`TextureSprite` or
   :class:`SoftwareSprite` instances, depending on the *sprite_type*
   being passed to it, which can be ``SOFTWARE`` or ``TEXTURE``. The
   additional *kwargs* are used as default arguments for creating
   sprites within the factory methods.

   .. attribute:: sprite_type

      The sprite type created by the factory. This will be either
      ``SOFTWARE`` for :class:`SoftwareSprite` or ``TEXTURE`` for
      :class:`TextureSprite` objects.

   .. attribute:: default_args

      The default arguments to use for creating new sprites.

   .. method:: create_software_sprite(size, bpp=32, masks=None) -> SoftwareSprite

      Creates a software sprite. A *size* tuple containing the width and
      height of the sprite and a *bpp* value, indicating the bits per
      pixel to be used, need to be provided.

   .. method:: create_sprite(**kwargs) -> Sprite

      Creates a :class:`Sprite`. Depending on the :attr:`sprite_type`,
      this will return a :class:`SoftwareSprite` or
      :class:`TextureSprite`.

      *kwargs* are the arguments to be passed for the sprite
      construction and can vary depending on the sprite type. Usually
      they have to follow the :meth:`create_software_sprite()` and
      :meth:`create_texture_sprite()` method signatures. *kwargs*
      however will be mixed with the set :attr:`default_args` so that
      one does not necessarily have to provide all arguments, if they
      are set within the :attr:`default_args`. If *kwargs* and
      :attr:`default_args` contain the same keys, the key-value pair of
      *kwargs* is chosen.

   .. method:: create_sprite_render_system(*args, **kwargs) -> SpriteRenderSystem

      Creates a new :class:`SpriteRenderSystem`, based on the set
      :attr:`sprite_type`. If :attr:`sprite_type` is ``TEXTURE``, a
      :class:`TextureSpriteRenderSystem` is created with the the
      ``renderer`` from the :attr:`default_args`. Other keyword
      arguments are ignored in that case.

      Otherwise a :class:`SoftwareSpriteRenderSystem` is created and *args*
      and *kwargs* are passed to it.

   .. method:: create_texture_sprite(renderer : object, size, pformat=sdl2.SDL_PIXELFORMAT_RGBA8888, access=sdl2.SDL_TEXTUREACCESS_STATIC) -> TextureSprite

      Creates a texture sprite. A *size* tuple containing the width and
      height of the sprite needs to be provided.

      :class:`TextureSprite` objects are assumed to be static by
      default, making it impossible to access their pixel buffer in
      favour for faster copy operations. If you need to update the pixel
      data frequently or want to use the texture as target for rendering
      operations, *access* can be set to the relevant
      SDL_TEXTUREACCESS_* flag.

   .. method:: from_color(color : object , size, bpp=32, masks=None) -> Sprite

      Creates a :class:`Sprite` with a certain color.

   .. method:: from_image(fname : str) -> Sprite

      Creates a :class:`Sprite` from an image file. The image must be
      loadable via :func:`sdl2.ext.load_image()`.

   .. method:: from_object(obj: object) -> Sprite

      Creates a :class:`Sprite` from an object. The object will be
      passed through :func:`sdl2.rwops_from_object()` in
      order to try to load image data from it.

   .. method:: from_surface(surface : SDL_Surface[, free=False]) -> Sprite

      Creates a :class:`Sprite` from the passed
      :class:`sdl2.SDL_Surface`. If *free* is set to
      ``True``, the passed *surface* will be freed automatically.

   .. method:: from_text(text : str[, **kwargs]) -> Sprite

      Creates a :class:`Sprite` from a string of text. This method
      requires a :class:`sdl2.ext.FontManager` to be in *kwargs* or
      :attr:`default_args`.

.. class:: Renderer(target : obj[, index=-1[, flags=sdl2.SDL_RENDERER_ACCELERATED]])

   A rendering context for windows and sprites that can use hardware or
   software-accelerated graphics drivers.

   If target is a :class:`sdl2.ext.Window` or :class:`sdl2.SDL_Window`,
   *index* and *flags* are passed to the relevant
   :class:`sdl2.SDL_CreateRenderer()` call. If *target* is a
   :class:`SoftwareSprite` or :class:`sdl2.SDL_Surface`, the *index*
   and *flags* arguments are ignored.

   .. attribute:: renderer

      The underlying :class:`sdl2.SDL_Renderer`.

   .. attribute:: rendertarget

      The target for which the :class:`Renderer` was created.

   .. attribute:: color

      The :class:`sdl2.ext.Color` to use for draw and fill operations.

   .. attribute:: blendmode

      The blend mode used for drawing operations (fill and line). This
      can be a value of

      * ``SDL_BLENDMODE_NONE`` for no blending
      * ``SDL_BLENDMODE_BLEND`` for alpha blending
      * ``SDL_BLENDMODE_ADD`` for additive color blending
      * ``SDL_BLENDMODE_MOD`` for multiplied color blending

   .. method:: clear([color=None])

      Clears the rendering context with the currently set or passed
      *color*.

   .. method:: copy(src : obj[, srcrect=None[, dstrect=None]]) -> None

      Copies (blits) the passed *src*, which can be a :class:`TextureSprite` or
      :class:`sdl2.SDL_Texture`, to the target of the
      :class:`Renderer`. *srcrect* is the source rectangle to be used for
      clipping portions of *src*. *dstrect* is the destination rectangle.

   .. method:: draw_line(points : iterable[, color=None]) -> None

      Draws one or multiple lines on the rendering context. The *line*
      argument contains the start and end coordinates of the individual lines
      in the form ``(line1_x1, line1_y1, line1_x2, line1_y2, line2_x1,
      line2_y1, ...)``.

   .. method:: draw_point(points : iterable[, color=None]) -> None

      Draws one or multiple points on the rendering context. The *points*
      argument contains the x and y values of the points as simple sequence in
      the form ``(point1_x, point1_y, point2_x, point2_y, ...)``.

   .. method:: draw_rect(rects : iterable[, color=None]) -> None

      Draws one or multiple rectangles on the rendering context. *rects*
      contains sequences of four values denoting the x and y offset and width
      and height of each individual rectangle in the form ``((x1, y1, w1, h1),
      (x2, y2, w2, h2), ...)``.

   .. method:: fill(rects : iterable[, color=None]) -> None

      Fills one or multiple rectangular areas on the rendering context with
      the current set or passed *color*. *rects* contains sequences of four
      values denoting the x and y offset and width and height of each
      individual rectangle in the form ``((x1, y1, w1, h1), (x2, y2, w2, h2),
      ...)``.

   .. method:: present() -> None

      Refreshes the rendering context, causing changes to the render buffers
      to be shown.
